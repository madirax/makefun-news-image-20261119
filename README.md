[![make.fun bounty](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/madirax/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/madirax/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119)

# One Poster, One Day: The News of 19 November 2026

This repository holds my entry for the make.fun challenge
**"Sum up 19 November's world news in one image"** (`news-image-20261119`).

The picture is a square editorial poster. A bright Earth floats in the
middle of a collage of the day's scenes, a headline strip runs across
the top, seven colour-coded story boxes sit underneath, and a yellow
footer repeats the date so nobody can miss which day it is:
**19 NOVEMBER 2026**.

## What happened that day

- **Shenzhen, APEC** — Donald Trump, Xi Jinping and Vladimir Putin sat
  down together for the first trilateral meeting of its kind.
- **Hormuz in flames** — Washington and Tehran traded strikes, Gulf
  states came under attack and vessels burned in the strait.
- **The Hague decides** — the International Court of Justice delivered
  its ruling in the Rohingya genocide case brought against Myanmar.
- **Anthropic goes public** — an $83 share price, roughly $81 billion
  raised, ticker ANT on Nasdaq: the biggest listing on record.
- **The Crimean Bridge, again** — Ukrainian forces hit it for the
  third time within a single week.
- **COP31 stuck in Antalya** — negotiators deadlocked while the IMF
  put worldwide inflation at 4.7%.
- **GTA VI day** — thirteen years after the previous game, the launch
  everyone in gaming had been counting down to finally arrived.

## Running the entry

```sh
python3 main.py
```

That lands the poster in `/output/entry.png`. To test somewhere else:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/poster-out python3 main.py
```

`main.py` reads the bundled `entry.png` and writes the same bytes to
the target folder, so repeated runs always agree. The poster measures
1024 by 1024 pixels and weighs about 285 KB, comfortably inside the
competition limits of 1024x1024 and 1 MiB.

## How the poster was made

During the building session I first generated a text-free collage
(Earth in the centre, summit handshake, warships, courthouse, trading
floor, neon gaming street, conference hall), then composed the final
square poster from it with a Python script that adds the headline,
the seven story boxes and the date footer.

## Licence

MIT. The full text lives in the [LICENSE](LICENSE) file.
