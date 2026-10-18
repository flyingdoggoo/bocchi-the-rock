import os

os.makedirs('public/assets/gear', exist_ok=True)
os.makedirs('public/assets/common', exist_ok=True)

# 1. Gibson Les Paul Custom 1968 Reissue ("Black Beauty")
les_paul_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 700" width="300" height="700">
  <defs>
    <linearGradient id="bodyGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e1e24"/>
      <stop offset="60%" stop-color="#0a0a0d"/>
      <stop offset="100%" stop-color="#000000"/>
    </linearGradient>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffe082"/>
      <stop offset="50%" stop-color="#ffd54f"/>
      <stop offset="100%" stop-color="#ffb300"/>
    </linearGradient>
  </defs>
  
  <!-- Headstock -->
  <polygon points="120,40 180,40 175,130 125,130" fill="#0d0d10" stroke="url(#goldGrad)" stroke-width="2"/>
  <text x="150" y="70" font-family="'Times New Roman', serif" font-weight="bold" font-size="12" fill="url(#goldGrad)" text-anchor="middle">Gibson</text>
  <polygon points="150,85 145,95 155,95" fill="url(#goldGrad)"/>
  <polygon points="150,110 145,100 155,100" fill="url(#goldGrad)"/>
  <!-- Gold Tuning Pegs (3 per side) -->
  <circle cx="112" cy="60" r="5" fill="url(#goldGrad)"/>
  <circle cx="112" cy="85" r="5" fill="url(#goldGrad)"/>
  <circle cx="112" cy="110" r="5" fill="url(#goldGrad)"/>
  <circle cx="188" cy="60" r="5" fill="url(#goldGrad)"/>
  <circle cx="188" cy="85" r="5" fill="url(#goldGrad)"/>
  <circle cx="188" cy="110" r="5" fill="url(#goldGrad)"/>
  
  <!-- Fretboard / Neck (Rosewood / Ebony with mother-of-pearl block inlays) -->
  <rect x="138" y="130" width="24" height="230" fill="#1b1612" stroke="#4a3728" stroke-width="1"/>
  <!-- Block Inlays -->
  <rect x="144" y="150" width="12" height="6" fill="#f0ebd8"/>
  <rect x="144" y="180" width="12" height="6" fill="#f0ebd8"/>
  <rect x="144" y="210" width="12" height="6" fill="#f0ebd8"/>
  <rect x="144" y="240" width="12" height="6" fill="#f0ebd8"/>
  <rect x="144" y="270" width="12" height="6" fill="#f0ebd8"/>
  <rect x="144" y="300" width="12" height="6" fill="#f0ebd8"/>
  <rect x="144" y="330" width="12" height="6" fill="#f0ebd8"/>
  <!-- Frets (Silver lines) -->
  <g stroke="#9e9e9e" stroke-width="1">
    <line x1="138" y1="140" x2="162" y2="140"/>
    <line x1="138" y1="165" x2="162" y2="165"/>
    <line x1="138" y1="195" x2="162" y2="195"/>
    <line x1="138" y1="225" x2="162" y2="225"/>
    <line x1="138" y1="255" x2="162" y2="255"/>
    <line x1="138" y1="285" x2="162" y2="285"/>
    <line x1="138" y1="315" x2="162" y2="315"/>
    <line x1="138" y1="345" x2="162" y2="345"/>
  </g>

  <!-- Les Paul Body (Carved Maple Top on Mahogany) -->
  <path d="M 135 360 
           C 95 360 60 390 60 440 
           C 60 480 85 510 80 540 
           C 70 590 100 650 150 650 
           C 200 650 230 590 220 540 
           C 215 510 240 480 240 440 
           C 240 395 205 360 165 360
           C 165 375 160 380 150 380
           C 140 380 135 375 135 360 Z"
        fill="url(#bodyGrad)" stroke="url(#goldGrad)" stroke-width="4"/>
        
  <!-- Pickguard (Black 5-ply with gold bracket) -->
  <path d="M 125 390 Q 95 440 105 490 L 135 480 Z" fill="#000000" stroke="#f5f5f5" stroke-width="1.5"/>

  <!-- Pickups: Gold-covered Humbuckers -->
  <!-- Neck Pickup -->
  <rect x="136" y="400" width="28" height="18" rx="2" fill="url(#goldGrad)" stroke="#1a1a24" stroke-width="1"/>
  <!-- Bridge Pickup -->
  <rect x="136" y="445" width="28" height="18" rx="2" fill="url(#goldGrad)" stroke="#1a1a24" stroke-width="1"/>
  
  <!-- Tune-o-matic Bridge & Stopbar Tailpiece (Gold) -->
  <rect x="138" y="480" width="24" height="6" rx="2" fill="url(#goldGrad)"/>
  <rect x="136" y="505" width="28" height="8" rx="3" fill="url(#goldGrad)"/>

  <!-- 4 Gold Top-Hat Control Knobs -->
  <circle cx="180" cy="520" r="7" fill="url(#goldGrad)" stroke="#222" stroke-width="1"/>
  <circle cx="195" cy="540" r="7" fill="url(#goldGrad)" stroke="#222" stroke-width="1"/>
  <circle cx="170" cy="550" r="7" fill="url(#goldGrad)" stroke="#222" stroke-width="1"/>
  <circle cx="185" cy="570" r="7" fill="url(#goldGrad)" stroke="#222" stroke-width="1"/>
  
  <!-- Pickup Selector Switch (Rhythm / Treble washer) -->
  <circle cx="105" cy="405" r="8" fill="#1b1612" stroke="url(#goldGrad)" stroke-width="1"/>
  <circle cx="105" cy="405" r="3" fill="#fff9c4"/>
  
  <!-- 6 Strings running full length -->
  <g stroke="#ffffff" opacity="0.6" stroke-width="1">
    <line x1="140" y1="40" x2="140" y2="510"/>
    <line x1="144" y1="40" x2="144" y2="510"/>
    <line x1="148" y1="40" x2="148" y2="510"/>
    <line x1="152" y1="40" x2="152" y2="510"/>
    <line x1="156" y1="40" x2="156" y2="510"/>
    <line x1="160" y1="40" x2="160" y2="510"/>
  </g>
