"""
Collection of needed paths.

by Jonathan Schilling
"""

from pathlib import Path

# Define the base directory for data storage
DATA_BASE_DIR = Path('C:/Users/Jonathan/Documents/Development/git/gitlab/projectpr/data')

# List of processed maps
MAPS = ['ascent', 'haven', 'split']


# Directory paths for different data stages
VIDEO_DIR = Path('raw/videos_raw')      # Directory containing raw video files
FRAME_DIR = Path('interim/frames')      # Directory for frames captured from videos
CROP_DIR = Path('interim/crops')        # Directory for storing cropped maps obtained from frames
LABEL_DIR = Path('interim/labels')      # Directory for storing unprocessed label data
DATASET_DIR = Path('processed')         # Directory for finished datasets

# File formats
VIDEO_FORMAT = '.mp4'
IMAGE_FORMAT = '.jpg'
LABEL_FORMAT = '.json'
