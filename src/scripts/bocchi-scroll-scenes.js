/**
 * BocchiScrollScenes - Living Curatorial Dossiers, Character Props & Accessories, Stage Gallery & Quirks
 */

const MEMBERS_DATA = {
  hitori: {
    name: 'Hitori Gotoh',
    kanji: '後藤 ひとり',
    role: 'Lead Guitar // "guitarhero"',
    color: '#ff7597',
    glow: 'rgba(255, 117, 151, 0.45)',
    render: './assets/characters/hitori_main.png',
    liveStill: './assets/gallery/still_ep05_4.jpg',
    liveTag: 'EP.05 // AUDITION GUITAR SOLO',
    statusBadge: { icon: '⚡', label: 'SOCIAL BATTERY', value: '3% · CRITICAL', color: '#ff7597' },
    quote: '"Even if I\'m an extreme introvert who hides in a cardboard box... when I hold this guitar, I can connect with the whole world."',
    instrument: 'Gibson Les Paul Custom 1968 / Yamaha PACIFICA 611V FM',
    archetype: 'The Bedroom Virtuoso',
    birthday: 'February 21 · Blood Type O',
    catchcopy: 'Conversations always start with "Ah..."',
    props: [
      {
        id: 'rat',
        name: 'ProCo RAT Distortion',
        desc: 'Bocchi\'s primary overdrive pedal for roaring distortion',
        svg: './assets/props/rat_pedal.svg',
        className: 'prop-top-left',
        delay: '0ms'
      },
      {
        id: 'mango',
        name: 'Ripe Mango Box ("完熟マンゴー")',
        desc: 'Cardboard armor against the harsh outside world',
        svg: './assets/quirks/mango_box.svg',
        className: 'prop-bottom-left',
        delay: '150ms'
      }
    ]
  },
  nijika: {
    name: 'Nijika Ijichi',
    kanji: '伊地知 虹夏',
    role: 'Drums // Band Leader & Founder',
    color: '#ffd13b',
    glow: 'rgba(255, 209, 59, 0.45)',
    render: './assets/characters/nijika_main.png',
    liveStill: './assets/gallery/still_ep08_4.jpg',
    liveTag: 'EP.08 // STARRY DRUMS IN SPOTLIGHT',
    statusBadge: { icon: '☀', label: 'STARRY MORALE', value: '100% · GUARDIAN', color: '#ffd13b' },
    quote: '"Kessoku Band won\'t stop here. We\'re going to become famous, perform at the biggest venues, and make everyone smile!"',
    instrument: 'Tama Imperialstar 5-Piece Drum Kit · Zildjian Cymbals',
    archetype: 'The Dorito Guardian Angel',
    birthday: 'May 29 · Blood Type A',
    catchcopy: 'The radiant heart holding the band together',
    props: [
      {
        id: 'dorito',
        name: 'Dorito Ahoge Ribbon',
        desc: 'Nijika\'s buoyant, gravity-defying yellow ahoge',
        svg: './assets/props/dorito_ahoge.svg',
        className: 'prop-top-right',
        delay: '0ms'
      },
      {
        id: 'sticks',
        name: 'Crossed TAMA Drumsticks',
        desc: 'Oak 5A drumsticks driving Kessoku Band\'s rhythm',
        svg: './assets/props/drumsticks.svg',
        className: 'prop-top-left',
        delay: '100ms'
      }
    ]
  },
  ryo: {
    name: 'Ryo Yamada',
    kanji: '山田 リョウ',
    role: 'Bass // Composer & Sound Architect',
    color: '#4383ff',
    glow: 'rgba(67, 131, 255, 0.45)',
    render: './assets/characters/ryo_main.png',
    liveStill: './assets/gallery/still_ep04_4.jpg',
    liveTag: 'EP.04 // BASSIST REVERIE',
    statusBadge: { icon: '🌿', label: 'WEED DIET', value: 'ACTIVE · WALLET: ¥0', color: '#4383ff' },
    quote: '"Abandon your individuality, and you\'re no better than dead. Playing rock means expressing what\'s truly inside you."',
    instrument: 'Fender Precision Bass 1960s Olympic White',
    archetype: 'The Cool-Headed Weed Eater',
    birthday: 'September 18 · Blood Type AB',
    catchcopy: 'Spends all her money on vintage vintage pedals',
    props: [
      {
        id: 'weeds',
        name: 'Wild Edible Weeds',
        desc: 'Zero-yen gourmet nutrition when bank account is empty',
        svg: './assets/props/weeds_grass.svg',
        className: 'prop-top-right',
        delay: '0ms'
      },
      {
        id: 'debt',
        name: 'Bocchi I.O.U. Note',
        desc: '"Bocchi-chan, lend me 1000 yen... bought vintage bass pedal"',
        svg: './assets/props/debt_note.svg',
        className: 'prop-bottom-left',
        delay: '120ms'
      }
    ]
  },
  ikuyo: {
    name: 'Ikuyo Kita',
    kanji: '喜多 郁代',
    role: 'Guitar & Lead Vocals // Moodmaker',
    color: '#ff4d4d',
    glow: 'rgba(255, 77, 77, 0.45)',
    render: './assets/characters/ikuyo_main.png',
    liveStill: './assets/gallery/still_ep08_1.jpg',
    liveTag: 'EP.08 // VOCALS & GUITAR CHORUS',
    statusBadge: { icon: '✨', label: 'KITA-AURA', value: '9999% · BLINDING', color: '#ff4d4d' },
    quote: '"I want to be by Gotoh-san\'s side, shining bright enough so that she never has to hide in the dark again!"',
    instrument: 'Gibson Les Paul Junior Special DC (Pelham Blue finish)',
    archetype: 'The Kitaura Radiant Sun',
    birthday: 'April 21 · Blood Type A',
    catchcopy: 'Spreads blinding positive energy everywhere',
    props: [
      {
        id: 'sparkles',
        name: 'Kita-Aura Sparkles',
        desc: 'Blinding positive energy radiating from the ultimate extrovert',
        svg: './assets/props/kita_sparkles.svg',
        className: 'prop-top-right',
        delay: '0ms'
      },
      {
        id: 'phone',
        name: 'Live Stream Smartphone',
        desc: 'Taking selfies & sharing Kessoku Band moments on Isstagram',
        svg: './assets/props/selfie_phone.svg',
        className: 'prop-top-left',
        delay: '100ms'
      }
    ]
  }
};

