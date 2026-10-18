import urllib.request
import re
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://bocchi.rocks/tv/story/'
}

os.makedirs('public/assets/gallery', exist_ok=True)

# Episodes 1, 4, 5, 8, 12
episodes = ['01', '04', '05', '08', '11', '12']

stills_to_download = []

for ep in episodes:
    url = f'https://bocchi.rocks/tv/story/?id={ep}'
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8')
            # Look for src="SYS/CONTENTS/..." or any img in story__content
            matches = re.findall(r'src="(SYS/CONTENTS/[^"]+)"', html)
            unique_matches = list(dict.fromkeys(matches))
            print(f"Episode {ep}: found {len(unique_matches)} stills")
            for idx, m in enumerate(unique_matches):
                full_url = f'https://bocchi.rocks/tv/story/{m}'
                local_file = f'public/assets/gallery/still_ep{ep}_{idx+1}.jpg'
                stills_to_download.append((local_file, full_url))
    except Exception as e:
        print(f"Error on ep {ep}:", e)

print(f"Total stills queued: {len(stills_to_download)}")

for local, remote in stills_to_download:
    try:
        req = urllib.request.Request(remote, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read()
            with open(local, 'wb') as f:
                f.write(data)
            print(f"Downloaded {local} ({len(data)} bytes)")
    except Exception as e:
        print(f"Failed {local}: {e}")
