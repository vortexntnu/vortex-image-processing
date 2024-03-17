from torch import device


def get_device() -> device:
    """
    Get the device to use for training and inference.

    Returns:
        torch.device: The device to use for training and inference.
    """
    from torch import cuda

    return device(device="cuda" if cuda.is_available() else "cpu")
