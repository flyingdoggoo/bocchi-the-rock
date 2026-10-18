import os
import wave
import struct
import math
import random

os.makedirs('public/assets/audio', exist_ok=True)

SAMPLE_RATE = 44100

def create_guitar_solo():
    # Riff notes in frequencies (Hz) - E minor / Rock solo phrasing
    # E4, G4, A4, B4, D5, E5, G5, A5
    notes = [
        (329.63, 0.4, 0.0),   # E4
        (392.00, 0.3, 0.0),   # G4
        (440.00, 0.35, 0.0),  # A4
        (493.88, 0.5, 0.05),  # B4 (bend)
        (587.33, 0.35, 0.0),  # D5
        (659.25, 0.6, 0.08),  # E5 (vibrato)
        (587.33, 0.25, 0.0),  # D5
        (493.88, 0.25, 0.0),  # B4
        (440.00, 0.4, 0.0),   # A4
        (392.00, 0.3, 0.0),   # G4
        (329.63, 1.2, 0.04),  # E4 power sustained
    ]
    
    total_duration = sum(dur for _, dur, _ in notes) + 0.5
    total_samples = int(SAMPLE_RATE * total_duration)
    audio = [0.0] * total_samples
    
    current_sample = 0
    
    for freq, duration, bend_depth in notes:
        note_samples = int(duration * SAMPLE_RATE)
        for i in range(note_samples):
            t = i / SAMPLE_RATE
            progress = i / note_samples
            
            # Pitch bend / vibrato
            current_freq = freq * (1.0 + bend_depth * math.sin(progress * math.pi) + 0.015 * math.sin(t * 35))
            
            # Karplus-Strong / Multi-harmonic saw with tube warmth
            harmonic1 = math.sin(2.0 * math.pi * current_freq * t)
            harmonic2 = 0.5 * math.sin(4.0 * math.pi * current_freq * t)
            harmonic3 = 0.3 * math.sin(6.0 * math.pi * current_freq * t)
            harmonic4 = 0.2 * math.sin(8.0 * math.pi * current_freq * t)
            sub = 0.4 * math.sin(math.pi * current_freq * t)
            
            raw_signal = (harmonic1 + harmonic2 + harmonic3 + harmonic4 + sub) * 1.5
            
            # Tube overdrive saturation: tanh-like soft clipping
            distorted = math.tanh(raw_signal * 2.2)
            
            # Amplitude envelope: snappy pick attack + sustained decay
            if t < 0.008:
                env = t / 0.008
            else:
                env = math.exp(-(t - 0.008) * 2.5)
                
            idx = current_sample + i
            if idx < total_samples:
                # Add delay / echo (STARRY live room reverb)
                delay_offset = int(0.18 * SAMPLE_RATE)
                echo = audio[idx - delay_offset] * 0.35 if idx >= delay_offset else 0.0
                audio[idx] += distorted * env * 0.7 + echo
                
        current_sample += int(duration * 0.9 * SAMPLE_RATE)  # Slight legato overlap
        
    # Normalize
    max_val = max(abs(x) for x in audio) or 1.0
    audio_norm = [x / max_val * 0.85 for x in audio]
    
    # Write 16-bit PCM WAV
    out_path = 'public/assets/audio/bocchi_guitar_solo.wav'
    with wave.open(out_path, 'wb') as wav:
        wav.setnchannels(1)  # Mono
        wav.setsampwidth(2)  # 16-bit
        wav.setframerate(SAMPLE_RATE)
        for s in audio_norm:
            sample_val = int(s * 32767.0)
            sample_val = max(-32768, min(32767, sample_val))
            wav.writeframes(struct.pack('<h', sample_val))
            
    print(f"Generated {out_path} ({len(audio_norm)/SAMPLE_RATE:.1f}s)")

create_guitar_solo()
