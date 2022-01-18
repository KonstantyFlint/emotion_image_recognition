from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

from flask import Flask, request
import flask
from waitress import serve
from io import BufferedReader
import tensorflow

import utils

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'temp_files'
app.config['MAX_CONTENT_PATH'] = 1024 * 1024

@app.route('/evaluateImage', methods = ['POST'])
def evaluate_image():
    file = request.files['file']
    
    image = utils.read_image(app, file)
    
    processed_image = utils.process_image(image)
    
    classifier = tensorflow.keras.models.load_model("model.h5")
    
    prediction_vals = classifier.predict(processed_image)[0]
    
    emotion_names = ['anger', 'disgust', 'fear', 'happiness', 'neutral', 'sadness', 'surprise']
    
    return utils.to_json(emotion_names, prediction_vals)

@app.route('/')
def homepage():
    return flask.send_from_directory("static", "file_form.html")


if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8080)
