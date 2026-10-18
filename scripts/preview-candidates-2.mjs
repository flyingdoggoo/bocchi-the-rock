import sharp from 'sharp';
import fs from 'fs';

const files = [
  'bocchi_guitarist_crop.png',
  'kessoku_live_banner_3k.png',
  'kessoku_band_walk_2k.png',
  'kessoku_band_stage_4k.jpg'
];

for (const file of files) {
  const p = `public/assets/2k/${file}`;
  if (fs.existsSync(p)) {
    const out = `public/assets/2k/preview_${file.replace(/\.[^.]+$/, '')}.jpg`;
    await sharp(p)
      .resize({ width: 600, height: 600, fit: 'inside' })
      .jpeg({ quality: 80 })
      .toFile(out);
    console.log(`Generated preview: ${out}`);
  }
}
