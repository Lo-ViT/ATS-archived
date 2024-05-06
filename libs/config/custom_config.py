#!/usr/bin/env python3
from pathlib import Path
"""Add custom configs and default values"""


def add_custom_config(_C):
    # Add your own customized configs.
    home = str(Path.home())
    _C.TRAIN.DATASET = "TinyImageNet"
    _C.TRAIN.BATCH_SIZE = 1024
    _C.OUTPUT_DIR = f"{home}/efficient-transformer-data/output"
    _C.VIT.NUM_CLASSES = 200
    _C.MODEL.NUM_CLASSES = 200
    _C.DATA.PATH_TO_DATA_DIR=f"{home}/efficient-transformer-data/tiny-imagenet-200"
    _C.TEST.DATASET="TinyImageNet"
    _C.DATA.TEST_CROP_SIZE=64
    _C.DATA.TRAIN_CROP_SIZE=64
    _C.DATA.MEAN=[0.485, 0.456, 0.406]
    _C.DATA.STD=[0.229, 0.224, 0.225]
    _C.VIT.IMG_SIZE=64
    _C.TEST.CHECKPOINT_FILE_PATH=f"{home}/efficient-transformer-data/models/default_custom_experiment_model.pth"
    return _C