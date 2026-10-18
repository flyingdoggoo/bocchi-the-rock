import os

os.makedirs('public/assets/chibi', exist_ok=True)
os.makedirs('public/assets/quirks', exist_ok=True)
os.makedirs('public/assets/gear', exist_ok=True)

# 1. Chibi Bocchi Shy Face
bocchi_shy_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <defs>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#ff7597" flood-opacity="0.5"/>
    </filter>
  </defs>
  <!-- Hair Base Pink -->
  <circle cx="50" cy="50" r="38" fill="#ff7597" filter="url(#glow)"/>
  <!-- Hair accessories: Blue & Yellow Cubes -->
  <rect x="18" y="18" width="14" height="14" rx="2" fill="#4383ff" stroke="#1a1a24" stroke-width="2"/>
  <rect x="28" y="24" width="14" height="14" rx="2" fill="#ffd13b" stroke="#1a1a24" stroke-width="2"/>
  <!-- Face Skin -->
  <path d="M 28 42 Q 50 38 72 42 Q 76 68 50 78 Q 24 68 28 42 Z" fill="#fff0e6"/>
  <!-- Bangs -->
  <path d="M 26 40 Q 38 52 44 44 Q 52 54 60 42 Q 68 50 74 38 Q 50 30 26 40 Z" fill="#ff7597"/>
  <!-- Shy Blushing Cheeks -->
  <ellipse cx="36" cy="58" rx="6" ry="3" fill="#ff4d79" opacity="0.6"/>
  <ellipse cx="64" cy="58" rx="6" ry="3" fill="#ff4d79" opacity="0.6"/>
  <!-- Nervous Eyes -->
  <ellipse cx="38" cy="50" rx="3.5" ry="5" fill="#1b1b22"/>
  <ellipse cx="62" cy="50" rx="3.5" ry="5" fill="#1b1b22"/>
  <circle cx="39.5" cy="48" r="1.5" fill="#ffffff"/>
  <circle cx="63.5" cy="48" r="1.5" fill="#ffffff"/>
  <!-- Wobbly Mouth -->
  <path d="M 46 64 Q 48 62 50 64 Q 52 66 54 64" fill="none" stroke="#1b1b22" stroke-width="2" stroke-linecap="round"/>
  <!-- Sweat Drop -->
  <path d="M 72 46 C 72 44 75 42 75 40 C 75 42 78 44 78 46 C 78 48 75 50 75 50 C 75 50 72 48 72 46 Z" fill="#00f0ff"/>
</svg>"""

with open('public/assets/chibi/bocchi_shy.svg', 'w', encoding='utf-8') as f:
    f.write(bocchi_shy_svg)

# 2. Chibi Bocchi Panic Face
bocchi_panic_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <circle cx="50" cy="50" r="38" fill="#ff7597"/>
  <!-- Cubes -->
  <rect x="18" y="18" width="14" height="14" rx="2" fill="#4383ff" stroke="#1a1a24" stroke-width="2"/>
  <rect x="28" y="24" width="14" height="14" rx="2" fill="#ffd13b" stroke="#1a1a24" stroke-width="2"/>
  <!-- Face Skin -->
  <path d="M 28 42 Q 50 38 72 42 Q 76 70 50 80 Q 24 70 28 42 Z" fill="#fff0e6"/>
  <!-- Bangs shaking -->
  <path d="M 24 38 Q 38 56 42 42 Q 54 58 62 40 Q 72 54 76 36 Q 50 28 24 38 Z" fill="#ff7597"/>
  <!-- Panic Spirals / Screaming Hollow Eyes -->
  <circle cx="38" cy="50" r="6" fill="none" stroke="#1b1b22" stroke-width="2.5"/>
  <circle cx="62" cy="50" r="6" fill="none" stroke="#1b1b22" stroke-width="2.5"/>
  <circle cx="38" cy="50" r="2" fill="#1b1b22"/>
  <circle cx="62" cy="50" r="2" fill="#1b1b22"/>
  <!-- Screaming wide open zig-zag mouth -->
  <path d="M 42 62 L 46 66 L 50 62 L 54 66 L 58 62 L 56 72 L 44 72 Z" fill="#ff4d79" stroke="#1b1b22" stroke-width="2"/>
  <!-- Heavy blue panic shadow lines on forehead -->
  <line x1="36" y1="40" x2="36" y2="46" stroke="#4383ff" stroke-width="2"/>
  <line x1="42" y1="38" x2="42" y2="45" stroke="#4383ff" stroke-width="2"/>
  <line x1="48" y1="37" x2="48" y2="44" stroke="#4383ff" stroke-width="2"/>
  <line x1="54" y1="38" x2="54" y2="45" stroke="#4383ff" stroke-width="2"/>
  <line x1="60" y1="40" x2="60" y2="46" stroke="#4383ff" stroke-width="2"/>
</svg>"""

