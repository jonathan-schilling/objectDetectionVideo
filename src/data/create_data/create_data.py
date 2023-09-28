"""
Create raw frames from videos.

by Jonathan Schilling
"""

import os

from src import paths as p
from src.data.utils_data import video2frames as vtools


if not os.path.exists(p.DATA_BASE_DIR / p.FRAME_DIR):
    os.makedirs(p.DATA_BASE_DIR / p.FRAME_DIR)

log_file = open(p.DATA_BASE_DIR / p.FRAME_DIR / 'log.txt', 'w')

# create output folders
for m in p.MAPS:
    path = p.DATA_BASE_DIR / p.FRAME_DIR / m
    if not os.path.exists(path):
        os.makedirs(path)
        log_file.write(f'Created directory: {path}\n')
        print(f'Created directory: {path}')

log_file.write('\n')

# create data from videos in DATA_BASE_DIR/VIDEO_DIR/<map>
for m in p.MAPS:
    path = p.DATA_BASE_DIR / p.VIDEO_DIR / m
    files_mp4 = [i[:-4] for i in os.listdir(path) if i.endswith(p.VIDEO_FORMAT)]

    next_frame_name = 0
    total_saved_frames = 0

    for v in files_mp4:
        (frame_name, saved_frames, log) = vtools.video2frames(m, v, next_frame_name)
        next_frame_name = frame_name
        total_saved_frames += saved_frames
        log_file.write(f'{log}\n')

    print(f"Map: {m}, totalSavedFrames: {total_saved_frames}")
    log_file.write(f'Map: {m}, totalSavedFrames: {total_saved_frames}\n')
    log_file.write('\n')

log_file.close()
