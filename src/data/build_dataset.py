"""
Creates dataset in YOLO format

by Jonathan Schilling
"""

import os
import shutil
import json
import re
import zipfile

from src import paths as p
from src import constants as c
import zip_dataset as zip


label_file = 'dataset_test'

# pre-checks
if not label_file:
    print('Specify label file, please!')
    print(f'The label file has to be saved in {p.DATA_BASE_DIR / p.LABEL_DIR}')
    exit(1)

if not os.path.exists(p.DATA_BASE_DIR / p.LABEL_DIR / (label_file + p.LABEL_FORMAT)):
    print(f'Label file {label_file}{p.LABEL_FORMAT} doesn\'t exist.')
    print(f'The label file has to be saved in {p.DATA_BASE_DIR / p.LABEL_DIR}')
    exit(1)

# preparation
if not os.path.exists(p.DATA_BASE_DIR / p.LABEL_DIR / 'tmp'):
    os.makedirs(p.DATA_BASE_DIR / p.LABEL_DIR / 'tmp')
    os.makedirs(p.DATA_BASE_DIR / p.LABEL_DIR / 'tmp' / 'images')
    os.makedirs(p.DATA_BASE_DIR / p.LABEL_DIR / 'tmp' / 'labels')

    shutil.copy(p.DATA_BASE_DIR / p.LABEL_DIR / 'assets' / 'classes.txt',
                p.DATA_BASE_DIR / p.LABEL_DIR / 'tmp' / 'classes.txt')
    shutil.copy(p.DATA_BASE_DIR / p.LABEL_DIR / 'assets' / 'notes.json',
                p.DATA_BASE_DIR / p.LABEL_DIR / 'tmp' / 'notes.json')
else:
    print('Delete folder \"' + str(p.DATA_BASE_DIR / p.LABEL_DIR / 'tmp') + '\", please!')
    exit(1)

# converting
with open(p.DATA_BASE_DIR / p.LABEL_DIR / (label_file + p.LABEL_FORMAT)) as input_labels:
    parsed_json = json.load(input_labels)

for img_lbl in parsed_json:
    img = re.findall('%5C([a-z]+_frame_[0-9]+).jpg', img_lbl['image'])[0]
    keypoints = img_lbl['kp']

    lbl_file = open(p.DATA_BASE_DIR / p.LABEL_DIR / 'tmp' / 'labels' / (img + '.txt'), 'w')

    for point in keypoints:
        x = point['x']
        y = point['y']
        label = c.LBL_ATT['id'] if point['keypointlabels'][0] == c.LBL_ATT['name'] else c.LBL_DEF['id']

        x_yolo = x / 100.0
        y_yolo = y / 100.0

        lbl_file.write(f'{label} {x_yolo} {y_yolo} {c.SQUARE_SIZE} {c.SQUARE_SIZE}\n')

    lbl_file.close()

    shutil.copy(p.DATA_BASE_DIR / p.CROP_DIR / 'ascent' / (img + p.IMAGE_FORMAT),
                p.DATA_BASE_DIR / p.LABEL_DIR / 'tmp' / 'images' / (img + p.IMAGE_FORMAT))

    path_zip = p.DATA_BASE_DIR / p.DATASET_DIR / (label_file + '.zip')
    with (zipfile.ZipFile(path_zip, 'w', zipfile.ZIP_DEFLATED) as zipf):
        zip.zip_dataset(p.DATA_BASE_DIR / p.LABEL_DIR / 'tmp', zipf)

# cleanup
shutil.copy(p.DATA_BASE_DIR / p.LABEL_DIR / (label_file + p.LABEL_FORMAT),
                p.DATA_BASE_DIR / p.DATASET_DIR / (label_file + p.LABEL_FORMAT))
os.remove(p.DATA_BASE_DIR / p.LABEL_DIR / (label_file + p.LABEL_FORMAT))
if os.path.exists(p.DATA_BASE_DIR / p.LABEL_DIR / 'tmp'):
    shutil.rmtree(p.DATA_BASE_DIR / p.LABEL_DIR / 'tmp')
