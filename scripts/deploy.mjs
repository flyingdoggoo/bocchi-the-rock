#!/usr/bin/env node
import { execSync } from 'child_process';
import { existsSync } from 'fs';

const BUCKET = 'bocchi.oguri-lab.io.vn';
const DISTRIBUTION_ID = 'ELRSMTSWUVT0X';
const PROFILE = 'leighk';
const REGION = 'ap-southeast-1';

console.log('🎸 [BOCCHI-DEPLOY] Starting optimized production deployment...');

// 1. Build
console.log('📦 [1/4] Building Vite production bundle...');
execSync('npm run build', { stdio: 'inherit' });

if (!existsSync('dist/index.html')) {
  console.error('❌ Build failed: dist/index.html not found');
  process.exit(1);
}

// 2. Sync hashed assets with 1-year immutable cache
console.log('⚡ [2/4] Syncing static assets with immutable cache headers...');
execSync(
  `aws s3 sync dist/ s3://${BUCKET} --profile ${PROFILE} --region ${REGION} --delete --exclude "index.html" --exclude "*.json" --cache-control "public, max-age=31536000, immutable"`,
  { stdio: 'inherit' }
);

// 3. Upload index.html and root metadata with no-cache revalidation
console.log('📄 [3/4] Uploading index.html with instant revalidation headers...');
execSync(
  `aws s3 cp dist/index.html s3://${BUCKET}/index.html --profile ${PROFILE} --region ${REGION} --cache-control "public, max-age=0, must-revalidate" --content-type "text/html; charset=utf-8"`,
  { stdio: 'inherit' }
);

// 4. Invalidate CloudFront edge cache
console.log('🚀 [4/4] Triggering CloudFront edge cache invalidation...');
const invOutput = execSync(
  `aws cloudfront create-invalidation --distribution-id ${DISTRIBUTION_ID} --paths "/*" --profile ${PROFILE} --output json`,
  { encoding: 'utf-8' }
);
const invData = JSON.parse(invOutput);
console.log(`✅ Cache invalidation submitted: ID ${invData.Invalidation?.Id || 'OK'}`);
console.log(`\n🎉 DEPLOYMENT COMPLETE!`);
console.log(`🌐 Live URL: https://bocchi.oguri-lab.io.vn`);
console.log(`📡 CloudFront: https://d1y4md4tyie8be.cloudfront.net`);
