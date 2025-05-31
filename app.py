from flask import Flask, render_template, request
from ultralytics import YOLO
import os
import cv2


app = Flask(__name__)
model = YOLO(".venv/yolov8n.pt")


os.makedirs("uploads", exist_ok=True)
os.makedirs("static/processed", exist_ok=True)

vehicle_classes = [2, 3, 5, 7]



def count_vehicles_and_save(image_path, output_path):
    results = model(image_path)
    result = results[0]

    # Count vehicles
    vehicle_count = sum(1 for cls in result.boxes.cls if int(cls.item()) in vehicle_classes)

    # Load image with OpenCV
    img = cv2.imread(image_path)

    # Draw clean boxes manually
    for box in result.boxes:
        cls_id = int(box.cls[0])
        if cls_id in vehicle_classes:
            label = model.names[cls_id]
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 1)  # thin box
            cv2.putText(img, label, (x1, y1 - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)  # small text

    # Save the cleaned image
    cv2.imwrite(output_path, img)

    return vehicle_count


def calculate_green_time(vehicle_count):
    base_green_time = 15  # Base green time in seconds
    vehicle_multiplier = 2  # Additional time per vehicle

    # Constraint: If vehicle count is 10 or less, use only base time
    if vehicle_count<=5:
        time=10
        return time
    elif vehicle_count <= 10:
        return base_green_time
    else:
        green_time = base_green_time + (vehicle_count * vehicle_multiplier)
        return green_time



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        files = request.files.getlist('images')
        results = []

        for i, image in enumerate(files):
            if image:
                filename = f"frame{i + 1}.jpg"
                upload_path = os.path.join("uploads", filename)
                output_path = os.path.join("static/processed", filename)
                image.save(upload_path)

                count = count_vehicles_and_save(upload_path, output_path)
                time = calculate_green_time(count)

                results.append({
                    "frame": i + 1,
                    "image": filename,
                    "count": count,
                    "time": time
                })

        return render_template("result.html", results=results)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
