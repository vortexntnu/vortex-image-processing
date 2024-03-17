"""
This module provides a utility function to get the device to use for training and inference.
"""

from torch import device


def get_device() -> device:
    """
    Get the device to use for training and inference.
    https://stackoverflow.com/questions/48152674/how-do-i-check-if-pytorch-is-using-the-gpu

    Returns:
        torch.device: The device to use for training and inference.
    """
    from torch import cuda

    return device(device="cuda" if cuda.is_available() else "cpu")
