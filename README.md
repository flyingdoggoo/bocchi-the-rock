# 🎸 BOCCHI THE ROCK! // KESSOKU BAND
### Cinematic Haute Editorial & 120 FPS Interactive Overdrive Experience

[![Live Demo](https://img.shields.io/badge/Production%20Live-bocchi.oguri--lab.io.vn-ff7597?style=for-the-badge&logo=google-chrome&logoColor=white)](https://bocchi.oguri-lab.io.vn/)
[![Vite](https://img.shields.io/badge/Vite-5.4-646CFF?style=for-the-badge&logo=vite&logoColor=white)](https://vitejs.dev/)
[![AWS CloudFront](https://img.shields.io/badge/AWS-CloudFront%20CDN-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/cloudfront/)
[![Web Audio API](https://img.shields.io/badge/Web%20Audio-Interactive%20Synth-ffd13b?style=for-the-badge&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API)
[![Framerate](https://img.shields.io/badge/Performance-120%20FPS%20Canvas-4383ff?style=for-the-badge)](https://bocchi.oguri-lab.io.vn/)

> **「暗闇のクローゼットから、下北沢STARRYの熱狂へ。」**  
> *(From the darkness of the bedroom closet to the explosive ecstasy of Shimokitazawa STARRY.)*

---

## 🌐 Production Live Deployment

The website is actively deployed and delivered globally via AWS CloudFront CDN:

🔗 **[https://bocchi.oguri-lab.io.vn/](https://bocchi.oguri-lab.io.vn/)**

- **Origin**: AWS S3 Bucket (`bocchi.oguri-lab.io.vn`, `ap-southeast-1`) with Origin Access Control (OAC).
- **Edge CDN**: Amazon CloudFront distribution (`ELRSMTSWUVT0X`).
- **SSL / TLS**: AWS Certificate Manager 256-bit encryption.
- **DNS**: Amazon Route53 Hosted Zone (`oguri-lab.io.vn`).

---

## ⚡ Core Features & Interactive Engineering

### 1. 🎞️ 120 FPS Kinetic Manga Rock Overdrive Scroller
- **Keyframe-Interpolated Canvas Engine**: Smooth scrub scroller interpolating 80 frames of Bocchi's guitar shred solo with sub-frame dual-blend optical crossfade.
- **Dynamic Manga Sound FX (Onomatopoeia)**: Hand-lettered Japanese rock sound bursts (`ジャカジャカ！` $\rightarrow$ `ドドドドッ！` $\rightarrow$ `ギュイィィン！` $\rightarrow$ `バーーーーーン！`) triggered by scroll velocity and milestone progress.
- **Real-Time Overdrive VU Meter**: Live HUD reflecting gain stages from `0% CRUNCH` up to `GUITAR HERO MAXIMUM! ⚡`.

### 2. 🌈 Universal Chromatic Cursor Aura
- Radial gradient spotlight mesh (`#ff7597`, `#ffd13b`, `#4383ff`) following pointer movements across the entire page.
- Built with **Emil Kowalski spring lerp physics** ($\lambda = 0.14$) and dynamic rotational tilt responding to mouse trajectory.

### 3. 🎸 Interactive Starry Gear Atelier
- **Anatomically Accurate Vector Render**: Hitori Gotoh's 1968 Gibson Les Paul Custom ("Black Beauty") single-cutaway body, Florentine treble horn, carved maple archtop, split-diamond open-book headstock, and gold hardware.
- **Cute Closet Charms & Accessories**:
  - 💛💙 Yellow & Cyan Hair Cubes keychain charm dangling from tuner pegs.
  - 🎸 Pink celluloid `GUITARHERO` pick with kaomoji `( > ﹏ < )`.
  - 🥭 Miyazaki Ripe Mango ("完熟マンゴー") box decal.
- **Interactive Web Audio Sound Synthesis**: Clickable hotspots synthesizing guitar plucks, harmonic chimes, distortion boosts, and dynamic character confession dialogues.

### 4. 👥 Living Curatorial Dossiers (Zero UI Breakage)
- Balanced dossiers for all four Kessoku Band members (**Hitori Gotoh**, **Nijika Ijichi**, **Ryo Yamada**, **Ikuyo Kita**).
- Curated signature props (ProCo RAT 2 distortion pedal, crossed drumsticks, Dorito hair ribbon, grass weeds, Kita-aura sparkles).
- Mobile-first responsive touch slider tabs for touchscreens.

### 5. 🎵 Instant 0ms Autoplay Soundtrack & STARRY Live Mode
- Zero-delay background audio playback of Kessoku Band's official anime soundtrack.
- **Default State**: Header toggle displays `STARRY: ON` with 6-bar realtime equalizer animation and spinning cassette tape deck spools.
- Universal cross-browser compatibility: Seamless fallback for strict W3C autoplay policies with instant zero-buffer unmute upon first touch/scroll gesture.

### 6. 🚀 Ultra-Lightweight Retina WebP Visual Archive
- Entire 8-artwork gallery compressed from uncompressed 40+ MB raw JPEGs down to **1.47 MB** retina WebP (**-96.3% payload reduction**).
- Non-blocking asynchronous decoding (`decoding="async"`) and background idle prefetching (`requestIdleCallback`).

---

## 🛠️ Tech Stack & Architecture

- **Core**: Vanilla HTML5, Modern CSS (Custom Design Tokens, Clamp Typography, Backdrop Filters), Vanilla ES Modules.
- **Bundler**: [Vite 5](https://vitejs.dev/) (Sub-second HMR & production builds).
- **Sound**: Web Audio API & HTML5 Audio streaming.
- **Graphics**: HTML5 2D Canvas Engine & Custom Scalable Vector Graphics (SVG).
- **Hosting & Infrastructure**: AWS S3, CloudFront CDN, Route53, ACM SSL, AWS CLI.
- **Testing & Verification**: Playwright MCP automated headless browser testing.

---

## 📂 Project Structure

```
bocchi-the-rock/
├── index.html                     # Main semantic HTML structure
├── package.json                   # Dependencies & npm scripts
├── vite.config.js                 # Vite bundler configuration
├── .gitignore                     # Git exclusions (dist, cache, node_modules)
├── public/
│   ├── assets/
│   │   ├── 2k/                    # High-definition WebP gallery artworks
│   │   ├── audio/                 # Kessoku Band soundtrack MP3
│   │   ├── characters/            # High-res character cutouts
│   │   ├── common/                # SVG logos and vectors
│   │   ├── gallery/               # Episode animation stills
│   │   ├── gear/                  # Gibson Les Paul Custom 1968 vector
│   │   ├── props/                 # Character prop SVGs
│   │   ├── quirks/                # Chibi & mango box SVGs
│   │   └── sequence/              # 80-frame WebP guitar solo sequence
├── scripts/
│   └── deploy.mjs                 # One-click AWS S3 & CloudFront deploy script
└── src/
    ├── styles/
    │   ├── animations.css         # Keyframes & kinetic transitions
    │   ├── main.css               # Haute-editorial styling & layouts
    │   └── tokens.css             # Palette, fonts, and typography tokens
    └── scripts/
        ├── audio-player.js        # Cassette deck & STARRY audio controller
        ├── bocchi-click-effect.js # Click particle sparks
        ├── bocchi-scroll-scenes.js# Gallery prefetcher & dossier interactions
        ├── gear-atelier.js        # Guitar SVG hotspots & Web Audio synthesis
        ├── main.js                # Application entrypoint & cursor aura
        └── scroll-sequence-engine.js # 120 FPS canvas scroller engine
```

---

## 💻 Local Development

### Prerequisites
- [Node.js](https://nodejs.org/) (v18 or higher recommended)
- [npm](https://www.npmjs.com/)

### Setup & Run
```bash
# 1. Clone repository
git clone https://github.com/flyingdoggoo/bocchi-the-rock.git
cd bocchi-the-rock

# 2. Install dependencies
npm install

# 3. Start local development server
npm run dev
```

Open [http://localhost:5173](http://localhost:5173) in your browser to view the site with Hot Module Replacement (HMR).

---

## 🚀 Building & Production Deployment

### Build Bundle
```bash
npm run build
```
Generates production-ready, minified HTML, CSS, and JS bundles inside the `dist/` folder in under 800ms.

### One-Click AWS Deploy
```bash
npm run deploy
```
This automated script:
1. Builds the Vite production bundle.
2. Syncs static assets to S3 bucket `bocchi.oguri-lab.io.vn` with `max-age=31536000, immutable` caching.
3. Uploads `index.html` with `must-revalidate` zero-cache headers for instant updates.
4. Triggers CloudFront edge invalidation (`/*`) across worldwide PoPs in 10 seconds.

---

## 📜 License & Credits

- **Character & IP**: *Bocchi The Rock!* (ぼっち・ざ・ろっく!) © Aki Hamazi / Houbunsha, Aniplex.
- **Crafted with passion for Kessoku Band and the underground spirit of Live House STARRY.**
