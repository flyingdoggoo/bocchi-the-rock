import os
import math
import random
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageFont

os.makedirs('public/assets/sequence', exist_ok=True)

# Load high-res crop of Bocchi playing guitar
bocchi_src = Image.open('public/assets/2k/bocchi_guitarist_crop.png').convert('RGBA')

CANVAS_W, CANVAS_H = 800, 800
TOTAL_FRAMES = 80

print(f"Generating {TOTAL_FRAMES} frames of Bocchi Guitar Solo at 800x800 WebP...")

# Try loading a bold font for rock SFX
font_path = "C:/Windows/Fonts/meiryb.ttc" # Meiryo Bold (supports Japanese kanji/kana)
if not os.path.exists(font_path):
    font_path = "C:/Windows/Fonts/msgothic.ttc"
if not os.path.exists(font_path):
    font_path = "C:/Windows/Fonts/arialbd.ttf"

try:
    sfx_font_large = ImageFont.truetype(font_path, 42)
    sfx_font_huge = ImageFont.truetype(font_path, 58)
    sfx_font_med = ImageFont.truetype(font_path, 28)
except Exception:
    sfx_font_large = ImageFont.load_default()
    sfx_font_huge = ImageFont.load_default()
    sfx_font_med = ImageFont.load_default()

