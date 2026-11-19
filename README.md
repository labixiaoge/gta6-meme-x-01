# Waited 13 Years for GTA 6

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/labixiaoge/gta6-meme-x-01/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/labixiaoge/gta6-meme-x-01/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

## About

A GTA 6 launch-week meme for the make.fun bounty "Post a GTA 6 meme on X".
The joke is the thirteen-year wait since GTA V: a skeleton slumps in a
cobwebbed gaming chair, controller still in hand, while the TV glows with a
sunny Vice City beach — and the make.fun ghost sits beside him, because while
he waited, his AI agent already got paid on make.fun.

The picture (`meme.png`, 1200 x 1200) is an AI-generated scene with the real
make.fun ghost mark from the press kit (https://make.fun/press/mark-1024.png)
worked into it, and captions drawn in large bold type so they stay readable
when the judge sees the picture shrunk to 480 x 480:

- Top: "WAITED 13 YEARS FOR GTA 6"
- Bottom: "MY AGENT ALREADY GOT PAID / ON MAKE.FUN"

The meme was built by `tools/make_meme.py` (run it again to rebuild
`meme.png` byte for byte from `assets/`); the base scene is
`assets/media-generation-base-scene-0-7d3a3f9a-24ad-414b-a08e-93d44f321dde.png`.

## The post is the entry

The post itself is the entry: post `meme.png` on X from the public account
@labixiaoge with the text below, then put the post's address in `POST.json`.
An AI judge compares the posts two at a time; the top 50 share $500
(1st $100, 2nd $60, 3rd $30, 4th–10th $10, 11th–50th $6).

Suggested post text (play code verified by the kit's check on 2026-11-20:
`makefun-jukebox-beret-bazaar`, code 0 of the account's 4 in this bounty;
any one of the four passes — `check --play-code 1` prints another):

> Waited 13 years for GTA 6. My agent already got paid on make.fun.
>
> On make.fun, you and your AI agents build things, win bounties and earn real money — this meme included.
>
> @makefunai https://make.fun/bounty/gta6-meme-x-01
> makefun-jukebox-beret-bazaar

Keep the post up and the account public until the results are out. Deadline:
2026-11-23 14:00 UTC (22:00 Beijing time).

## What is still missing before submission

- [ ] Post `meme.png` on X from @labixiaoge (public account) with the text
      above, including a real play code.
- [ ] Replace the placeholder in `POST.json` with the post's address:
      `{"url": "https://x.com/labixiaoge/status/<id>"}`
- [ ] Create the GitHub repository, push this commit, and submit with the
      kit CLI (see the kit's `RULES.txt`).

## How the program runs

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, standard library only, no network) copies `POST.json` and
`meme.png` into the output directory. Run it twice and the two outputs are
byte-identical.

Built for the make.fun bounty "Post a GTA 6 meme on X" —
https://make.fun/bounty/gta6-meme-x-01
