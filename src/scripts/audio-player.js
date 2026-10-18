/**
 * AudioPlayer - STARRY Live House Cassette Deck & Guitar Amp
 * Controls real anime soundtrack playback, rotating tape reels, and audio visualizer.
 * Defaults to playing music immediately upon entering the web.
 */

export class AudioPlayer {
  constructor() {
    const existing = document.getElementById('bgmAudio');
    this.audio = existing || new Audio('./assets/audio/kessoku_band_theme.mp3');
    this.audio.loop = true;
    this.audio.preload = 'auto';
    this.audio.volume = 0.8;

    this.isPlaying = false;
    this.userPaused = false;

    this.navBtn = document.getElementById('navAudioToggle');
    this.deckBtn = document.getElementById('deckPlayBtn');
    this.eqBars = document.querySelectorAll('.audio-bar');
    this.spools = document.querySelectorAll('.spool');

    this.init();
  }

  init() {
    // 1. Explicit button click listeners
    if (this.navBtn) {
      this.navBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        this.toggle();
      });
    }
    if (this.deckBtn) {
      this.deckBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        this.toggle();
      });
    }

    // 2. HTML5 Audio event listeners
    this.audio.addEventListener('play', () => {
      this.updateUI(true);
    });

    this.audio.addEventListener('playing', () => {
      this.updateUI(true);
    });

    this.audio.addEventListener('pause', () => {
      // Only show paused UI if user explicitly paused
      if (this.userPaused) {
        this.updateUI(false);
      }
    });

    this.audio.addEventListener('ended', () => {
      this.updateUI(false);
    });

    // 3. Default state is ON
    this.updateUI(true);

    // 4. Start unmuted autoplay immediately; fallback to muted autoplay + instant gesture unmute
    const startPlayback = () => {
      this.audio.muted = false;
      const playPromise = this.audio.play();
      if (playPromise !== undefined) {
        playPromise
          .then(() => {
            this.updateUI(true);
          })
          .catch(() => {
            // Unmuted autoplay blocked by browser policy -> start muted so it buffers and runs
            this.audio.muted = true;
            this.audio.play().then(() => {
              this.updateUI(true);
            }).catch(() => {});
          });
      }
    };

    startPlayback();

    // 5. Unmute on very first user interaction if muted or paused
    const unlockAndUnmute = () => {
      if (this.userPaused) return;
      this.audio.muted = false;
      if (this.audio.paused) {
        this.play().then(() => {
          this.updateUI(true);
          cleanup();
        }).catch(() => {});
      } else {
        this.updateUI(true);
        cleanup();
      }
    };

    const cleanup = () => {
      ['pointerdown', 'mousedown', 'touchstart', 'click', 'keydown', 'wheel', 'scroll'].forEach((ev) => {
        window.removeEventListener(ev, unlockAndUnmute, true);
        document.removeEventListener(ev, unlockAndUnmute, true);
      });
    };

    ['pointerdown', 'mousedown', 'touchstart', 'click', 'keydown', 'wheel', 'scroll'].forEach((ev) => {
      window.addEventListener(ev, unlockAndUnmute, { capture: true, passive: true });
      document.addEventListener(ev, unlockAndUnmute, { capture: true, passive: true });
    });

    // Expose on window for debugging or external triggers
    window.starryAudioPlayer = this;
  }

  play() {
    return this.audio.play();
  }

  pause() {
    this.audio.pause();
  }

  toggle() {
    if (this.isPlaying && !this.audio.paused) {
      this.userPaused = true;
      this.pause();
      this.updateUI(false);
    } else {
      this.userPaused = false;
      this.audio.muted = false;
      this.play().then(() => {
        this.updateUI(true);
      }).catch((err) => {
        console.warn('Audio playback blocked:', err);
      });
    }
  }

  updateUI(playing) {
    this.isPlaying = playing;

    if (this.navBtn) {
      this.navBtn.classList.toggle('is-playing', playing);
      const label = this.navBtn.querySelector('.audio-label');
      if (label) {
        label.textContent = playing ? 'STARRY: ON' : 'STARRY: LIVE';
      }
    }

    if (this.deckBtn) {
      const deckText = this.deckBtn.querySelector('.deck-btn-text');
      if (deckText) {
        deckText.textContent = playing ? 'PAUSE TAPE' : 'PLAY SOLO RIFF';
      }
    }

    this.eqBars.forEach((bar) => {
      bar.classList.toggle('playing', playing);
    });

    this.spools.forEach((spool) => {
      spool.classList.toggle('spool-spinning', playing);
    });
  }
}
