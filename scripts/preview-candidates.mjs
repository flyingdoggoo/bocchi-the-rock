import sharp from 'sharp';
import fs from 'fs';

const files = [
  'hero_bocchi_7ppd69.jpg',
  'bocchi_epic_solo_5k.jpg',
  'bocchi_guitar_shred_4k.jpg',
  'bocchi_live_concert_4k.jpg',
  'hero_bocchi_gpv8wl.png',
  'hero_bocchi_2yeem9.png',
  'hero_bocchi_2ymr79.png',
  'hero_bocchi_gp2q9q.jpg'
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
