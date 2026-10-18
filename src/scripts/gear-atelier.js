/**
 * Bocchi The Rock - Starry Gear Atelier Interactive Controller
 * Handles interactive guitar hotspots, cute charms, speech bubble confessions, and Web Audio tones.
 */

export function initGearAtelier() {
  const quoteEl = document.getElementById('gearConfessionQuote');
  const transEl = document.getElementById('gearConfessionTrans');
  const avatarKaomojiEl = document.getElementById('gearAvatarKaomoji');
  const guitarImg = document.getElementById('gearGuitarImg');
  const specTitle = document.getElementById('specTitle');
  const specDesc = document.getElementById('specDesc');
  const specTag = document.getElementById('specTag');
  const specBadge = document.getElementById('specBadge');

  const chips = document.querySelectorAll('.accessory-chip');
  const hotspots = document.querySelectorAll('.gear-hotspot');

  // Interactive Gear Data with authentic Bocchi voice lines
  const gearData = {
    father: {
      kaomoji: '(⁄ ⁄＞⁄ ▽ ⁄＜⁄ ⁄)',
      quote: '「お父さんのギブソン・レスポール・カスタム... 傷つけないように毎日クロスで磨いてます...」',
      trans: '"My father\'s Gibson Les Paul Custom 1968... I polish it with microfiber every day so it never gets scratched..."',
      tag: 'PRIMARY WEAPON · INHERITED',
      badge: '1968 REISSUE',
      title: 'GIBSON LES PAUL CUSTOM ("BLACK BEAUTY")',
      desc: 'Inherited from her father\'s youth. Carved maple top on mahogany back with gold hardware, dual humbuckers, and ebony fretboard with mother-of-pearl split-diamond inlay. Heavy, thunderous sustain that powers Kessoku Band\'s solos.',
      soundType: 'custom'
    },
    cubes: {
      kaomoji: '( ｡• ᵕ •｡ )',
      quote: '「ペグのところにヘアゴムのキューブをこっそり付けてます... お守りみたいなものです...！」',
      trans: '"I secretly tied my hair cubes to the tuner peg... it\'s kind of like my lucky charm...!"',
      tag: 'CUTE ACCESSORY · HEADSTOCK',
      badge: 'LUCKY CHARM',
      title: 'YELLOW & CYAN HAIR CUBE CHARM',
      desc: 'Iconic yellow and cyan geometric hair ties fastened securely to the Grover tuning pegs. Adds zero decibels of sustain but 100% emotional stability during live stage panic.',
      soundType: 'chime'
    },
    pick: {
      kaomoji: '( > ﹏ < )',
      quote: '「ピックガードに予備のピンクのピックを挟んでます... ギターヒーローの魂です...！」',
      trans: '"I wedge an extra pink pick under the pickguard... it holds the soul of guitarhero...!"',
      tag: 'SOLO CATALYST · PICKGUARD',
      badge: 'CELLULOID 1.0MM',
      title: 'GUITARHERO PINK CELLULOID PICK',
      desc: 'Custom pink triangular pick marked with ( > ﹏ < ) blushing kaomoji. Tucked under the 5-ply pickguard for emergency high-speed tapping and arpeggios.',
      soundType: 'pick'
    },
    mango: {
      kaomoji: '( ；∀；)',
      quote: '「段ボール箱の完熟マンゴーシール... これが私の精神的防壁なんです...！」',
      trans: '"The Ripe Mango box sticker... this is my absolute emotional defense barrier...!"',
      tag: 'DEFENSE MATRIX · LOWER BOUT',
      badge: 'MIYAZAKI SEAL',
      title: '完熟マンゴー (RIPE MANGO) BOX ARMOR DECAL',
      desc: 'A commemorative sticker peeled from her childhood cardboard box sanctuary. Shields the lead guitarist against direct audience eye contact and social vulnerability.',
      soundType: 'pop'
    },
    amp: {
      kaomoji: '( ಠ_ಠ )ง',
      quote: '「RATの歪みペダルとJCM900を踏み込んだ時だけ... 人前でも大きな音を出せます...！」',
      trans: '"Only when I stomp on the ProCo RAT distortion and Marshall JCM900... can I make a loud sound in front of people...!"',
      tag: 'UNDERGROUND RIG · HIGH GAIN',
      badge: 'DUAL REVERB',
      title: 'MARSHALL JCM900 + PROCO RAT 2 OVERDRIVE',
      desc: 'The screaming sonic powerhouse of Shimokitazawa STARRY. High-gain tube saturation pushed into screaming harmonics by vintage silicon clipping diodes.',
      soundType: 'chord'
    }
  };

  // Web Audio Synthesizer for tactile feedback
  let audioCtx = null;
  function playGearSound(type) {
    try {
      if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      }
      if (audioCtx.state === 'suspended') {
        audioCtx.resume();
      }

      const now = audioCtx.currentTime;

      if (type === 'chime') {
        // High sparkling bell chime
        const freqs = [1046.5, 1318.5, 1567.98, 2093]; // C6, E6, G6, C7
        freqs.forEach((freq, idx) => {
          const osc = audioCtx.createOscillator();
          const gain = audioCtx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(freq, now + idx * 0.05);

          gain.gain.setValueAtTime(0.08, now + idx * 0.05);
          gain.gain.exponentialRampToValueAtTime(0.0001, now + idx * 0.05 + 0.6);

          osc.connect(gain);
          gain.connect(audioCtx.destination);

          osc.start(now + idx * 0.05);
          osc.stop(now + idx * 0.05 + 0.65);
        });
      } else if (type === 'pick') {
        // Bright guitar acoustic harmonic pluck
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(659.25, now); // E5
        osc.frequency.exponentialRampToValueAtTime(1318.5, now + 0.08);

        gain.gain.setValueAtTime(0.12, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.4);

        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start(now);
        osc.stop(now + 0.45);
      } else if (type === 'pop') {
        // Cute bubble pop sound
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(440, now);
        osc.frequency.exponentialRampToValueAtTime(880, now + 0.08);

        gain.gain.setValueAtTime(0.15, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.12);

        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start(now);
        osc.stop(now + 0.15);
      } else if (type === 'chord' || type === 'custom') {
        // Rich rock guitar power chord
        const freqs = [164.81, 246.94, 329.63, 493.88]; // E3, B3, E4, B4
        freqs.forEach((freq) => {
          const osc = audioCtx.createOscillator();
          const gain = audioCtx.createGain();
          osc.type = 'sawtooth';
          osc.frequency.setValueAtTime(freq, now);

          gain.gain.setValueAtTime(0.04, now);
          gain.gain.exponentialRampToValueAtTime(0.0005, now + 0.7);

          osc.connect(gain);
          gain.connect(audioCtx.destination);
          osc.start(now);
          osc.stop(now + 0.75);
        });
      }
    } catch {
      // Audio context might be restricted before interaction
    }
  }

  function selectAccessory(key, triggerElement) {
    const data = gearData[key];
    if (!data) return;

    // Update quote & translations with smooth fade
    if (quoteEl && transEl) {
      quoteEl.style.opacity = '0';
      transEl.style.opacity = '0';
      setTimeout(() => {
        quoteEl.textContent = data.quote;
        transEl.textContent = data.trans;
        quoteEl.style.opacity = '1';
        transEl.style.opacity = '1';
      }, 150);
    }

    if (avatarKaomojiEl) {
      avatarKaomojiEl.textContent = data.kaomoji;
    }

    // Update specs card
    if (specTitle) specTitle.textContent = data.title;
    if (specDesc) specDesc.textContent = data.desc;
    if (specTag) specTag.textContent = data.tag;
    if (specBadge) specBadge.textContent = data.badge;

    // Update active chip
    chips.forEach(chip => {
      chip.classList.toggle('active', chip.dataset.accessory === key);
    });

    // Animate guitar
    if (guitarImg) {
      guitarImg.style.transform = 'scale(1.04) rotate(-1deg)';
      setTimeout(() => {
        guitarImg.style.transform = '';
      }, 350);
    }

    // Play feedback sound
    playGearSound(data.soundType);

    // Spawn floating cute confetti/note from click point
    if (triggerElement) {
      const rect = triggerElement.getBoundingClientRect();
      spawnCharmSparkle(rect.left + rect.width / 2, rect.top + rect.height / 2, data.kaomoji);
    }
  }

  // Floating sparkle burst
  function spawnCharmSparkle(x, y, text) {
    const sparkle = document.createElement('div');
    sparkle.className = 'gear-floating-sparkle';
    sparkle.textContent = text || '✨';
    sparkle.style.left = `${x}px`;
    sparkle.style.top = `${y}px`;
    document.body.appendChild(sparkle);

    setTimeout(() => {
      sparkle.remove();
    }, 1200);
  }

  // Wire up accessory chips
  chips.forEach(chip => {
    chip.addEventListener('click', (e) => {
      const key = chip.dataset.accessory;
      selectAccessory(key, chip);
    });
  });

  // Wire up guitar hotspots
  hotspots.forEach(hotspot => {
    hotspot.addEventListener('click', (e) => {
      e.stopPropagation();
      const target = hotspot.dataset.target;
      selectAccessory(target, hotspot);
    });
  });
}
