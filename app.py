import cv2
import numpy as np
import csv
from datetime import datetime
import os

# Initialize video capture
video_capture = cv2.VideoCapture(0)

# Load Haar Cascade for face detection (built into OpenCV, no dlib needed)
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Initialize LBPH Face Recognizer (works great on Apple Silicon)
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Known faces setup
known_faces_names = ["rayan", "kevin", "shaggy", "president"]
students = known_faces_names.copy()


# Train the recognizer with your photos
def load_and_train():
    faces = []
    labels = []

    for idx, name in enumerate(known_faces_names):
        # Try different extensions
        for ext in [".jpg", ".jpeg", ".png"]:
            filepath = f"photos/{name}{ext}"
            if os.path.exists(filepath):
                img = cv2.imread(filepath)
                if img is None:
                    continue
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                face = face_cascade.detectMultiScale(gray, 1.3, 5)

                if len(face) > 0:
                    (x, y, w, h) = face[0]
                    face_roi = gray[y : y + h, x : x + w]
                    face_roi = cv2.resize(face_roi, (200, 200))
                    faces.append(face_roi)
                    labels.append(idx)
                    print(f"✓ Loaded {name}")
                    break
        else:
            print(f"✗ Could not load {name}")

    if len(faces) > 0:
        recognizer.train(faces, np.array(labels))
        print("\n✓ Training complete!")
    else:
        print("\n✗ No faces loaded. Check your photos folder.")
        exit()


# Train the model
print("Loading and training faces...")
load_and_train()

# Create CSV file
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
f = open(current_date + ".csv", "w+", newline="")
lnwriter = csv.writer(f)
lnwriter.writerow(["Name", "Time"])

print("\nStarting attendance system. Press 'q' to quit.\n")

# Track who has been recorded (with cooldown)
recorded_times = {}
COOLDOWN_SECONDS = 5

while True:
    ret, frame = video_capture.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Convert to grayscale for detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for x, y, w, h in faces:
        # Extract and prepare face for recognition
        face_roi = gray[y : y + h, x : x + w]
        face_roi = cv2.resize(face_roi, (200, 200))

        # Recognize face
        label, confidence = recognizer.predict(face_roi)

        # Lower confidence = better match (0-100 scale typically)
        if confidence < 70:
            name = known_faces_names[label]
            color = (0, 255, 0)

            # Record attendance with cooldown
            current_time = datetime.now()
            if name in students:
                students.remove(name)
                time_str = current_time.strftime("%H:%M:%S")
                lnwriter.writerow([name, time_str])
                f.flush()  # Save immediately
                recorded_times[name] = current_time
                print(f"✓ Recorded: {name} at {time_str}")
                print(f"Remaining: {students}")
        else:
            name = "Unknown"
            color = (0, 0, 255)

        # Draw rectangle and label
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv2.rectangle(frame, (x, y + h), (x + w, y + h + 30), color, cv2.FILLED)
        cv2.putText(
            frame,
            f"{name} ({int(confidence)})",
            (x + 5, y + h + 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 255, 255),
            1,
        )

    # Show frame
    cv2.imshow("Attendance System", frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Cleanup
video_capture.release()
cv2.destroyAllWindows()
f.close()
print(f"\n✓ Attendance saved to {current_date}.csv")
