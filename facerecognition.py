import face_recognition_models
import cv2
import face_recognition
import os
import sqlite3
from datetime import datetime
print("Starting face recognition system...")

# Database setup
conn = sqlite3.connect('attendance.db')
conn.execute('''CREATE TABLE IF NOT EXISTS attendance (name TEXT, date TEXT)''')

# Load known faces
known_faces = []
known_names = []
for image in os.listdir('student_images'):
    img = face_recognition.load_image_file(f"student_images/{image}")
    encoding = face_recognition.face_encodings(img)[0]
    known_faces.append(encoding)
    known_names.append(image.split('.')[0])

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    
    for face_encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_faces, face_encoding)
        name = "Unknown"
        if True in matches:
            name = known_names[matches.index(True)]
            conn.execute("INSERT INTO attendance (name, date) VALUES (?, ?)", (name, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            conn.commit()
            print(f"Attendance marked for {name}")
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
conn.close()