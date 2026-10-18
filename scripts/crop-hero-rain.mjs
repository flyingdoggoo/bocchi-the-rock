import sharp from 'sharp';

// 8g5yr2 is 3508 x 2050
// Bocchi is in left-center: x: 350 to 2050, y: 0 to 2050 (1700 wide, 2050 high)
await sharp('public/assets/downloads/8g5yr2.jpg')
  .extract({ left: 320, top: 0, width: 1700, height: 2050 })
  .resize(1400, 1680)
  .webp({ quality: 92 })
  .toFile('public/assets/2k/hero_bocchi_rain_lespaul.webp');

console.log('Generated hero_bocchi_rain_lespaul.webp');
