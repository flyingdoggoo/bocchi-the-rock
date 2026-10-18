import urllib.request
import os

os.makedirs('public/assets/2k', exist_ok=True)

wallpapers = {
    'public/assets/2k/bocchi_guitar_solo_2k.png': 'https://w.wallhaven.cc/full/d8/wallhaven-d8welo.png',
    'public/assets/2k/kessoku_band_stage_4k.jpg': 'https://w.wallhaven.cc/full/ly/wallhaven-lyjdxr.jpg',
    'public/assets/2k/kessoku_band_walk_2k.png': 'https://w.wallhaven.cc/full/w5/wallhaven-w56w5x.png',
    'public/assets/2k/bocchi_overdrive_4k.jpg': 'https://w.wallhaven.cc/full/rq/wallhaven-rqqegj.jpg',
    'public/assets/2k/kessoku_live_banner_3k.png': 'https://w.wallhaven.cc/full/1q/wallhaven-1qq259.png',
    'public/assets/2k/bocchi_poster_5k.jpg': 'https://w.wallhaven.cc/full/rr/wallhaven-rrdgp1.jpg'
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

for local, remote in wallpapers.items():
    try:
        print(f"Downloading {local}...")
        req = urllib.request.Request(remote, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
            with open(local, 'wb') as f:
                f.write(data)
            print(f"-> Saved {local} ({len(data)} bytes)")
    except Exception as e:
        print(f"-> Failed {local}: {e}")
