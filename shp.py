import shapefile
import math
import random
import json
import pickle
import simplejson
import time

from turtle import Screen, Turtle

r = 200
main_counter = 0

def d2r(a):
    return a * math.pi / 180

def get_color(s):
    s = str(s)
    a = 0
    b = 1
    for i in s:
        a += ord(i)

    b = a ** 5
    
    ans1 = "rgb("
    ans2 = "rgb("
    ans1 += str(127 + b % 127 - 65)
    ans2 += str(127 + b % 127 - 85)
    b /= 127
    ans1 += ", "
    ans2 += ", "
    ans1 += str(127 + b % 127 - 65)
    ans2 += str(127 + b % 127 - 85)
    b /= 127
    ans1 += ", "
    ans2 += ", "
    ans1 += str(127 + b % 127 - 65)
    ans2 += str(127 + b % 127 - 85)
    ans1 += ")"
    ans2 += ")"
    return ans1, ans2

def proj(point):
    x = point[0] * math.sinh(d2r(10)) * 10 * r * 1.5 / 180 + r * 2.9
    y = -math.sinh(d2r(point[1])) * r * 1.25 + r * 3.5

    #x = (d2r(point[0]) * 3 / (2 * math.pi)) * math.sqrt(abs((math.pi ** 2) / 3 - d2r(point[1]) ** 2))
    #y = d2r(point[1])

    #x *= r
    #y *= r

    return x, y

def map(attrs):
    attrs = json.loads(attrs)
    print(list(attrs))
    path = "temp/" + str(main_counter) + "_" + str(time.time()) + ".svg"
    svg = open(path, 'w', encoding="utf-8")
    svg.write("<g>")
    for attr in list(attrs):
        sf = shapefile.Reader("resources/shape/" + attr + "/" + attr)
        countries = attrs[attr]["chosen"]

        shapeRecords = sf.shapeRecords()

        for shapeRecord in shapeRecords:
            record = shapeRecord.record
            shape = shapeRecord.shape

            if record[attrs[attr]["name"]] not in countries and countries[0] != "all":
                continue

            if attrs[attr]["color1"] != "random":
                color2, color1 = attrs[attr]["color1"], attrs[attr]["color2"]
            else:
                color2, color1 = get_color(record[attrs[attr]["name"]])
            parts = shape.parts

            counter = 0

            head = ""

            for i in range(len(shape.points)):
                if len(parts) > 0 and i == parts[0]:
                    if parts[0] != 0:
                        svg.write('" />\n')
                    if shape.shapeType == 5:
                        svg.write('<polygon stroke="' + str(color1) + '" fill="' + str(color2) + '" id="' + str(attr) + str(record[attrs[attr]["name"]]) + str(counter) + '" stroke-width="' + str(attrs[attr]["width"]) + '" stroke-opacity="' + str(attrs[attr]["opacity"]) + '" stroke-linejoin="round" style="clip-path: url("#' + str(attr) + str(record[attrs[attr]["name"]]) + str(counter) + '")' + '" points="')
                    if shape.shapeType == 3:
                        svg.write('<polyline stroke="' + str(color1) + '" id="' + str(attr) + str(record[attrs[attr]["name"]]) + str(counter) + '" stroke-width="' + str(attrs[attr]["width"]) +'" stroke-opacity="' + str(attrs[attr]["opacity"]) + '" fill="none" stroke-linejoin="round" points="')
                    parts = parts[1::]
                    counter += 1

                point = shape.points[i]
                x, y = proj(point)
                svg.write(" " + str(x) + "," + str(y))
            svg.write('" />\n')
        sf.close()
        print(attr)

    svg.write("</g>")
    svg.close()
    print("All done!")
    return path