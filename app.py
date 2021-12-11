from flask import Flask
from waitress import serve
app = Flask(__name__)

@app.route('/')
def homepage():
    return 'asdasdasdasdasd'

@app.route('/uploader', methods = ['POST'])
def upload_file():
      f = request.files['file']
      o = f.read()
      
      return str(o);

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8080)
