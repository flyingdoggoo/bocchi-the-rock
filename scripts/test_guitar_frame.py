import math
import random
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageFont

# Load high-res crop of Bocchi shredding
bocchi_src = Image.open('public/assets/2k/bocchi_guitarist_crop.png').convert('RGBA')

# Target canvas size: 800x800 for crisp 2K display
CANVAS_W, CANVAS_H = 800, 800

def generate_frame(i, total_frames=80):
    t = i / (total_frames - 1) # 0.0 to 1.0
    
    # Base canvas with dark STARRY livehouse background
    frame = Image.new('RGBA', (CANVAS_W, CANVAS_H), (10, 9, 14, 255))
    draw = ImageDraw.Draw(frame)
    
    # 1. Background Stage Atmosphere & Spotlights
    # Tempo ramps up as solo builds
    bpm_freq = 8 + 24 * (t ** 1.4)
    rhythm = math.sin(t * math.pi * bpm_freq)
    pulse = 0.5 + 0.5 * rhythm
    
    # Volumetric spotlight beams swinging
    amber_angle = math.sin(t * 7) * 0.35
    pink_angle = math.cos(t * 8.5) * 0.4
    
    # Amber spot
    amber_alpha = int(35 + 50 * (1 - t * 0.3) + 30 * pulse)
    amber_x = int(CANVAS_W * 0.25 + 120 * math.sin(t * 5))
    draw.polygon([(CANVAS_W // 2, -40), (amber_x - 140, CANVAS_H), (amber_x + 140, CANVAS_H)], 
                 fill=(255, 209, 59, min(255, amber_alpha)))
                 
    # Hot pink / Magenta spot (intensifies as solo reaches climax)
    pink_alpha = int(25 + 140 * (t ** 1.5) + 40 * pulse)
    pink_x = int(CANVAS_W * 0.75 + 140 * math.cos(t * 6.2))
    draw.polygon([(CANVAS_W // 2, -40), (pink_x - 160, CANVAS_H), (pink_x + 160, CANVAS_H)], 
                 fill=(255, 42, 112, min(255, pink_alpha)))
                 
    # Cyan backlight at peak (t > 0.5)
    if t > 0.45:
        cyan_alpha = int(90 * ((t - 0.45) / 0.55) * (0.7 + 0.3 * math.sin(t * 22)))
        draw.polygon([(CANVAS_W // 2, -40), (CANVAS_W // 2 - 100, CANVAS_H), (CANVAS_W // 2 + 100, CANVAS_H)],
                     fill=(0, 240, 255, min(255, cyan_alpha)))
    
    # Background STARRY live house mesh & amp silhouette
    draw.rectangle([0, CANVAS_H - 140, CANVAS_W, CANVAS_H], fill=(14, 13, 20, 255))
    # Amps
    draw.rectangle([20, CANVAS_H - 240, 160, CANVAS_H - 130], fill=(22, 20, 28, 255), outline=(45, 42, 58, 255), width=2)
    draw.rectangle([CANVAS_W - 170, CANVAS_H - 240, CANVAS_W - 20, CANVAS_H - 130], fill=(22, 20, 28, 255), outline=(45, 42, 58, 255), width=2)

    # 2. Rocking & Headbanging Character Animation
    # Dynamic scale and headbang rocking angle
    # Starting slightly pulled back, zooming in on Bocchi's intense solo expression and hands
    zoom_scale = 0.28 + 0.05 * (t ** 1.2) + 0.015 * pulse
    
    # Headbanging angle & vertical bob
    headbang_angle = math.sin(t * math.pi * bpm_freq) * (1.5 + 4.5 * t)
    bob_y = math.sin(t * math.pi * bpm_freq) * (3.0 + 8.0 * t)
    sway_x = math.cos(t * math.pi * bpm_freq * 0.5) * (2.0 + 6.0 * t)
    
    # Scale Bocchi
    bw = int(bocchi_src.width * zoom_scale)
    bh = int(bocchi_src.height * zoom_scale)
    bocchi_scaled = bocchi_src.resize((bw, bh), Image.Resampling.LANCZOS)
    
    # Rotate with smooth bicubic interpolation
    bocchi_rotated = bocchi_scaled.rotate(headbang_angle, resample=Image.Resampling.BICUBIC, expand=True)
    
    # Center character with rhythm sway & bob
    bx = (CANVAS_W - bocchi_rotated.width) // 2 + int(sway_x)
    by = CANVAS_H - bocchi_rotated.height - 20 + int(bob_y)
    
    frame.alpha_composite(bocchi_rotated, (bx, by))
    
    # 3. Dynamic Guitar Shredding FX Layer
    fx = Image.new('RGBA', (CANVAS_W, CANVAS_H), (0, 0, 0, 0))
    fx_draw = ImageDraw.Draw(fx)
    
    # Approximate guitar center in canvas coords
    gx = CANVAS_W // 2 - 30 + int(sway_x)
    gy = CANVAS_H // 2 + 70 + int(bob_y)
    
    # A. Strumming Motion Blur & Pick Speed Trails
    # Red guitar pick is strumming furiously up and down
    pick_x = gx + 55
    pick_y = gy + 35
    strum_offset = math.sin(t * math.pi * bpm_freq * 2) * (12 + 25 * t)
    
    # Strum speed sweeps
    num_strum_lines = int(3 + 12 * t)
    for s in range(num_strum_lines):
        sweep_y = pick_y + strum_offset + (s - num_strum_lines // 2) * 5
        sweep_alpha = int(160 * (1.0 - s / num_strum_lines) * (0.4 + 0.6 * t))
        sweep_col = (255, 77, 100, sweep_alpha) if s % 2 == 0 else (255, 209, 59, sweep_alpha)
        fx_draw.line([(pick_x - 45, sweep_y - 12), (pick_x + 50, sweep_y + 10)], fill=sweep_col, width=2)
        
    # B. Vibrating Fretboard Strings & Glints
    # Strings running from fret hand (approx gx - 140, gy - 80) to bridge (gx + 70, gy + 30)
    fx_fret_x = gx - 150
    fx_fret_y = gy - 75
    fx_bridge_x = gx + 85
    fx_bridge_y = gy + 45
    
    for string_idx in range(6):
        string_offset = (string_idx - 2.5) * 4
        # String vibration wave
        string_vib = math.sin(t * 40 + string_idx) * (1.0 + 3.5 * t)
        str_start = (fx_fret_x, fx_fret_y + string_offset + string_vib)
        str_mid = ((fx_fret_x + fx_bridge_x) // 2, (fx_fret_y + fx_bridge_y) // 2 + string_offset - string_vib * 1.5)
        str_end = (fx_bridge_x, fx_bridge_y + string_offset + string_vib * 0.5)
        
        string_col = (255, 240, 180, int(120 + 100 * t))
        fx_draw.line([str_start, str_mid, str_end], fill=string_col, width=1)
        
    # C. Electric Overdrive Lightning Sparks along Fretboard (t > 0.3)
    if t > 0.28:
        random.seed(int(i * 997))
        num_sparks = int(5 + 22 * t)
        for _ in range(num_sparks):
            # Spark origin along neck
            prog = random.random()
            sp_x = int(fx_fret_x + prog * (fx_bridge_x - fx_fret_x) + random.randint(-15, 15))
            sp_y = int(fx_fret_y + prog * (fx_bridge_y - fx_fret_y) + random.randint(-20, 20))
            
            # Jagged lightning branch
            bx1 = sp_x + random.randint(-18, 18)
            by1 = sp_y + random.randint(-18, 18)
            bx2 = bx1 + random.randint(-14, 14)
            by2 = by1 + random.randint(-14, 14)
            
            spark_col = random.choice([
                (255, 255, 255, 255),
                (255, 117, 151, 230),  # Pink
                (67, 131, 255, 230),   # Blue
                (255, 215, 60, 240)    # Gold
            ])
            fx_draw.line([(sp_x, sp_y), (bx1, by1), (bx2, by2)], fill=spark_col, width=random.randint(1, 3))
            fx_draw.ellipse([sp_x - 3, sp_y - 3, sp_x + 3, sp_y + 3], fill=(255, 255, 255, 255))

    # D. Sonic Overdrive Shockwave Rings (t > 0.55)
    if t > 0.52:
        ring_prog = ((t * 4.5) % 1.0)
        ring_rad = int(50 + 320 * ring_prog)
        ring_alpha = int(220 * (1.0 - ring_prog))
        fx_draw.ellipse([gx - ring_rad, gy - ring_rad, gx + ring_rad, gy + ring_rad], 
                        outline=(255, 117, 151, ring_alpha), width=3)
        
        # Second echo ring in electric blue
        ring2_prog = (((t * 4.5) + 0.5) % 1.0)
        ring2_rad = int(40 + 280 * ring2_prog)
        ring2_alpha = int(180 * (1.0 - ring2_prog))
        fx_draw.ellipse([gx - ring2_rad, gy - ring2_rad, gx + ring2_rad, gy + ring2_rad], 
                        outline=(67, 131, 255, ring2_alpha), width=2)

    # E. 4-Point Stage Lens Glints on Bocchi's Hair Cubes & Les Paul Gold Pickups
    def draw_star_glint(cx, cy, radius, color):
        fx_draw.line([(cx - radius, cy), (cx + radius, cy)], fill=color, width=2)
        fx_draw.line([(cx, cy - radius), (cx, cy + radius)], fill=color, width=2)
        fx_draw.ellipse([cx - 2, cy - 2, cx + 2, cy + 2], fill=(255, 255, 255, 255))
        
    # Blue/Yellow hair cube glint
    cube_x = CANVAS_W // 2 - 25 + int(sway_x)
    cube_y = CANVAS_H // 2 - 195 + int(bob_y)
    glint_size = int(8 + 14 * pulse)
    draw_star_glint(cube_x, cube_y, glint_size, (255, 215, 60, 240))
    
    # Gold pickup glint
    pickup_x = gx + 15
    pickup_y = gy + 10
    draw_star_glint(pickup_x, pickup_y, int(10 + 16 * pulse), (255, 235, 150, 255))

    # Composite FX layer
    frame.alpha_composite(fx)
    return frame

# Test generation of 4 representative frames
print("Generating test frames 5, 25, 50, 75...")
for test_i in [5, 25, 50, 75]:
    test_img = generate_frame(test_i)
    test_img.save(f'public/assets/sequence/test_frame_{test_i}.png')
print("Test frames generated!")
