import sharp from 'sharp';
import fs from 'fs';

const files = [
  'bocchi_epic_solo_5k.jpg',
  'bocchi_guitar_shred_4k.jpg',
  'bocchi_live_concert_4k.jpg',
  'hero_bocchi_7ppd69.jpg',
  'hero_bocchi_gpv8wl.png',
  'hero_bocchi_2yeem9.png',
  'hero_bocchi_2ymr79.png',
  'hero_bocchi_gp2q9q.jpg',
  'bocchi_stage_solo_4k.jpg',
  'kessoku_art_7k.jpg'
];

for (const file of files) {
  const p = `public/assets/2k/${file}`;
  if (fs.existsSync(p)) {
    const meta = await sharp(p).metadata();
    console.log(`${file}: ${meta.width}x${meta.height}, format: ${meta.format}`);
  }
}
