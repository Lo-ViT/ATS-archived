from torchvision import datasets, transforms
from fvcore.common.registry import Registry

DATASET_REGISTRY = Registry("DATASET")
DATASET_REGISTRY.__doc__ = """
Registry for dataset.

The registered object will be called with `obj(cfg, split)`.
The call should return a `torch.utils.data.Dataset` object.
"""

def build_dataset(dataset_name, cfg, split):
    """
    Build a dataset, defined by `dataset_name`.
    Args:
        dataset_name (str): the name of the dataset to be constructed.
        cfg (CfgNode): configs. Details can be found in libs/config/defaults.py
        split (str): the split of the data loader. Options include `train`, `val`, and `test`.
    Returns:
        Dataset: a constructed dataset specified by dataset_name.
    """
    name = dataset_name
    
    # Define the path to the dataset directory
    data_dir = cfg.DATA.PATH_TO_DATA_DIR
    
    # Initialize the dataset based on the dataset name
    if name.lower() == 'tinyimagenet':
        assert cfg.DATA.TRAIN_CROP_SIZE == cfg.DATA.TEST_CROP_SIZE == cfg.VIT.IMG_SIZE, "Train and test crop size must be equal."
        if split in ['train', 'val', 'test']:
            dataset_path = f"{data_dir}/{split}"
            dataset = datasets.ImageFolder(dataset_path, transform=transforms.Compose([
            transforms.Resize((cfg.DATA.TRAIN_CROP_SIZE, cfg.DATA.TRAIN_CROP_SIZE)),
            transforms.ToTensor(),
        ]))
        else:
            raise ValueError(f"Invalid split: {split}. Expected one of: 'train', 'val', 'test'.")
        return dataset
    else:
        return DATASET_REGISTRY.get(name)(cfg=cfg, split=split)