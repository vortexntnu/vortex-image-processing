"""
The main entry point for YOLO detecter buoys.
"""

from ultralytics import YOLO
from utils import get_device

if "__main__" == __name__:
    device = get_device()
    model = YOLO("yolov8n.pt")
    model.to(device)

    # Train the model using the 'coco128.yaml' dataset for 3 epochs
    results = model.train(data="coco128.yaml", epochs=3)

    # Evaluate the model's performance on the validation set
    results = model.val()

    # Perform object detection on an image using the model
    results = model("https://ultralytics.com/images/bus.jpg")


# References:
# https://docs.ultralytics.com/quickstart/#install-ultralytics
