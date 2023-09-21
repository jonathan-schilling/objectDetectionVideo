"""
Collection of needed paths

by Jonathan Schilling
"""

from pathlib import Path


DATA_BASE_DIR = Path('C:/Users/Jonathan/Documents/Development/git/gitlab/projectpr/data')

# list of processed maps
MAPS = ['ascent', 'haven', 'split']


VIDEO_DIR = Path('raw/videos_raw')
FRAME_DIR = Path('interim/frames')
CROP_DIR = Path('interim/crops')
LABEL_DIR = Path('interim/labels')
DATASET_DIR = Path('processed')

VIDEO_FORMAT = '.mp4'
IMAGE_FORMAT = '.jpg'
LABEL_FORMAT = '.json'
