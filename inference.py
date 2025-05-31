from ultralytics import YOLO
import cv2
import numpy as np
import json
import base64
import io
from PIL import Image

model = YOLO("yolov8n.pt")
vehicle_classes = [2, 3, 5, 7]  # car, bike, bus, truck

def model_fn(model_dir):
    return model

def input_fn(request_body, request_content_type):
    if request_content_type == 'application/json':
        payload = json.loads(request_body)
        image_data = base64.b64decode(payload['image'])
        image = Image.open(io.BytesIO(image_data)).convert("RGB")
        return np.array(image)

def predict_fn(image_array, model):
    results = model(image_array)
    boxes = results[0].boxes
    count = sum(1 for cls in boxes.cls if int(cls.item()) in vehicle_classes)
    return {"vehicle_count": count}

def output_fn(prediction, content_type):
    return json.dumps(prediction)


#old code in imagedetect.y


