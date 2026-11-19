// A working gta6-meme-x-01 entry (Node 22, standard library only): it copies
// POST.json and meme.png from the repository root to /output/POST.json and
// /output/meme.png. The entry is the post itself: the meme is posted on X from
// a public account with make.fun (a link or written out) and/or a tag of
// @makefunai and the entrant's play code in its text, POST.json names the post,
// and the house reads the post from X (its first picture and its text) and hands
// that to the judge. Nothing this program writes about the post is judged.
//
// The POST.json this repository ships holds a placeholder address, so the gate
// refuses it as it stands (valid 0). Replace it with the post's address before
// you submit.
//
// Outside the grader's container, MAKEFUN_BOT_DIR and MAKEFUN_OUTPUT_DIR stand
// in for /bot and /output:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, readFileSync, statSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

mkdirSync(OUTPUT_DIR, { recursive: true });
for (const file of ['POST.json', 'meme.png']) {
  try {
    copyFileSync(join(BOT_DIR, file), join(OUTPUT_DIR, file));
  } catch (err) {
    console.error(`${file} could not be copied from ${BOT_DIR}: ${(err as Error).message}`);
    process.exit(1);
  }
}

// Confirm the run produced both files, so a silent failure can never pass
// for a success. The gate reads POST.json; meme.png is the same picture the
// post carries, kept beside it for the record.
const postBytes = statSync(join(OUTPUT_DIR, 'POST.json')).size;
const memeBytes = statSync(join(OUTPUT_DIR, 'meme.png')).size;
// Validate the copied POST.json the way the gate will: a JSON object with a
// string url. A malformed POST.json must fail loudly here, not at the gate.
let post;
try {
  post = JSON.parse(readFileSync(join(OUTPUT_DIR, 'POST.json'), 'utf8'));
} catch (err) {
  console.error(`POST.json is not valid JSON: ${(err as Error).message}`);
  process.exit(1);
}
if (typeof post !== 'object' || post === null || typeof post.url !== 'string') {
  console.error('POST.json must be a JSON object with a string "url" field');
  process.exit(1);
}
if (post.url.includes('<handle>')) {
  console.error('warning: POST.json still holds the placeholder address; replace it with the real post address before submitting');
}
console.log(`wrote ${join(OUTPUT_DIR, 'POST.json')} (${postBytes} bytes) and ${join(OUTPUT_DIR, 'meme.png')} (${memeBytes} bytes)`);
