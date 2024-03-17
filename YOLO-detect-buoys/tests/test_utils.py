"""
Module for the utility functions.
"""

from torch import cuda, device
from utils import get_device


def test_get_device() -> None:
    """
    Test the get_device function.
    """
    expected_device = (
        device(device="cuda") if cuda.is_available() else device(device="cpu")
    )
    assert get_device() == expected_device
