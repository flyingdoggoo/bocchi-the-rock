import sharp from 'sharp';
import fs from 'fs';

const files = [
  'still_ep08_4.jpg',
  'still_ep10_1.jpg',
  'still_ep10_2.jpg',
  'still_ep10_3.jpg',
  'still_ep10_4.jpg',
  'still_ep11_4.jpg'
];

for (const file of files) {
  const p = `public/assets/gallery/${file}`;
  if (fs.existsSync(p)) {
    const meta = await sharp(p).metadata();
    console.log(`${file}: ${meta.width}x${meta.height}, format: ${meta.format}`);
    const out = `public/assets/gallery/preview_${file}`;
    await sharp(p)
      .resize({ width: 500, height: 500, fit: 'inside' })
      .jpeg({ quality: 80 })
      .toFile(out);
  }
}
