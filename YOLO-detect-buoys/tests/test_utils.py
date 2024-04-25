"""
Module for the utility functions.
"""

from unittest.mock import Mock, patch

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
    with patch("os.getenv") as mock_getenv:
        mock_getenv.return_value = "ROBOFLOW_API_KEY"
        with patch("roboflow.Roboflow") as mock_roboflow:
            mock_roboflow.return_value = Mock()
            mock_roboflow.return_value.workspace.return_value = Mock()
            mock_roboflow.return_value.workspace.return_value.project.return_value = (
                Mock()
            )
            mock_roboflow.return_value.workspace.return_value.project.return_value.version.return_value = (
                Mock()
            )
            mock_roboflow.return_value.workspace.return_value.project.return_value.version.return_value.download.return_value = (
                Mock()
            )
            mock_roboflow.return_value.workspace.return_value.project.return_value.version.return_value.download.return_value.location = (
                "https://example.com"
            )
            assert get_data("project_id", 1) == "https://example.com"
