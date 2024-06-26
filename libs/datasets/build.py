from fvcore.common.registry import Registry
from libs.datasets.tinyimagenet import build_tinyimagenet
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
    # Initialize the dataset based on the dataset name
    if name.lower() == 'tinyimagenet':
        return build_tinyimagenet(cfg=cfg, split=split)
    else:
        return DATASET_REGISTRY.get(name)(cfg=cfg, split=split)