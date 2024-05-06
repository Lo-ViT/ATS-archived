from torchvision import datasets, transforms

def build_tinyimagenet(cfg, split):
    """Build TinyImageNet.

    Args:
        cfg (CfgNode): Run's config.
        split (str): Data Split.
    Returns:
        Dataset: TinyImageNet dataset.
    """
    # Define the path to the dataset directory
    data_dir = cfg.DATA.PATH_TO_DATA_DIR
    assert cfg.DATA.TRAIN_CROP_SIZE == cfg.DATA.TEST_CROP_SIZE == cfg.VIT.IMG_SIZE, "Train and test crop size must be equal."
    if split in ['train', 'val', 'test']:
        dataset_path = f"{data_dir}/{split}"
        return datasets.ImageFolder(dataset_path, transform=transforms.Compose([
            transforms.Resize((cfg.DATA.TRAIN_CROP_SIZE, cfg.DATA.TRAIN_CROP_SIZE)),
            transforms.ToTensor(),
        ]))
    raise ValueError(f"Invalid split: {split}. Expected one of: 'train', 'val', 'test'.")