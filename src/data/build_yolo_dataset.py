"""
Builds dataset in YOLO format.

by Jonathan Schilling
"""

import os
import shutil
import json
import re

from src import paths as p
from src import constants as c
from src.data.utils_data import dataset_tools as ds_tools


SEED = 12


label_file = input('Insert name of label file, please! ')
ds_base = p.DATA_BASE_DIR / p.DATASET_DIR / f'ds_{label_file}'


# Pre-check
ds_tools.validate_label_file_input(label_file)

# Preparation
ds_tools.init_dataset_structure(label_file)


# Converting
with open(p.DATA_BASE_DIR / p.LABEL_DIR / (label_file + p.LABEL_FORMAT)) as input_labels:
    parsed_json = json.load(input_labels)

for img_lbl in parsed_json:
    img = re.findall('%5C([a-z]+_frame_[0-9]+).jpg', img_lbl['image'])[0]
    map_name = re.findall('([a-z]+)_frame_[0-9]+', img)[0]
    keypoints = img_lbl['kp']

    lbl_file = open(ds_base / label_file / 'labels' / (img + '.txt'), 'w')

    for point in keypoints:
        x = point['x']
        y = point['y']
        label = c.LBL_ATT['id'] if point['keypointlabels'][0] == c.LBL_ATT['name'] else c.LBL_DEF['id']

        x_yolo = x / 100.0
        y_yolo = y / 100.0

        lbl_file.write(f'{label} {x_yolo} {y_yolo} {c.SQUARE_SIZE} {c.SQUARE_SIZE}\n')

    lbl_file.close()

    shutil.copy(p.DATA_BASE_DIR / p.CROP_DIR / map_name / (img + p.IMAGE_FORMAT),
                ds_base / label_file / 'images' / (img + p.IMAGE_FORMAT))


# Create train/validation/test split
ds_tools.create_split(label_file, SEED, train_p=0.8, val_p=0.15, test_p=0.5)

# Create dataset description
ds_tools.create_ds_yaml(label_file)

# Cleanup
shutil.copy(p.DATA_BASE_DIR / p.LABEL_DIR / (label_file + p.LABEL_FORMAT),
            ds_base / (label_file + p.LABEL_FORMAT))
os.remove(p.DATA_BASE_DIR / p.LABEL_DIR / (label_file + p.LABEL_FORMAT))
