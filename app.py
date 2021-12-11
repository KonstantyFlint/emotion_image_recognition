from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

from flask import Flask, request
from waitress import serve
from io import BufferedReader


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/temp_files/'
app.config['MAX_CONTENT_PATH'] = 1024 * 1024

@app.route('/')
def homepage():
    return "hello"

@app.route('/uploader', methods = ['POST'])
def upload_file():
    file = request.files['file']
    file_content = file.read()
    file_path = getpath(file)
    return file_path


if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8080)
