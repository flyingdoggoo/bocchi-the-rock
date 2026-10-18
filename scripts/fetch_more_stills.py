import urllib.request, re, os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://bocchi.rocks/tv/story/'
}

for ep in ['02', '03', '06', '07', '09', '10']:
    url = f'https://bocchi.rocks/tv/story/?id={ep}'
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8')
            matches = list(dict.fromkeys(re.findall(r'src="(SYS/CONTENTS/[^"]+)"', html)))
            for idx, m in enumerate(matches):
                remote = f'https://bocchi.rocks/tv/story/{m}'
                local = f'public/assets/gallery/still_ep{ep}_{idx+1}.jpg'
                with urllib.request.urlopen(urllib.request.Request(remote, headers=headers), timeout=10) as img_resp:
                    with open(local, 'wb') as f:
                        f.write(img_resp.read())
                print(f'Saved {local}')
    except Exception as e:
        print(f'Error ep {ep}:', e)
