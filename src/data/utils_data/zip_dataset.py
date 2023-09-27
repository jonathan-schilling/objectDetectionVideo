"""
Saves all files of a dataset in zip file

by Jonathan Schilling
"""

import os


def zip_dataset(path, zip_file):
    for root, dirs, files in os.walk(path):
        for file in files:
            src_path = root + '/' + file
            dest_path = root.replace(str(path), '') + '/' + file

            zip_file.write(src_path, dest_path)
