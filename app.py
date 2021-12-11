from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

from flask import Flask, request
import flask
from waitress import serve
from io import BufferedReader

import utils
import pseudomaciek

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'temp_files'
app.config['MAX_CONTENT_PATH'] = 1024 * 1024

@app.route('/evaluateImage', methods = ['POST'])
def evaluate_image():
    file = request.files['file']
    image = utils.read_image(app, file)
    processed_image = utils.process_image(image)
    return pseudomaciek.evaluate(processed_image)

@app.route('/')
def homepage():
    return flask.send_from_directory("static", "file_form.html")


if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8080)
