#!/usr/bin/env python3
from pathlib import Path
"""Add custom configs and default values"""
import wandb

def add_custom_config(_C):
    # Initialize wandb's meta data
    if _C.WANDB.ENABLE:
        wandb.init(
            # set the wandb project where this run will be logged
            project="Train TinyImageNet",
            name="Experiment 0004"
        )
    
    # Change your hyper-parameters here if needed
    _C.TRAIN.EVAL_PERIOD = 1
    _C.TEST.BATCH_SIZE = 1024
    _C.TRAIN.AUTO_RESUME = False
    return _C