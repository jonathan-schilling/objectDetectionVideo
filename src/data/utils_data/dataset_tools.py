"""
Functions that are needed to build a dataset.

by Jonathan Schilling
"""

import os
import random
import shutil
import math

from textwrap import dedent

from src import paths as p


def validate_label_file_input(label_file):
    """
    Validates name of the label file from user input.

    :param label_file: String containing the name of the label file
    :return: None
    """

    if str(label_file).endswith('.json'):
        label_file = label_file[:-5]

    if not label_file:
        print('Specify label file, please!')
        print(f'The label file has to be saved in {p.DATA_BASE_DIR / p.LABEL_DIR}')
        exit(1)

    if not os.path.exists(p.DATA_BASE_DIR / p.LABEL_DIR / (label_file + p.LABEL_FORMAT)):
        print(f'Label file {label_file}{p.LABEL_FORMAT} doesn\'t exist.')
        print(f'The label file has to be saved in {p.DATA_BASE_DIR / p.LABEL_DIR}')
        exit(1)


def init_dataset_structure(label_file):
    """
    Initializes datastructure of the new dataset.

    :param label_file: String containing the name of the label file
    :return: None
    """

    if not os.path.exists(p.DATA_BASE_DIR / p.DATASET_DIR / f'ds_{label_file}'):
        os.makedirs(p.DATA_BASE_DIR / p.DATASET_DIR / f'ds_{label_file}')

        os.makedirs(p.DATA_BASE_DIR / p.DATASET_DIR / f'ds_{label_file}' / label_file)
        os.makedirs(p.DATA_BASE_DIR / p.DATASET_DIR / f'ds_{label_file}' / label_file / 'images')
        os.makedirs(p.DATA_BASE_DIR / p.DATASET_DIR / f'ds_{label_file}' / label_file / 'labels')
        os.makedirs(p.DATA_BASE_DIR / p.DATASET_DIR / f'ds_{label_file}' / label_file / 'data_splits')

        shutil.copy(p.DATA_BASE_DIR / p.LABEL_DIR / 'assets' / 'classes.txt',
                    p.DATA_BASE_DIR / p.DATASET_DIR / f'ds_{label_file}' / label_file / 'classes.txt')
        shutil.copy(p.DATA_BASE_DIR / p.LABEL_DIR / 'assets' / 'notes.json',
                    p.DATA_BASE_DIR / p.DATASET_DIR / f'ds_{label_file}' / label_file / 'notes.json')
    else:
        print(f'Dataset {label_file} already was built.')
        print(f'It is saved in {p.DATA_BASE_DIR / p.DATASET_DIR / ("ds_" + label_file)}')
        exit(1)


def create_split(label_file, seed, train_p=0.8, val_p=0.1, test_p=0.1):
    """
    Create a train/validation/test split for the dataset.

    :param label_file: String containing the name of the label file
    :param seed: Seed for shuffle function
    :param train_p: Percentage of images allocated for training
    :param val_p: Percentage of images allocated for validation
    :param test_p: Percentage of images allocated for testing
    :return: None
    """

    ds_base_path = p.DATA_BASE_DIR / p.DATASET_DIR / f'ds_{label_file}' / label_file

    imgs_files = [str(i) for i in os.listdir(ds_base_path / 'images') if i.endswith(p.IMAGE_FORMAT)]
    imgs = [((ds_base_path / 'images').as_posix() + '/') + sub for sub in imgs_files]
    random.Random(seed).shuffle(imgs)

    num_train_imgs = math.ceil(len(imgs)*train_p)
    num_val_imgs = math.ceil(len(imgs) * val_p)
    num_test_imgs = math.ceil(len(imgs) * test_p)

    # create splits from shuffled file names
    imgs_train = imgs[:num_train_imgs]
    imgs_val = imgs[num_train_imgs:num_train_imgs+num_val_imgs]
    imgs_test = imgs[num_train_imgs+num_val_imgs:num_train_imgs+num_val_imgs+num_test_imgs]

    with open(ds_base_path / 'data_splits' / 'train.txt', 'w') as f_train:
        f_train.write('\n'.join(imgs_train))

    with open(ds_base_path / 'data_splits' / 'validation.txt', 'w') as f_validation:
        f_validation.write('\n'.join(imgs_val))

    with open(ds_base_path / 'data_splits' / 'test.txt', 'w') as f_test:
        f_test.write('\n'.join(imgs_test))


def create_ds_yaml(label_file):
    """
    Generate a YAML dataset description in YOLO format.

    :param label_file: String containing the name of the label file
    :return: None
    """

    path = p.DATA_BASE_DIR / p.DATASET_DIR / f'ds_{label_file}' / label_file

    description = f"""
    # {label_file.upper()} dataset
    
    path: {str(path.as_posix())}
    
    # Data split
    train: data_splits/train.txt
    val: data_splits/validation.txt
    test: data_splits/test.txt
    
    # Classes
    names:
      0: attacker
      1: defender
    """

    with open(p.DATA_BASE_DIR / p.DATASET_DIR / f'ds_{label_file}' / f'{label_file}.yaml', 'w') as file:
        file.write(dedent(description))