for i in range(TOTAL_FRAMES):
    t = i / (TOTAL_FRAMES - 1)  # 0.0 to 1.0
    
    # 1. Base Stage Atmosphere
    frame = Image.new('RGBA', (CANVAS_W, CANVAS_H), (10, 9, 14, 255))
    draw = ImageDraw.Draw(frame)
    
    # Live house rhythmic tempo
    # Stage I: 100 BPM -> Stage IV: 240+ BPM shredding frenzy
    bpm_freq = 6 + 26 * (t ** 1.3)
    beat = math.sin(t * math.pi * bpm_freq)
    pulse = 0.5 + 0.5 * beat
    
    # Volumetric Stage Spotlights
    # Left Amber spot sweeps
    amber_alpha = int(40 + 55 * math.cos(t * 6) + 35 * pulse)
    amber_x = int(CANVAS_W * 0.20 + 130 * math.sin(t * 4.8))
    draw.polygon([(CANVAS_W // 2, -60), (amber_x - 160, CANVAS_H + 50), (amber_x + 160, CANVAS_H + 50)], 
                 fill=(255, 209, 59, min(240, amber_alpha)))
                 
    # Right Hot Magenta spot sweeps (intensifies with solo overdrive)
    pink_alpha = int(30 + 150 * (t ** 1.4) + 45 * pulse)
    pink_x = int(CANVAS_W * 0.80 + 150 * math.cos(t * 5.5))
    draw.polygon([(CANVAS_W // 2, -60), (pink_x - 170, CANVAS_H + 50), (pink_x + 170, CANVAS_H + 50)], 
                 fill=(255, 42, 112, min(250, pink_alpha)))
                 
    # Overhead Electric Cyan backlight at peak (t > 0.45)
    if t > 0.42:
        cyan_intensity = (t - 0.42) / 0.58
        cyan_alpha = int(120 * cyan_intensity * (0.65 + 0.35 * math.sin(t * 24)))
        cyan_x = int(CANVAS_W // 2 + 80 * math.sin(t * 9))
        draw.polygon([(CANVAS_W // 2, -60), (cyan_x - 130, CANVAS_H + 50), (cyan_x + 130, CANVAS_H + 50)],
                     fill=(0, 240, 255, min(230, cyan_alpha)))
                     
    # 2. Rocking & Headbanging Character Animation
    # Progressive dynamic camera zoom: draws viewer into the fingers & guitar
    base_zoom = 0.27 + 0.05 * (t ** 1.1) + 0.012 * pulse
    
    # Headbanging angle & bodily sway
    # Bocchi rocks forward on downbeats
    rock_angle = beat * (1.2 + 3.8 * t)
    bob_y = abs(beat) * (4.0 + 10.0 * t)  # Head drops on the beat
    sway_x = math.cos(t * math.pi * bpm_freq * 0.5) * (3.0 + 8.0 * t)
    
    bw = int(bocchi_src.width * base_zoom)
    bh = int(bocchi_src.height * base_zoom)
    bocchi_scaled = bocchi_src.resize((bw, bh), Image.Resampling.LANCZOS)
    
    # Rotate with smooth bicubic sampling
    bocchi_rot = bocchi_scaled.rotate(rock_angle, resample=Image.Resampling.BICUBIC, expand=True)
    
    # Position: guarantee bottom edge overflows past CANVAS_H so no black wedge appears
    bx = (CANVAS_W - bocchi_rot.width) // 2 + int(sway_x)
    by = CANVAS_H - bocchi_rot.height + 45 + int(bob_y)
    
    frame.alpha_composite(bocchi_rot, (bx, by))
    
    # 3. Dynamic Visual FX Layer
    fx = Image.new('RGBA', (CANVAS_W, CANVAS_H), (0, 0, 0, 0))
    fx_draw = ImageDraw.Draw(fx)
    
    # Anchor points on the guitar in rotated/translated space
    # Center of guitar body
    gx = CANVAS_W // 2 - 35 + int(sway_x)
    gy = CANVAS_H // 2 + 105 + int(bob_y)
    
    # Fretboard hand anchor (top-left)
    fret_x = gx - 160
    fret_y = gy - 135
    
    # Strumming hand & pick anchor (bottom-right)
    pick_x = gx - 10
    pick_y = gy + 120
    
    # Pickups / bridge anchor (center-right)
    bridge_x = gx + 5
    bridge_y = gy + 40
    
    # A. Strumming Alternate Picking Motion Trails
    strum_dir = math.sin(t * math.pi * bpm_freq * 2.2)
    strum_offset = strum_dir * (14 + 30 * t)
    
    num_strum_lines = int(4 + 14 * t)
    for s in range(num_strum_lines):
        line_y = pick_y + strum_offset + (s - num_strum_lines // 2) * 6
        strum_alpha = int(180 * (1.0 - s / num_strum_lines) * (0.35 + 0.65 * t))
        col = (255, 75, 115, strum_alpha) if s % 2 == 0 else (255, 215, 60, strum_alpha)
        fx_draw.line([(pick_x - 55, line_y - 15), (pick_x + 55, line_y + 12)], fill=col, width=2)
        
    # Red pick ghost afterimage during high shredding (t > 0.35)
    if t > 0.35:
        ghost_alpha = int(160 * (t ** 1.2))
        fx_draw.polygon([
            (pick_x + 10, pick_y + strum_offset - 10),
            (pick_x + 28, pick_y + strum_offset + 8),
            (pick_x - 4, pick_y + strum_offset + 14)
        ], fill=(255, 30, 60, ghost_alpha))
        
    # B. 6 Vibrating Guitar Strings (E, A, D, G, B, e)
    for s_idx in range(6):
        spacing = (s_idx - 2.5) * 5
        vib_amp = math.sin(t * 45 + s_idx * 1.5) * (1.2 + 4.5 * t)
        
        p1 = (fret_x + spacing * 0.8, fret_y + spacing * 0.5)
        # Midpoint vibrating with high harmonic frequency
        mid_x = (fret_x + bridge_x) // 2 + spacing
        mid_y = (fret_y + bridge_y) // 2 + spacing + vib_amp
        p3 = (bridge_x + spacing * 0.6, bridge_y + spacing * 0.8)
        
        str_alpha = int(140 + 115 * t)
        str_color = (255, 245, 195, str_alpha)
        fx_draw.line([p1, (mid_x, mid_y), p3], fill=str_color, width=1)

    # C. Electric Overdrive Lightning Sparks (t > 0.25)
    if t > 0.22:
        random.seed(int(i * 1237))
        num_sparks = int(6 + 28 * t)
        for _ in range(num_sparks):
            # Sparks track along the neck and pickups
            along_neck = random.random()
            spk_x = int(fret_x + along_neck * (bridge_x - fret_x) + random.randint(-18, 18))
            spk_y = int(fret_y + along_neck * (bridge_y - fret_y) + random.randint(-22, 22))
            
            # Jagged lightning bolts
            b1_x = spk_x + random.randint(-22, 22)
            b1_y = spk_y + random.randint(-22, 22)
            b2_x = b1_x + random.randint(-18, 18)
            b2_y = b1_y + random.randint(-18, 18)
            
            spk_color = random.choice([
                (255, 255, 255, 255),
                (255, 117, 151, 240),  # Bocchi Pink
                (67, 131, 255, 240),   # Ryo Blue
                (255, 209, 59, 250),   # Nijika Yellow
                (0, 240, 255, 240)     # Neon Cyan
            ])
            fx_draw.line([(spk_x, spk_y), (b1_x, b1_y), (b2_x, b2_y)], fill=spk_color, width=random.randint(1, 3))
            fx_draw.ellipse([spk_x - 3, spk_y - 3, spk_x + 3, spk_y + 3], fill=(255, 255, 255, 255))
            
    # D. Sonic Overdrive Shockwave Rings (t > 0.48)
    if t > 0.48:
        # Concentric expanding rings from bridge pickup
        for r_offset in [0.0, 0.35, 0.70]:
            prog = ((t * 4.0 + r_offset) % 1.0)
            radius = int(40 + 360 * prog)
            alpha = int(220 * (1.0 - prog) * (t ** 0.8))
            ring_col = (255, 117, 151, alpha) if r_offset < 0.5 else (0, 240, 255, alpha)
            fx_draw.ellipse([bridge_x - radius, bridge_y - radius, bridge_x + radius, bridge_y + radius],
                            outline=ring_col, width=2)

    # E. 4-Point Star Glints on Bocchi's Hair Cube & Les Paul Gold Hardware
    def draw_glint(cx, cy, radius, col):
        fx_draw.line([(cx - radius, cy), (cx + radius, cy)], fill=col, width=2)
        fx_draw.line([(cx, cy - radius), (cx, cy + radius)], fill=col, width=2)
        fx_draw.ellipse([cx - 2, cy - 2, cx + 2, cy + 2], fill=(255, 255, 255, 255))
        
    # Hair cube glint (yellow/blue)
    hc_x = CANVAS_W // 2 - 38 + int(sway_x)
    hc_y = CANVAS_H // 2 - 195 + int(bob_y)
    draw_glint(hc_x, hc_y, int(10 + 16 * pulse), (255, 215, 60, 255))
    
    # Gold neck pickup glint
    draw_glint(bridge_x - 25, bridge_y - 20, int(12 + 18 * pulse), (255, 235, 140, 255))
    
    # F. Stylized Manga Rock SFX Typography
    # Render authentic rock sound effects at dramatic peaks
    sfx_text = None
    sfx_pos = (CANVAS_W - 240, 80)
    sfx_col = (255, 215, 60, 240)
    
    if 0.24 <= t <= 0.34:
        sfx_text = "ジャジャッ！"
        sfx_col = (255, 209, 59, int(230 * math.sin((t - 0.24) / 0.10 * math.pi)))
        sfx_pos = (CANVAS_W - 220, 80 + int(bob_y))
    elif 0.48 <= t <= 0.62:
        sfx_text = "ギュイイィン！"
        sfx_col = (255, 117, 151, int(240 * math.sin((t - 0.48) / 0.14 * math.pi)))
        sfx_pos = (50, 90 + int(bob_y))
    elif 0.72 <= t <= 0.88:
        sfx_text = "ドドドドッ！"
        sfx_col = (0, 240, 255, int(240 * math.sin((t - 0.72) / 0.16 * math.pi)))
        sfx_pos = (CANVAS_W - 240, 75 + int(bob_y))
    elif t > 0.88:
        sfx_text = "バーーーーーン！"
        sfx_col = (255, 255, 255, int(250 * math.sin((t - 0.88) / 0.12 * math.pi)))
        sfx_pos = (CANVAS_W // 2 - 160, 60 + int(bob_y))
        
    if sfx_text:
        # Draw text drop-shadow then text
        fx_draw.text((sfx_pos[0] + 3, sfx_pos[1] + 3), sfx_text, font=sfx_font_large, fill=(0, 0, 0, 200))
        fx_draw.text(sfx_pos, sfx_text, font=sfx_font_large, fill=sfx_col)

    # Composite FX
    frame.alpha_composite(fx)
    
    # 4. Save WebP frame (quality 88 for crisp retina rendering)
    out_file = f'public/assets/sequence/frame_{i:03d}.webp'
    frame.save(out_file, 'WEBP', quality=88, method=4)

print(f"Successfully generated all {TOTAL_FRAMES} high-definition guitar shredding frames!")
