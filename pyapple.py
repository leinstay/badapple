import os
import json
import threading
import curses
import time

from playsound import playsound
from moviepy.editor import *

# Basic configuration
with open('config.json', 'r', encoding='utf-8') as cfg_file:
    config = json.load(cfg_file)

if config['sync_multiplier'] <= 0:
    raise Exception(
        "Config Error: Sync Multiplier must be greater than 0")

if config['illumination_level'] not in [2, 3, 5, 9]:
    raise Exception(
        "Config Error: Number of llumination levels must be set to 2, 3, 5 or 9")

clip = VideoFileClip(config['video_source'])

if clip.w % config['chunk_size_x'] != 0 or clip.h % config['chunk_size_y'] != 0:
    raise Exception(
        "Config Error: Video resolution must be divisible by Chunk Size")
else:
    sx = config['chunk_size_x']
    sy = config['chunk_size_y']

# Retrieving the audio track for later use
if not os.path.isfile(config['audio_source']):
    clip.audio.write_audiofile(config['audio_source'])


def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')


def sound():
    threading.Thread(target=playsound, args=(
        config['audio_source'],), daemon=True).start()


def illumination_to_ascii(illumination):
    # Illumination slice: number of pixels on X-asis * number of pixels on Y-asis * maximum RGB intensity (255*3) / number of levels
    islc = int(sx*sy*255*3/config['illumination_level'])
    for i in range(0, config['illumination_level']):
        if islc*(i) <= illumination <= islc*(i+1):
            return config['illumination_characters'][i]


try:
    sound()
    clear()

    console = curses.initscr()
    curses.noecho()

    frame_counter = 1
    video_duration = 0

    ex_video_start = time.time()

    for frame in clip.iter_frames():
        ex_frame_start = time.time()

        if frame_counter % clip.fps == 0:
            video_duration += 1000

        # Frame generation using illumination_to_ascii() function
        for y in range(0, int(clip.h/sy)):
            line = ""
            for x in range(0, int(clip.w/sx)):
                y1, y2, x1, x2 = sy*y, sy+sy*y, sx*x, sx+sx*x
                line += illumination_to_ascii(frame[y1:y2, x1:x2].sum())
                console.addstr(y, 0, line)
                console.noutrefresh()

        curses.doupdate()

        ex_frame_end = time.time()
        ascii_frame_duration = (ex_frame_end-ex_frame_start)*1000

        # Sync logic (~wait for next frame if you can)
        if ascii_frame_duration < video_duration:
            if ascii_frame_duration < 1000/clip.fps:
                curses.delay_output(
                    int((1000/clip.fps - ascii_frame_duration)/config['sync_multiplier']))

        ex_video_end = time.time()
        ascii_video_duration = int((ex_video_end-ex_video_start)*1000)
        desync = ascii_video_duration-video_duration

        frame_counter += 1
finally:
    curses.endwin()
