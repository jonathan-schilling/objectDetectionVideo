"""
Crop frames onto maps.

by Jonathan Schilling
"""

import cv2
import os

from src import paths as p
from src import constants as c


if not os.path.exists(p.DATA_BASE_DIR / p.CROP_DIR):
    os.makedirs(p.DATA_BASE_DIR / p.CROP_DIR)
    print('Created directory: ' + str(p.DATA_BASE_DIR / p.CROP_DIR))

for m in p.MAPS:
    if not os.path.exists(p.DATA_BASE_DIR / p.CROP_DIR / m):
        os.makedirs(p.DATA_BASE_DIR / p.CROP_DIR / m)
        print('Created directory: ' + str(p.DATA_BASE_DIR / p.CROP_DIR / m))

    files = os.listdir(p.DATA_BASE_DIR / p.FRAME_DIR / m)
    files_jpg = [i[:-4] for i in files if i.endswith(p.IMAGE_FORMAT)]

    for f in files_jpg:
        img = cv2.imread(str(p.DATA_BASE_DIR / p.FRAME_DIR / m / (f + p.IMAGE_FORMAT)))
        img_crop = img[c.MAP_COORDS[m]['y']:c.MAP_COORDS[m]['y']+c.SIDE_LENGTH,
                        c.MAP_COORDS[m]['x']:c.MAP_COORDS[m]['x']+c.SIDE_LENGTH]
        cv2.imwrite(str(p.DATA_BASE_DIR / p.CROP_DIR / m / (m + '_' + f + p.IMAGE_FORMAT)), img_crop)
