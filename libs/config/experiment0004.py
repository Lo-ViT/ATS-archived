#!/usr/bin/env python3
from pathlib import Path
from libs.utils.date import get_time_stamp
"""Add custom configs and default values"""
import wandb

def add_custom_config(_C):
    # Experiment's name
    experiment_name = f"0004-{get_time_stamp()}"
    
    # Initialize wandb's meta-data
    # You properly don't need to change this
    home = str(Path.home())
    _C.OUTPUT_DIR =  f"{home}/efficient-transformer-data/output/{experiment_name}"
    _C.EXPERIMENT_NAME = experiment_name
    if _C.WANDB.ENABLE:
        wandb.init(
            # set the wandb project where this run will be logged
            project=f"Train TinyImageNet",
            name=experiment_name
        )
    
    # Change your hyper-parameters here if needed
    _C.TRAIN.EVAL_PERIOD = 1
    return _C