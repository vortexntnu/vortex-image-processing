"""
The main entry point for YOLO detecter buoys.
"""

from os import getcwd, path

from ultralytics import YOLO
from utils import get_data, get_device, process_video

if "__main__" == __name__:
    """
    The main entry point for YOLO detecter buoys.
    """

    device = get_device()
    model = YOLO("yolov8n.pt")

    file_path = path.abspath(getcwd())
    dataset_location = get_data("soccer-players-ckbru", 16)

    result = model.train(
        data=dataset_location + "\data.yaml", epochs=50, imgsz=640, device=device
    )

    model.val()

    process_video("https://youtu.be/4WGpIOwkLA4?feature=shared", model)

# References:
# https://docs.ultralytics.com/quickstart/#install-ultralytics
