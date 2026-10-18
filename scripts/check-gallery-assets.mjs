import sharp from 'sharp';
import fs from 'fs';

const files = [
  'bocchi_shred_guitar_2k.png',
  'bocchi_guitar_solo_2k.png',
  'bocchi_overdrive_4k.jpg',
  'bocchi_poster_5k.jpg',
  'bocchi_stage_solo_4k.jpg',
  'kessoku_band_6k.jpg',
  'kessoku_squad_4k.jpg',
  'kessoku_art_7k.jpg'
];

for (const file of files) {
  const p = `public/assets/2k/${file}`;
  if (fs.existsSync(p)) {
    const out = `public/assets/2k/gallery_check_${file.replace(/\.[^.]+$/, '')}.jpg`;
    await sharp(p)
      .resize({ width: 500, height: 500, fit: 'inside' })
      .jpeg({ quality: 75 })
      .toFile(out);
    console.log(`Generated: ${out}`);
  }
}
