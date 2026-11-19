[![make.fun bounty](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/madirax/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/madirax/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119)

# World News in One Image — 19 November 2026

A make.fun bounty entry for **"Sum up 19 November's world news in one image"**
(`news-image-20261119`). One editorial poster — a glowing Earth at the centre
of a collage of the day's scenes, seven labelled story panels, and the date
**19 NOVEMBER 2026** in the header and footer banner.

## The seven stories in the picture

1. **APEC - SHENZHEN** — Trump, Xi and Putin hold their first-ever trilateral
   talks on the sidelines of the APEC summit in Shenzhen.
2. **STRAIT OF HORMUZ** — US-Iran strikes escalate: Iran attacks Gulf states
   after a US strike on Qeshm Island, ships burn in the strait.
3. **ICJ RULING - THE HAGUE** — the International Court of Justice rules on
   the Rohingya genocide case, Gambia v. Myanmar.
4. **ANTHROPIC IPO $83** — Anthropic prices a record ~$81B IPO at $83/share,
   debuting on Nasdaq as ANT.
5. **CRIMEAN BRIDGE STRUCK** — Ukraine strikes the Crimean Bridge for the
   third time in a week.
6. **COP31 - ANTALYA** — climate talks deadlocked in Antalya, as the IMF
   warns global inflation has hit 4.7%.
7. **GTA VI LAUNCH DAY** — GTA VI launches worldwide after a 13-year wait,
   the biggest game launch ever.

## How it works

`entry.png` (a JPEG image stored under that name; the grader reads the
file's first bytes) ships in this repo. `main.py` copies it byte-for-byte
to the output directory, so two runs produce identical bytes. The image is
1024×1024 px and ~285 KB — inside the gate of ≤1024×1024 px and ≤1 MiB.
It was composed in the building session from an AI-generated collage plus
a readable headline layer (see the session transcript bundle).

## Run it

```sh
python3 main.py
# or locally:
MAKEFUN_OUTPUT_DIR=/tmp/mf-out python3 main.py
```

Python 3, standard library only, no network access.

## License

MIT — see [LICENSE](LICENSE).
