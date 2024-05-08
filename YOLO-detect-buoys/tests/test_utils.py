"""
Module for the utility functions.
"""

from os import getcwd

from dotenv import load_dotenv
from torch import cuda, device
from utils import get_data, get_device


def test_get_device() -> None:
    """
    Test the get_device function.
    This makes sure that if the function is changed, the tests verifies that
    the function returns the expected device.
    """
    expected_device = (
        device(device="cuda") if cuda.is_available() else device(device="cpu")
    )
    assert get_device() == expected_device


def test_get_data() -> None:
    """
    Test the get_data function.
    This makes sure that if the function is changed, the tests verifies that
    the function returns the expected dataset location.
    """
    load_dotenv()

    location_, name_, version_ = get_data("football-players-detection", 1)

    assert location_ == getcwd() + "\\" + name_.replace(" ", "-") + "-" + str(
        version_
    ), "The dataset location is not correct."