with open('public/assets/chibi/bocchi_panic.svg', 'w', encoding='utf-8') as f:
    f.write(bocchi_panic_svg)

# 3. Chibi Bocchi Slime (Tsuchinoko)
bocchi_slime_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <!-- Puddle base -->
  <ellipse cx="50" cy="74" rx="42" ry="14" fill="#ff7597" opacity="0.9"/>
  <!-- Melting head mound -->
  <path d="M 22 74 C 20 48 35 34 50 34 C 65 34 80 48 78 74 C 84 76 90 80 84 84 C 74 90 26 90 16 84 C 10 80 16 76 22 74 Z" fill="#ff7597"/>
  <!-- Hair Cubes floating crookedly -->
  <rect x="22" y="24" width="12" height="12" rx="2" fill="#4383ff" transform="rotate(-15 28 30)" stroke="#1a1a24" stroke-width="1.5"/>
  <rect x="32" y="28" width="12" height="12" rx="2" fill="#ffd13b" transform="rotate(10 38 34)" stroke="#1a1a24" stroke-width="1.5"/>
  <!-- Two droopy eyes on puddle -->
  <ellipse cx="40" cy="56" rx="3" ry="2" fill="#1b1b22"/>
  <ellipse cx="60" cy="56" rx="3" ry="2" fill="#1b1b22"/>
  <!-- Melting mouth line -->
  <path d="M 44 64 Q 50 67 56 64" fill="none" stroke="#1b1b22" stroke-width="2" stroke-linecap="round"/>
  <!-- Melting droplets -->
  <circle cx="86" cy="80" r="3" fill="#ff7597"/>
  <circle cx="12" cy="82" r="2.5" fill="#ff7597"/>
</svg>"""

with open('public/assets/chibi/bocchi_slime.svg', 'w', encoding='utf-8') as f:
    f.write(bocchi_slime_svg)

# 4. Cute Pink Guitar Pick with Star
bocchi_pick_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <defs>
    <linearGradient id="pickGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff7597"/>
      <stop offset="100%" stop-color="#d6336c"/>
    </linearGradient>
  </defs>
  <!-- Tear-drop pick shape -->
  <path d="M 50 92 C 30 70 12 50 14 26 C 16 12 30 8 50 8 C 70 8 84 12 86 26 C 88 50 70 70 50 92 Z" 
        fill="url(#pickGrad)" stroke="#ffd13b" stroke-width="3"/>
  <!-- Star symbol in center -->
  <polygon points="50,24 55,36 68,36 57,44 61,56 50,48 39,56 43,44 32,36 45,36" fill="#ffd13b"/>
  <!-- STARRY text -->
  <text x="50" y="70" font-family="'Impact', sans-serif" font-size="11" fill="#ffffff" text-anchor="middle" letter-spacing="1.5">STARRY</text>
</svg>"""

with open('public/assets/chibi/guitar_pick.svg', 'w', encoding='utf-8') as f:
    f.write(bocchi_pick_svg)

