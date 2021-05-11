import shapefile
import math
import random
import json
import pickle
import simplejson

from turtle import Screen, Turtle

r = 256

def proj(point):
    #x = math.tan(point[0] * math.pi / 180) * r + r
    #y = -point[1] * r / 180 + r

    x = point[0] * r * 2 / 180 + r
    y = -math.tan(point[1] * math.pi / 180) * r + r * 3

    #y = r * math.tan(math.pi * -point[1] / 180) + 800

    return x, y

def map(attrs):
    res = ""
    attrs = json.loads(attrs)

    for attr in list(attrs):
        sf = shapefile.Reader("resources/shape/" + attr + "/" + attr)
        countries = attrs[attr]

        colors = ["red", "green", "blue", "cyan", "gray"]
        shapeRecords = sf.shapeRecords()

        while len(shapeRecords) > 0:
            shapeRecord = shapeRecords[0]
            record = shapeRecord.record
            shape = shapeRecord.shape
            shapeRecords = shapeRecords[1::]

            if record[17] not in countries:
                continue

            color = colors[random.randrange(0, len(colors), 1)]
            parts = shape.parts

            counter = 0

            for i in range(len(shape.points)):
                if len(parts) > 0 and i == parts[0]:
                    if parts[0] != 0:
                        res += '" />\n'
                    res += '<polygon stroke="' + color + '" id="' + attr + record[17] + str(counter) + '" stroke-width="1px" fill="none" points="'
                    parts = parts[1::]
                    counter += 1

                point = shape.points[i]
                x, y = proj(point)
                res += " " + str(x) + "," + str(y)
            res += '" />\n'
        sf.close()
    return res