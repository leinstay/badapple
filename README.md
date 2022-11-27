# Bad apple

A python script that transforms a video file into ASCII graphics frame by frame and outputs it directly to the console.
Script can be used for any monochrome video. All options are set via config file.

[![Bad apple](https://user-images.githubusercontent.com/8215580/203308975-2af88779-73fa-477d-9b1f-64e264eb1311.png)](https://youtu.be/omi5VWlpfOs)

Config:

```json
{
    "chunk_size_x": 6, // width of single character in px;
    "chunk_size_y": 10, // height of single character in px;
    "sync_multiplier": 1.18, // must be > 1, raise this parameter if the video is desynchronized by more than one second;
    "illumination_level": 2, // the number of characters used, where the first is for black, the last for white, 
                                        and the intermediate for the shades of gray in between;
    "illumination_characters": [
        "💀",
        "🍎"
    ],
    "video_source": "ba.mp4", // source video file to parse;
    "audio_source": "ba.mp3" //source audio file to use, if it is missing, 
                                        this option will be used as the name for the audio track taken from the video;
}
```
