import { ScrollSequenceEngine } from './scroll-sequence-engine.js';
import { initBocchiClickEffect } from './bocchi-click-effect.js';
import { AudioPlayer } from './audio-player.js';
import { initLivingDossier } from './bocchi-scroll-scenes.js';
import { initGearAtelier } from './gear-atelier.js';

/**
 * Interactive Chromatic Mouse Aura Spotlight
 * Emil Kowalski spring lerp physics (lambda = 0.12)
 */
function initCursorAura() {
  const aura = document.getElementById('cursorAura');
  if (!aura) return;

  let mouseX = window.innerWidth / 2;
  let mouseY = window.innerHeight / 2;
  let currentX = mouseX;
  let currentY = mouseY;
  let isMoving = false;

  window.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    if (!isMoving) {
      isMoving = true;
      requestAnimationFrame(updateAura);
    }
  }, { passive: true });

  function updateAura() {
    const dx = mouseX - currentX;
    const dy = mouseY - currentY;

    currentX += dx * 0.14;
    currentY += dy * 0.14;

    const angle = (currentX / window.innerWidth) * 50 - 25;
    aura.style.transform = `translate3d(${currentX}px, ${currentY}px, 0) translate(-50%, -50%) rotate(${angle}deg)`;

    if (Math.abs(dx) > 0.1 || Math.abs(dy) > 0.1) {
      requestAnimationFrame(updateAura);
    } else {
      isMoving = false;
    }
  }

  // Initial center position
  aura.style.transform = `translate3d(${currentX}px, ${currentY}px, 0) translate(-50%, -50%)`;
}

document.addEventListener('DOMContentLoaded', () => {
  // 1. Initialize Realtime Cute Bocchi Click Particles
  initBocchiClickEffect();

  // 2. Initialize Interactive Background Chromatic Cursor Aura
  initCursorAura();

  // 3. Initialize STARRY Cassette Deck & Audio Player
  const audioPlayer = new AudioPlayer();

  // 4. Initialize Living Curatorial Dossiers & Quirks
  initLivingDossier();

  // 5. Initialize Starry Gear Atelier Interactive Controller
  initGearAtelier();

  // 6. Initialize 120 FPS Manga-Rock Kinetic Canvas Sequence Engine
  const sfx1 = document.getElementById('sfx1');
  const sfx2 = document.getElementById('sfx2');
  const sfx3 = document.getElementById('sfx3');
  const sfx4 = document.getElementById('sfx4');
  const overdriveFill = document.getElementById('overdriveFill');
  const overdriveVal = document.getElementById('overdriveVal');

  const engine = new ScrollSequenceEngine({
    canvas: '#sequenceCanvas',
    container: '#scrubSequence',
    totalFrames: 80,
    fitMode: 'cover',
    framePattern: (i) => `./assets/sequence/frame_${String(i).padStart(3, '0')}.webp`,
    keyframeStride: 4,
    lerpFactor: 0.18,
    opticalCrossfade: true,
    onProgress: (progress) => {
      // Manga SFX Dynamic Triggers based on solo intensity
      if (sfx1) sfx1.classList.toggle('active', progress >= 0.10 && progress < 0.38);
      if (sfx2) sfx2.classList.toggle('active', progress >= 0.35 && progress < 0.62);
      if (sfx3) sfx3.classList.toggle('active', progress >= 0.58 && progress < 0.85);
      if (sfx4) sfx4.classList.toggle('active', progress >= 0.80);

      // Overdrive meter
      const pct = Math.round(progress * 100);
      if (overdriveFill) overdriveFill.style.width = `${pct}%`;
      if (overdriveVal) {
        if (pct < 30) overdriveVal.textContent = `${pct}% CRUNCH`;
        else if (pct < 75) overdriveVal.textContent = `${pct}% DISTORTION`;
        else overdriveVal.textContent = `${pct}% GUITAR HERO MAXIMUM! ⚡`;
      }
    }
  });

  // Hero scroll cue trigger
  const heroCue = document.querySelector('.hero-scroll-cue');
  if (heroCue) {
    heroCue.addEventListener('click', (e) => {
      e.preventDefault();
      const scrubSection = document.getElementById('scrubSequence');
      if (scrubSection) {
        scrubSection.scrollIntoView({ behavior: 'smooth' });
      }
    });
  }
});

