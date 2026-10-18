/**
 * ScrollSequenceEngine - 120 FPS Cinematic Canvas Scrubbing Engine
 * Part of landing-page-skill
 *
 * Implements:
 * 1. Two-phase progressive hydration (Instant First Paint -> Sparse Keyframes -> Background Pool)
 * 2. Emil Kowalski spring lerp physics with idle sleep (saves 100% GPU/CPU when still)
 * 3. Sub-frame dual-blend optical crossfade (eliminates frame stepping)
 * 4. Retina / HiDPI sharp rendering via devicePixelRatio
 * 5. Nearest-loaded fallback so canvas NEVER blinks even during fast initial scrubs
 */

export class ScrollSequenceEngine {
  constructor(options = {}) {
    this.canvas = typeof options.canvas === 'string' 
      ? document.querySelector(options.canvas) 
      : options.canvas;
      
    this.container = typeof options.container === 'string' 
      ? document.querySelector(options.container) 
      : options.container;

    if (!this.canvas) throw new Error('ScrollSequenceEngine: valid canvas element or selector is required.');

    this.ctx = this.canvas.getContext('2d', { alpha: true });
    
    // Core parameters
    this.totalFrames = options.totalFrames || 80;
    this.framePattern = options.framePattern || ((i) => `./assets/sequence/frame_${String(i).padStart(3, '0')}.webp`);
    this.keyframeStride = options.keyframeStride || 4;
    this.lerpFactor = options.lerpFactor || 0.18;
    this.opticalCrossfade = options.opticalCrossfade !== false;
    this.fitMode = options.fitMode || 'contain'; // 'contain' | 'cover' | 'fill'
    this.maxConcurrentLoads = options.maxConcurrentLoads || 6;

    // Callbacks
    this.onProgress = options.onProgress || null;
    this.onMilestone = options.onMilestone || null;
    this.milestones = options.milestones || [];

    // Internal state
    this.images = new Array(this.totalFrames).fill(null);
    this.loadedSet = new Set();
    this.targetFrame = 0;
    this.currentFrame = 0;
    this.progress = 0;
    this.isRendering = false;
    this.rafId = null;
    this.lastMilestoneIndex = -1;

    // Concurrency queue
    this.pendingQueue = [];
    this.activeLoads = 0;

    // Bindings
    this.onScroll = this.handleScroll.bind(this);
    this.onResize = this.handleResize.bind(this);
    this.renderLoop = this.render.bind(this);

    this.init();
  }

  init() {
    this.setupCanvasDPI();
    this.attachEvents();
    this.startHydration();
    this.handleScroll(); // Initial compute
  }

  setupCanvasDPI() {
    const dpr = window.devicePixelRatio || 1;
    const rect = this.canvas.getBoundingClientRect();
    const w = rect.width || this.canvas.parentElement?.clientWidth || 640;
    const h = rect.height || this.canvas.parentElement?.clientHeight || 640;

    this.canvas.width = Math.round(w * dpr);
    this.canvas.height = Math.round(h * dpr);
    this.ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    this.displayWidth = w;
    this.displayHeight = h;
  }

  attachEvents() {
    window.addEventListener('scroll', this.onScroll, { passive: true });
    window.addEventListener('resize', this.onResize, { passive: true });

    if (window.ResizeObserver && this.canvas.parentElement) {
      this.resizeObserver = new ResizeObserver(() => this.handleResize());
      this.resizeObserver.observe(this.canvas.parentElement);
    }
  }

  startHydration() {
    // 1. Instant First Paint
    this.preloadImage(0).then(() => {
      this.drawFrame();
    });

    // 2. Schedule Keyframes
    const keyframes = [];
    for (let i = 0; i < this.totalFrames; i += this.keyframeStride) {
      if (i !== 0) keyframes.push(i);
    }
    if (!keyframes.includes(this.totalFrames - 1)) {
      keyframes.push(this.totalFrames - 1);
    }

    // 3. Queue rest
    const remainder = [];
    for (let i = 0; i < this.totalFrames; i++) {
      if (i % this.keyframeStride !== 0 && i !== (this.totalFrames - 1)) {
        remainder.push(i);
      }
    }

    this.pendingQueue = [...keyframes, ...remainder];
    this.processQueue();
  }

  processQueue() {
    while (this.activeLoads < this.maxConcurrentLoads && this.pendingQueue.length > 0) {
      const frameIndex = this.pendingQueue.shift();
      if (this.loadedSet.has(frameIndex)) continue;

      this.activeLoads++;
      this.preloadImage(frameIndex)
        .catch(() => {})
        .finally(() => {
          this.activeLoads--;
          this.processQueue();
        });
    }
  }

  preloadImage(index) {
    if (this.images[index]) return Promise.resolve(this.images[index]);

    return new Promise((resolve, reject) => {
      const img = new Image();
      const src = typeof this.framePattern === 'function' 
        ? this.framePattern(index) 
        : this.framePattern.replace('%d', index);

      img.src = src;
      img.onload = () => {
        this.images[index] = img;
        this.loadedSet.add(index);
        
        // If this image is near currentFrame, redraw
        if (Math.abs(this.currentFrame - index) < 1.5) {
          this.drawFrame();
        }
        resolve(img);
      };
      img.onerror = () => {
        reject(new Error(`Failed to load frame ${index} from ${src}`));
      };
    });
  }

