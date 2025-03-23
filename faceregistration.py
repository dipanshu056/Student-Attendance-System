import cv2
import os

# Folder for student images 
if not os.path.exists('student_images'):
    os.makedirs('student_images')

cap = cv2.VideoCapture(0)  # Webcam
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') 

# Student Name
name = input("Enter student name: ")

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        face = frame[y:y+h, x:x+w]  
# Face crop 
        cv2.imshow('frame', frame)
        
# 's' press karo to save
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite(f"student_images/{name}.jpg", face)
            print(f"{name} registered!")
            cap.release()
            cv2.destroyAllWindows()
            exit()
    
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
 # 'q' se exit
        break

cap.release()
cv2.destroyAllWindows()