"""
The main entry point for YOLO detecter buoys.
"""

from ultralytics import YOLO
from utils import get_device

if "__main__" == __name__:
    """
    The main entry point for YOLO detecter buoys.
    """

    device = get_device()
    model = YOLO("yolov8n.pt")
    model.to(device)
    results = model.train(data="coco128.yaml", epochs=3)
    results = model.val()


# References:
# https://docs.ultralytics.com/quickstart/#install-ultralytics