</svg>"""

with open('public/assets/gear/gibson_les_paul.svg', 'w', encoding='utf-8') as f:
    f.write(les_paul_svg)

# 2. Cassette Tape Graphic
cassette_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 250" width="400" height="250">
  <defs>
    <linearGradient id="tapeBody" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#24232a"/>
      <stop offset="100%" stop-color="#141318"/>
    </linearGradient>
    <linearGradient id="labelGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff7597"/>
      <stop offset="25%" stop-color="#ffd13b"/>
      <stop offset="50%" stop-color="#4383ff"/>
      <stop offset="100%" stop-color="#ff4d4d"/>
    </linearGradient>
  </defs>
  <!-- Outer Shell -->
  <rect x="20" y="15" width="360" height="220" rx="14" fill="url(#tapeBody)" stroke="#3a3845" stroke-width="3"/>
  <!-- Corner Screws -->
  <circle cx="35" cy="30" r="4" fill="#666"/>
  <circle cx="365" cy="30" r="4" fill="#666"/>
  <circle cx="35" cy="220" r="4" fill="#666"/>
  <circle cx="365" cy="220" r="4" fill="#666"/>
  
  <!-- Paper Label -->
  <rect x="45" y="35" width="310" height="150" rx="8" fill="#f8f9fa"/>
  <!-- Color Band on Label -->
  <rect x="45" y="35" width="310" height="20" fill="url(#labelGrad)"/>
  
  <!-- Handwritten Cassette Title -->
  <text x="60" y="80" font-family="'Courier New', monospace" font-weight="bold" font-size="20" fill="#1b1b22">KESSOKU BAND // LIVE DEMO</text>
  <text x="60" y="100" font-family="'Courier New', monospace" font-size="12" fill="#555">SIDE A · THAT BAND (あのバンド) [GUITAR HERO SOLO]</text>
  
  <!-- Clear Window in center -->
  <rect x="90" y="115" width="220" height="60" rx="6" fill="#111016" stroke="#444" stroke-width="2"/>
  
  <!-- Two Rotating Tape Hubs / Spools -->
  <!-- Left Spool -->
  <g class="spool spool-left" id="spoolLeft" transform="translate(140, 145)">
    <circle cx="0" cy="0" r="22" fill="#333" stroke="#ffd13b" stroke-width="2"/>
    <circle cx="0" cy="0" r="9" fill="#111016"/>
    <!-- Teeth -->
    <rect x="-3" y="-22" width="6" height="8" fill="#ffd13b"/>
    <rect x="-3" y="14" width="6" height="8" fill="#ffd13b"/>
    <rect x="-22" y="-3" width="8" height="6" fill="#ffd13b"/>
    <rect x="14" y="-3" width="8" height="6" fill="#ffd13b"/>
  </g>
  
  <!-- Right Spool -->
  <g class="spool spool-right" id="spoolRight" transform="translate(260, 145)">
    <circle cx="0" cy="0" r="22" fill="#333" stroke="#ffd13b" stroke-width="2"/>
    <circle cx="0" cy="0" r="9" fill="#111016"/>
    <!-- Teeth -->
    <rect x="-3" y="-22" width="6" height="8" fill="#ffd13b"/>
    <rect x="-3" y="14" width="6" height="8" fill="#ffd13b"/>
    <rect x="-22" y="-3" width="8" height="6" fill="#ffd13b"/>
    <rect x="14" y="-3" width="8" height="6" fill="#ffd13b"/>
  </g>
  
  <!-- Tape Magnetic Ribbon view -->
  <line x1="162" y1="145" x2="238" y2="145" stroke="#4a3b32" stroke-width="12"/>
  
  <!-- Bottom Trapezoid indent -->
  <polygon points="100,235 300,235 280,195 120,195" fill="#19181f" stroke="#333" stroke-width="2"/>
</svg>"""

with open('public/assets/common/cassette_tape.svg', 'w', encoding='utf-8') as f:
    f.write(cassette_svg)

print("Gear and cassette assets generated!")
