from flask import Flask, render_template, flash, redirect, url_for, request, jsonify, send_from_directory
import math
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

def proj_cyll_p(points, scale):
    for i in len(points):
        points[i] = math.sin(points[i] * math.pi / 180*60*60*100) * scale
    return points

def proj_cyll_l(points, start, scale):
    for i in len(points):
        points[i] = points[i] * scale
    return points

@app.route('/getmap/<map>')
def get_map(map):
    map_dat = json.load(open('maps/' + map + '.json', 'r'))
    print(map_dat)
    polyline = open('maps/' + map_dat["points"]).read()
    polyline = list(map(int, polyline.split()))
    pointsP = polyline[0::2]  #Широта
    pointsL = polyline[1::2]  #Долгота
    print(pointsP)
    print(pointsL)

    proj_cyll_p(pointsP, 1)
    proj_cyll_l(pointsL, 0, 1)

    polyline[0::2] = pointsP
    polyline[1::2] = pointsL

    return render_template("map.html", polyline = polyline)

if __name__ == '__main__':
    app.run()