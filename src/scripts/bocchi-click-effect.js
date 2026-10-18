/**
 * BocchiClickEffect - Realtime Cute Bocchi Icon Click Particle Engine
 * Spawns charming mini chibi Bocchi faces, guitar picks, and stars on pointerdown.
 */

const CHIBI_ICONS = [
  './assets/chibi/bocchi_shy.svg',
  './assets/chibi/bocchi_panic.svg',
  './assets/chibi/bocchi_slime.svg',
  './assets/chibi/guitar_pick.svg'
];

let audioCtx = null;

function playCutePluckSound() {
  try {
    if (!audioCtx) {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      if (AudioContext) audioCtx = new AudioContext();
    }
    if (!audioCtx || audioCtx.state === 'suspended') return;

    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();

    // High, cute guitar harmonic / pluck pitch
    const pitches = [523.25, 659.25, 783.99, 1046.50]; // C5, E5, G5, C6
    const freq = pitches[Math.floor(Math.random() * pitches.length)];

    osc.type = 'triangle';
    osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(freq * 1.5, audioCtx.currentTime + 0.08);

    gain.gain.setValueAtTime(0.08, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.18);

    osc.connect(gain);
    gain.connect(audioCtx.destination);

    osc.start();
    osc.stop(audioCtx.currentTime + 0.18);
  } catch (e) {
    // Silent fail if audio is blocked
  }
}

export function initBocchiClickEffect() {
  document.addEventListener('pointerdown', (e) => {
    // Avoid triggering on links or buttons if needed, or trigger lightly everywhere
    const count = 1 + Math.floor(Math.random() * 2); // 1-2 particles

    for (let i = 0; i < count; i++) {
      createParticle(e.clientX, e.clientY, i);
    }

    playCutePluckSound();
  }, { passive: true });
}

function createParticle(x, y, index) {
  const particle = document.createElement('div');
  particle.className = 'bocchi-particle';

  const iconSrc = CHIBI_ICONS[Math.floor(Math.random() * CHIBI_ICONS.length)];
  const size = 36 + Math.floor(Math.random() * 16); // 36px to 52px

  const img = document.createElement('img');
  img.src = iconSrc;
  img.style.width = `${size}px`;
  img.style.height = `${size}px`;
  img.style.filter = 'drop-shadow(0 4px 10px rgba(255, 117, 151, 0.45))';

  particle.appendChild(img);

  // Random trajectory
  const dx = (Math.random() - 0.5) * 110 + (index * 20);
  const dy = -40 - Math.random() * 50;
  const rotStart = (Math.random() - 0.5) * 30;
  const rotMid = (Math.random() - 0.5) * 45;
  const rotEnd = (Math.random() - 0.5) * 60;

  particle.style.left = `${x}px`;
  particle.style.top = `${y}px`;
  particle.style.setProperty('--dx', `${dx}px`);
  particle.style.setProperty('--dy', `${dy}px`);
  particle.style.setProperty('--rot-start', `${rotStart}deg`);
  particle.style.setProperty('--rot-mid', `${rotMid}deg`);
  particle.style.setProperty('--rot-end', `${rotEnd}deg`);

  document.body.appendChild(particle);

  // Self-cleaning
  setTimeout(() => {
    if (particle && particle.parentNode) {
      particle.parentNode.removeChild(particle);
    }
  }, 700);
}
