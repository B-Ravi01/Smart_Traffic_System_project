from ultralytics import YOLO
import cv2

model = YOLO(".venv/yolov8n.pt")  # You can replace this with a fine-tuned model later

# Replace with your test image path
image_path = ".venv/traffic-jamz-2.jpg"
results = model(image_path)

# Class IDs for vehicles in COCO dataset
vehicle_classes = [2, 3, 5, 7]  # car, motorcycle, bus, truck

vehicle_count = sum(
    1 for cls in results[0].boxes.cls if int(cls.item()) in vehicle_classes
)

print(f"Detected {vehicle_count} vehicles.")