  handleScroll() {
    if (!this.container) {
      const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
      this.progress = maxScroll > 0 ? Math.min(1, Math.max(0, window.scrollY / maxScroll)) : 0;
    } else {
      const rect = this.container.getBoundingClientRect();
      const containerH = this.container.offsetHeight - window.innerHeight;
      if (containerH <= 0) return;
      const scrolled = -rect.top;
      this.progress = Math.min(1, Math.max(0, scrolled / containerH));
    }

    this.targetFrame = this.progress * (this.totalFrames - 1);

    if (this.onProgress) {
      this.onProgress(this.progress, this.targetFrame);
    }

    this.checkMilestones(this.progress);

    if (!this.isRendering) {
      this.isRendering = true;
      this.rafId = requestAnimationFrame(this.renderLoop);
    }
  }

  handleResize() {
    this.setupCanvasDPI();
    this.drawFrame();
  }

  checkMilestones(progress) {
    if (!this.onMilestone || this.milestones.length === 0) return;

    let activeIndex = -1;
    for (let i = this.milestones.length - 1; i >= 0; i--) {
      if (progress >= this.milestones[i].at) {
        activeIndex = i;
        break;
      }
    }

    if (activeIndex !== -1 && activeIndex !== this.lastMilestoneIndex) {
      this.lastMilestoneIndex = activeIndex;
      this.onMilestone(this.milestones[activeIndex], activeIndex);
    }
  }

  render() {
    const diff = this.targetFrame - this.currentFrame;

    // Emil Kowalski spring lerp physics
    if (Math.abs(diff) < 0.005) {
      this.currentFrame = this.targetFrame;
      this.drawFrame();
      this.isRendering = false; // Sleep RAF until next scroll event
      return;
    }

    this.currentFrame += diff * this.lerpFactor;
    this.drawFrame();
    this.rafId = requestAnimationFrame(this.renderLoop);
  }

  findNearestLoaded(index) {
    if (this.loadedSet.has(index)) return index;
    let delta = 1;
    while (delta < this.totalFrames) {
      if (index - delta >= 0 && this.loadedSet.has(index - delta)) return index - delta;
      if (index + delta < this.totalFrames && this.loadedSet.has(index + delta)) return index + delta;
      delta++;
    }
    return 0; // Fallback to frame 0
  }

  drawFrame() {
    const baseIndex = Math.floor(this.currentFrame);
    const nextIndex = Math.min(this.totalFrames - 1, baseIndex + 1);
    const blend = this.currentFrame - baseIndex;

    const baseLoaded = this.findNearestLoaded(baseIndex);
    const nextLoaded = this.findNearestLoaded(nextIndex);

    const baseImg = this.images[baseLoaded];
    const nextImg = this.images[nextLoaded];

    if (!baseImg) return;

    this.ctx.clearRect(0, 0, this.displayWidth, this.displayHeight);

    // Sub-frame optical crossfade
    if (this.opticalCrossfade && nextImg && baseLoaded !== nextLoaded && blend > 0.01) {
      this.ctx.globalAlpha = 1.0;
      this.drawImageFitted(baseImg);

      this.ctx.globalAlpha = blend;
      this.drawImageFitted(nextImg);
      this.ctx.globalAlpha = 1.0;
    } else {
      this.ctx.globalAlpha = 1.0;
      this.drawImageFitted(baseImg);
    }
  }

  drawImageFitted(img) {
    if (!img || !img.width || !img.height) return;

    const canvasW = this.displayWidth;
    const canvasH = this.displayHeight;
    const imgW = img.width;
    const imgH = img.height;

    let drawW, drawH, drawX, drawY;

    if (this.fitMode === 'cover') {
      const scale = Math.max(canvasW / imgW, canvasH / imgH);
      drawW = imgW * scale;
      drawH = imgH * scale;
      drawX = (canvasW - drawW) / 2;
      drawY = (canvasH - drawH) / 2;
    } else if (this.fitMode === 'contain') {
      const scale = Math.min(canvasW / imgW, canvasH / imgH);
      drawW = imgW * scale;
      drawH = imgH * scale;
      drawX = (canvasW - drawW) / 2;
      drawY = (canvasH - drawH) / 2;
    } else {
      drawW = canvasW;
      drawH = canvasH;
      drawX = 0;
      drawY = 0;
    }

    this.ctx.drawImage(img, drawX, drawY, drawW, drawH);
  }

  destroy() {
    window.removeEventListener('scroll', this.onScroll);
    window.removeEventListener('resize', this.onResize);
    if (this.resizeObserver) this.resizeObserver.disconnect();
    if (this.rafId) cancelAnimationFrame(this.rafId);
  }
}