export function initLivingDossier() {
  // 1. Dossier Member Tabs
  const tabs = document.querySelectorAll('.member-tab-btn');
  const card = document.getElementById('dossierCard');
  const renderImg = document.getElementById('dossierCharRender');
  const propsLayer = document.getElementById('dossierPropsLayer');
  const liveStillImg = document.getElementById('dossierLiveStill');
  const liveTagEl = document.getElementById('dossierLiveTag');
  const roleEl = document.getElementById('dossierRole');
  const nameEl = document.getElementById('dossierName');
  const quoteEl = document.getElementById('dossierQuote');
  const instEl = document.getElementById('dossierInstrument');
  const archEl = document.getElementById('dossierArchetype');
  const bdayEl = document.getElementById('dossierBirthday');
  const catchEl = document.getElementById('dossierCatchcopy');
  const statusBadge = document.getElementById('dossierStatusBadge');

  function renderProps(memberKey) {
    if (!propsLayer) return;
    const member = MEMBERS_DATA[memberKey];
    if (!member || !member.props) return;

    propsLayer.innerHTML = '';
    member.props.forEach((p) => {
      const wrap = document.createElement('div');
      wrap.className = `dossier-prop-card ${p.className}`;
      wrap.style.animationDelay = p.delay;
      wrap.setAttribute('title', `${p.name}: ${p.desc}`);
      wrap.innerHTML = `
        <div class="prop-inner">
          <img src="${p.svg}" alt="${p.name}" class="prop-svg-img" />
          <span class="prop-tooltip">${p.name}</span>
        </div>
      `;
      propsLayer.appendChild(wrap);
    });
  }

  // Initial props render for default member (hitori)
  renderProps('hitori');

  if (tabs.length && card) {
    tabs.forEach((tab) => {
      tab.addEventListener('click', () => {
        const memberKey = tab.dataset.member;
        const data = MEMBERS_DATA[memberKey];
        if (!data) return;

        // Update active tab state
        tabs.forEach((t) => t.classList.remove('active'));
        tab.classList.add('active');

        // Update CSS variables on card
        card.style.setProperty('--active-color', data.color);
        card.style.setProperty('--active-glow', data.glow);

        // Animate render and props out
        if (renderImg) {
          renderImg.style.opacity = '0';
          renderImg.style.transform = 'scale(0.95) translateY(10px)';
        }
        if (propsLayer) {
          propsLayer.style.opacity = '0';
          propsLayer.style.transform = 'scale(0.9)';
        }
        if (liveStillImg) {
          liveStillImg.style.opacity = '0';
          liveStillImg.style.transform = 'scale(0.95) rotate(-3deg)';
        }

        setTimeout(() => {
          if (renderImg) renderImg.src = data.render;
          if (liveStillImg) liveStillImg.src = data.liveStill;
          if (liveTagEl) liveTagEl.textContent = data.liveTag;
          if (roleEl) roleEl.textContent = data.role;
          if (nameEl) nameEl.textContent = data.name;
          if (quoteEl) quoteEl.textContent = data.quote;
          if (instEl) instEl.textContent = data.instrument;
          if (archEl) archEl.textContent = data.archetype;
          if (bdayEl) bdayEl.textContent = data.birthday;
          if (catchEl) catchEl.textContent = data.catchcopy;

          if (statusBadge && data.statusBadge) {
            statusBadge.style.borderColor = data.color;
            statusBadge.style.color = data.color;
            statusBadge.innerHTML = `
              <span class="status-icon">${data.statusBadge.icon}</span>
              <span class="status-label">${data.statusBadge.label}:</span>
              <span class="status-val">${data.statusBadge.value}</span>
            `;
          }

          renderProps(memberKey);

          if (renderImg) {
            renderImg.style.opacity = '1';
            renderImg.style.transform = 'scale(1) translateY(0)';
          }
          if (propsLayer) {
            propsLayer.style.opacity = '1';
            propsLayer.style.transform = 'scale(1)';
          }
          if (liveStillImg) {
            liveStillImg.style.opacity = '1';
            liveStillImg.style.transform = 'scale(1) rotate(-1.5deg)';
          }
        }, 120);
      });
    });
  }

  // 2. Quirks interactions: Click glitch card to trigger panic jitter
  const glitchCard = document.getElementById('glitchCard');
  if (glitchCard) {
    glitchCard.addEventListener('click', () => {
      glitchCard.classList.add('glitch-active');
      setTimeout(() => {
        glitchCard.classList.remove('glitch-active');
      }, 1200);
    });
  }

  // 3. Stage Gallery Filter & Lightbox
  initGalleryArchive();
}

