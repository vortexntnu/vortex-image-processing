"""
The main entry point for YOLO detecter buoys.
"""

from os import getcwd, getenv, path

from dotenv import load_dotenv
from huggingface_hub import HfApi, Repository
from ultralytics import YOLO
from utils import get_data, get_device, process_video

if "__main__" == __name__:

    load_dotenv()

    device = get_device()
    print("device", device)
    model = YOLO("yolov8n.pt")

    file_path = path.abspath(getcwd())
    dataset = get_data()

    result = model.train(
        data=dataset.location + "/data.yaml",
        epochs=100,
        imgsz=640,
        device=device,
        batch=4,
        cache=False,
    )

    model.val()

    path = model.export(format="onnx")  # export to onnx

    print("Model exported to: " + path)
    print(path)

# References:
# https://docs.ultralytics.com/quickstart/#install-ultralytics
