# Bad apple!!! but it's made of apples in VS Code terminal

Audio/video synchronization and frame parsing are handled in code on the fly. Script can be used for any monochrome video. Number of symbols per line, number and type of used symbols and syncronization options are set via config file.

Config:

```json
{
    "chunk_size_x": 6, // width of single character in px;
    "chunk_size_y": 10, // height of single character in px;
    "sync_multiplier": 1.18, // must be > 1, raise this parameter if the video is desynchronized by more than one second;
    "illumination_level": 2, // the number of characters used, where the first is for black, the last for white, and the intermediate for the shades of gray in between;
    "illumination_characters": [
        "💀",
        "🍎"
    ],
    "video_source": "ba.mp4", // source video file to parse;
    "audio_source": "ba.mp3" //source audio file to use, if it is missing, this option will be used as the name for the audio track taken from the video;
}
```

[![Bad apple](https://img.youtube.com/vi/omi5VWlpfOs/0.jpg)](https://youtu.be/omi5VWlpfOs)
