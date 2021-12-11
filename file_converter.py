import cv2
import os
import flask

def file_to_numpy_array(app, file):
    filename = file.filename
    upload_folder = app.config['UPLOAD_FOLDER']

    if not os.path.isdir(upload_folder):
        os.makedirs(upload_folder)
    
    file_path = os.path.join(upload_folder, filename)
    file.save(file_path)
        
    return flask.send_file(file_path, attachment_filename = filename)


def cut_out_face(image):
    return 'nothin yet'
