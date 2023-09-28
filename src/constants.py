"""
Collection of Constants.

by Jonathan Schilling
"""

# Side length of cropped images (square)
SIDE_LENGTH = 384

# Coordinates of the upper left corner per map (x, y) for cropping
MAP_COORDS = {
    'ascent': {'x': 48, 'y': 36},
    'haven': {'x': 36, 'y': 36},
    'split': {'x': 32, 'y': 32}
}


# Side length of label square in percentage of image size (YOLO format)
SQUARE_SIZE = 0.053

# Label id and name
LBL_ATT = {'id': 0, 'name': 'attacker'}
LBL_DEF = {'id': 1, 'name': 'defender'}
