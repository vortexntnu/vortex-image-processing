"""
Get data from Roboflow.
# Path: YOLO-detect-buoys/utils/get_device.py
"""

from os import getenv

from dotenv import load_dotenv
from roboflow import Roboflow


def get_data_roboflow(project_id: str, version_number: int):
    """
    Get data from Roboflow.
    Do not expose the API key in the code.
    """
    # import environment variables

    load_dotenv()

    rf = Roboflow(api_key=getenv("ROBOFLOW_API_KEY"))
    project = rf.workspace(the_workspace="roboflow-universe-projects").project(
        project_id=project_id
    )
    version = project.version(version_number=version_number)
    dataset = version.download(model_format="yolov8", overwrite=True, location="./data")

    return dataset.location, dataset.name, dataset.version


def get_data(*args, **kwargs):
    """
    Get data from Roboflow.

    Interface function for any method of getting data.
    """

    return get_data_roboflow(*args, **kwargs)
