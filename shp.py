import shapefile
import math
import random
import json
import pickle
import simplejson

from turtle import Screen, Turtle

r = 256

def get_color(s):
    s = str(s)
    a = 0
    b = 1
    for i in s:
        a += ord(i)

    b = a ** 4
    
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
    x = point[0] * r * 2 / 180 + r * 2.25
    y = -math.sinh(point[1] * math.pi / 180) * r + r * 2.25

    return x, y

def map(attrs):
    res = ""
    attrs = json.loads(attrs)
    print(list(attrs))
    for attr in list(attrs):
        sf = shapefile.Reader("resources/shape/" + attr + "/" + attr)
        countries = attrs[attr]["chosen"]

        shapeRecords = sf.shapeRecords()

        while len(shapeRecords) > 0:
            shapeRecord = shapeRecords[0]
            record = shapeRecord.record
            shape = shapeRecord.shape
            shapeRecords = shapeRecords[1::]

            if record[17] not in countries and countries[0] != "all":
                continue

            if attrs[attr]["color"] != "random":
                color2, color1 = attrs[attr]["color"], attrs[attr]["color"]
            else:
                color2, color1 = get_color(record[attrs[attr]["name"]])
            parts = shape.parts

            counter = 0

            for i in range(len(shape.points)):
                if len(parts) > 0 and i == parts[0]:
                    if parts[0] != 0:
                        res += '" />\n'
                    res += '<polygon stroke="' + color1 + '" fill="' + color2 + '" id="' + attr + record[attrs[attr]["name"]] + str(counter) + '" stroke-width="' + attrs[attr]["width"] +'" stroke-linejoin="round" points="'
                    parts = parts[1::]
                    counter += 1

                point = shape.points[i]
                x, y = proj(point)
                res += " " + str(x) + "," + str(y)
            res += '" />\n'
        sf.close()
        print(attr)
    return res

sf = shapefile.Reader("resources/shape/" + "inner_water" + "/" + "inner_water")
print(vars(sf.records()[0]))