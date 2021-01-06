from flask import Flask, render_template, flash, redirect, url_for, request, jsonify, send_from_directory
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/getmap/<map>')
def get_map(map):
    map_dat = json.load(open('maps/' + map + '.json', 'r'))
    print(map_dat)
    return render_template("map.html")

if __name__ == '__main__':
    app.run()