function initGalleryArchive() {
  const filterBtns = document.querySelectorAll('.gallery-filter-btn');
  const cards = document.querySelectorAll('.gallery-card');
  const lightbox = document.getElementById('galleryLightbox');
  const lightboxImg = document.getElementById('lightboxImg');
  const lightboxTitle = document.getElementById('lightboxTitle');
  const lightboxBadge = document.getElementById('lightboxBadge');
  const lightboxDesc = document.getElementById('lightboxDesc');
  const lightboxClose = document.getElementById('lightboxClose');

  // Progressive background prefetching of all gallery WebP images during browser idle time
  const galleryWebpList = [
    './assets/2k/kessoku_art_7k.webp',
    './assets/2k/kessoku_band_6k.webp',
    './assets/2k/bocchi_poster_5k.webp',
    './assets/2k/kessoku_squad_4k.webp',
    './assets/2k/bocchi_stage_solo_4k.webp',
    './assets/2k/bocchi_guitar_solo_2k.webp',
    './assets/2k/bocchi_shred_guitar_2k.webp',
    './assets/2k/bocchi_overdrive_4k.webp'
  ];

  const prefetchGalleryPool = () => {
    galleryWebpList.forEach((src) => {
      const img = new Image();
      img.decoding = 'async';
      img.src = src;
    });
  };

  if ('requestIdleCallback' in window) {
    requestIdleCallback(prefetchGalleryPool, { timeout: 2000 });
  } else {
    setTimeout(prefetchGalleryPool, 800);
  }

  if (filterBtns.length && cards.length) {
    filterBtns.forEach((btn) => {
      btn.addEventListener('click', () => {
        filterBtns.forEach((b) => b.classList.remove('active'));
        btn.classList.add('active');

        const filter = btn.dataset.filter;
        cards.forEach((card) => {
          const category = card.dataset.category || 'all';
          if (filter === 'all' || category === filter || category.includes(filter)) {
            card.style.display = 'block';
            setTimeout(() => {
              card.style.opacity = '1';
              card.style.transform = 'translateY(0)';
            }, 30);
          } else {
            card.style.opacity = '0';
            card.style.transform = 'translateY(15px)';
            setTimeout(() => {
              card.style.display = 'none';
            }, 250);
          }
        });
      });
    });
  }

  // Lightbox opening without breaking scroll/sticky
  cards.forEach((card) => {
    card.addEventListener('click', () => {
      if (!lightbox) return;
      const img = card.querySelector('.gallery-img');
      const title = card.querySelector('.gallery-card-title')?.textContent || '';
      const badge = card.querySelector('.gallery-res-tag')?.textContent || '';
      const desc = card.querySelector('.gallery-card-desc')?.textContent || '';
      const fullSrc = card.dataset.fullsrc || img?.src || '';

      if (lightboxImg) lightboxImg.src = fullSrc;
      if (lightboxTitle) lightboxTitle.textContent = title;
      if (lightboxBadge) lightboxBadge.textContent = badge;
      if (lightboxDesc) lightboxDesc.textContent = desc;

      lightbox.classList.add('is-open');
    });
  });

  const closeLightbox = () => {
    if (!lightbox) return;
    lightbox.classList.remove('is-open');
  };

  if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
  if (lightbox) {
    lightbox.addEventListener('click', (e) => {
      if (e.target === lightbox) closeLightbox();
    });
  }
  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeLightbox();
  });
}
