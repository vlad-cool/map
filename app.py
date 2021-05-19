import os
import shp
from flask import Flask, render_template, send_from_directory, request, Response, stream_with_context, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

    return render_template("simple_path_to_polyline.html")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static', 'favicons'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/get_map', methods=['POST'])
def get_map():
    path = shp.map(request.form["attrs"])
    file = open(path, 'r', encoding="utf-8")
    s = file.read()
    file.close()
    os.remove(path)
    return s

@app.route('/test', methods=['GET'])
def hello_world():
    def generate():
        yield "111"
        yield "222"
    return Response(stream_with_context(generate()))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")