import cv2
import os
import flask
import numpy

def read_image(app, file):
    file_path = save_file(app, file)
    image = cv2.imread(file_path)
    os.remove(file_path)
    return image

def process_image(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor = 1.2, minNeighbors = 5)
    cropped_image = None
    if len(faces) > 0:
        x, y, w, h = faces[0]
        cropped_image = gray_image[y:y+h, x:x+w]
    else:
        cropped_image = gray_image
    final_image = cv2.resize(cropped_image, [48,48])
    return final_image

def save_file(app, file):
    filename = file.filename
    upload_folder = app.config['UPLOAD_FOLDER']

    if not os.path.isdir(upload_folder):
        os.makedirs(upload_folder)
    
    file_path = os.path.join(upload_folder, filename)
    file.save(file_path)
    return file_path
