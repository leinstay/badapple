# Bad Apple

Python script that plays a video as ASCII art in the terminal, frame by frame, with the audio track alongside. It was made for the Bad Apple!! shadow video but works with any monochrome video. Every block of pixels becomes one character chosen by brightness, and a sync multiplier keeps the frames in step with the sound.

[![Bad Apple in the console](https://user-images.githubusercontent.com/8215580/203308975-2af88779-73fa-477d-9b1f-64e264eb1311.png)](https://youtu.be/omi5VWlpfOs)

## Requirements

Python 3.8 or newer and FFmpeg, which moviepy uses to read the video and extract the audio. On Windows the `windows-curses` package from `requirements.txt` provides curses.

## Installation

```bash
git clone https://github.com/leinstay/badapple.git
cd badapple
pip install -r requirements.txt
```

## Usage

```bash
python pyapple.py
```

The script reads `config.json`, extracts the audio from the video into `audio_source` on the first run, and plays in the current console window. Make the window large enough for `width / chunk_size_x` columns and `height / chunk_size_y` rows.

## Configuration

All options live in `config.json`.

| Key | Default | Meaning |
|---|---|---|
| `video_source` | `ba.mp4` | Input video. Its resolution must be divisible by the chunk size |
| `audio_source` | `ba.mp3` | Audio file, extracted from the video if missing |
| `chunk_size_x` | `6` | Width of the pixel block that becomes one character |
| `chunk_size_y` | `10` | Height of that block |
| `illumination_level` | `2` | Number of brightness levels, 2, 3, 5 or 9 |
| `illumination_characters` | `["💀", "🍎"]` | One character per level, dark to light |
| `sync_multiplier` | `1.18` | Must be above 1. Raise it if the video falls more than a second behind the audio |

## License and credits

MIT License, see [LICENCE](LICENCE).

* Bad Apple!! shadow art video by Anira (<https://www.nicovideo.jp/watch/sm8628149>), bundled as `ba.mp4` for demonstration. Rights belong to the author.
* [moviepy](https://github.com/Zulko/moviepy): MIT License