# 5. Ripe Mango Box Quirk ("完熟マンゴー")
mango_box_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 400" width="500" height="400">
  <!-- Cardboard Box Body -->
  <defs>
    <linearGradient id="cardboard" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d4a373"/>
      <stop offset="100%" stop-color="#bc8a5f"/>
    </linearGradient>
    <filter id="boxShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="12" stdDeviation="15" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
  </defs>
  <!-- Floor Shadow -->
  <ellipse cx="250" cy="370" rx="200" ry="25" fill="#050508" opacity="0.8"/>
  
  <!-- Bocchi Peeking Inside First (under flaps) -->
  <g id="bocchi-peeking">
    <!-- Pink hair dome -->
    <path d="M 160 210 C 160 110 340 110 340 210 Z" fill="#ff7597"/>
    <!-- Hair accessories cubes -->
    <rect x="180" y="110" width="28" height="28" rx="4" fill="#4383ff" stroke="#1a1a24" stroke-width="3"/>
    <rect x="200" y="125" width="28" height="28" rx="4" fill="#ffd13b" stroke="#1a1a24" stroke-width="3"/>
    <!-- Face -->
    <path d="M 180 180 Q 250 170 320 180 L 320 220 L 180 220 Z" fill="#fff0e6"/>
    <!-- Nervous Shaking Eyes -->
    <ellipse cx="215" cy="188" rx="8" ry="12" fill="#1b1b22"/>
    <ellipse cx="285" cy="188" rx="8" ry="12" fill="#1b1b22"/>
    <circle cx="218" cy="184" r="3.5" fill="#ffffff"/>
    <circle cx="288" cy="184" r="3.5" fill="#ffffff"/>
    <!-- Blushing -->
    <ellipse cx="200" cy="202" rx="14" ry="7" fill="#ff4d79" opacity="0.5"/>
    <ellipse cx="300" cy="202" rx="14" ry="7" fill="#ff4d79" opacity="0.5"/>
    <!-- Two Hands gripping the box rim -->
    <ellipse cx="190" cy="222" rx="14" ry="9" fill="#fff0e6" stroke="#d4a373" stroke-width="2"/>
    <ellipse cx="310" cy="222" rx="14" ry="9" fill="#fff0e6" stroke="#d4a373" stroke-width="2"/>
  </g>
  
  <!-- Front Box Face -->
  <rect x="100" y="210" width="300" height="150" fill="url(#cardboard)" stroke="#8c5836" stroke-width="3" filter="url(#boxShadow)"/>
  
  <!-- Open Top Flaps -->
  <!-- Left Flap Folded Out -->
  <polygon points="100,210 40,160 100,180" fill="#c69363" stroke="#8c5836" stroke-width="2"/>
  <!-- Right Flap Folded Out -->
  <polygon points="400,210 460,160 400,180" fill="#c69363" stroke="#8c5836" stroke-width="2"/>
  
  <!-- Box Graphics: "完熟マンゴー" (Ripe Mango) Brand -->
  <g transform="translate(140, 240)">
    <rect x="0" y="0" width="220" height="90" fill="#a0522d" rx="6" opacity="0.15"/>
    <circle cx="45" cy="45" r="30" fill="#ff9f1c"/>
    <ellipse cx="50" cy="42" rx="20" ry="16" fill="#e71d36" opacity="0.4"/>
    <!-- Japanese Kanji: 完熟マンゴー -->
    <text x="90" y="38" font-family="'Noto Sans JP', sans-serif" font-weight="900" font-size="24" fill="#582f0e">完熟マンゴー</text>
    <text x="92" y="62" font-family="'Barlow Condensed', sans-serif" font-weight="700" font-size="14" fill="#7f4f24" letter-spacing="2">PREMIUM MANGO BOX</text>
    <text x="92" y="78" font-family="monospace" font-size="11" fill="#8c5836">PRODUCE OF MIYAZAKI // 4.5KG</text>
  </g>
  
  <!-- Shipping Barcode & FRAGILE stamp -->
  <g transform="translate(120, 320)">
    <rect x="0" y="0" width="100" height="25" fill="#f4edea" stroke="#8c5836" stroke-width="1"/>
    <!-- Barcode lines -->
    <line x1="10" y1="4" x2="10" y2="21" stroke="#000" stroke-width="2"/>
    <line x1="15" y1="4" x2="15" y2="21" stroke="#000" stroke-width="1"/>
    <line x1="20" y1="4" x2="20" y2="21" stroke="#000" stroke-width="3"/>
    <line x1="26" y1="4" x2="26" y2="21" stroke="#000" stroke-width="1"/>
    <line x1="32" y1="4" x2="32" y2="21" stroke="#000" stroke-width="2"/>
    <line x1="40" y1="4" x2="40" y2="21" stroke="#000" stroke-width="4"/>
    <line x1="50" y1="4" x2="50" y2="21" stroke="#000" stroke-width="1"/>
    <line x1="60" y1="4" x2="60" y2="21" stroke="#000" stroke-width="3"/>
    <line x1="72" y1="4" x2="72" y2="21" stroke="#000" stroke-width="2"/>
    <line x1="85" y1="4" x2="85" y2="21" stroke="#000" stroke-width="2"/>
  </g>
  <rect x="290" y="318" width="90" height="28" fill="#d90429" rx="3"/>
  <text x="335" y="337" font-family="'Impact', sans-serif" font-size="13" fill="#ffffff" text-anchor="middle" letter-spacing="1.5">HANDLE WITH CARE</text>
</svg>"""

with open('public/assets/quirks/mango_box.svg', 'w', encoding='utf-8') as f:
    f.write(mango_box_svg)

print("Vector assets generated successfully!")
