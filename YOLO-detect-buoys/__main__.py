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

    HfApi().whoami(token=getenv("HF_TOKEN"))

    device = get_device()
    model = YOLO("yolov8n.pt")

    file_path = path.abspath(getcwd())
    dataset = get_data()

    result = model.train(
        data=dataset.location + "/data.yaml", epochs=50, imgsz=640, device=device
    )

    model.val()

    path = model.export(format="onnx")  # export to onnx

    # Initialize the repository
    repo = Repository(local_dir=path, clone_from=getenv("HG_REPO_ID"))

    # Commit and push your changes
    repo.push_to_hub(commit_message="push the model to the hub")

# References:
# https://docs.ultralytics.com/quickstart/#install-ultralytics
