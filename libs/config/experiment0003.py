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
            name="Experiment 0003"
        )
    
    # Change your hyper-parameters here if needed
    _C.TRAIN.EVAL_PERIOD = 1
    return _C