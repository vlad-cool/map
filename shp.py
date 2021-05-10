import shapefile
import math
import random
import json
import pickle
import simplejson

from turtle import Screen, Turtle

r = 1000

def proj(point):
    x = point[0] * r / 180 + r
    y = -point[1] * r / 180 + r

    #y = r * math.tan(math.pi * -point[1] / 180) + 800

    return x, y

'''def parse_record(record):
    
    #attrs = vars(record)
    #f.write(str(attrs) + "\n")

    try:
        attrs = vars(record)["_Record__field_positions"]
    except:
        attrs = vars(record)

    for attr_name in tuple(attrs.keys()):
        #f.write(attr_name + " " + str(attrs[attr_name]) + "\n")
        try:
            attrs[attr_name] = record[attrs[attr_name]]
        except:
            attrs[attr_name] = attrs[attr_name]

    f.write(str(attrs) + "\n")

    return attrs

    try:
        for attr_name in tuple(attrs.keys()):
            attrs[attr_name] = eval("record." + attr_name)
    except:
        attrs = vars(record)
        for attr_name in tuple(attrs.keys()):
            attrs[attr_name] = eval("record." + attr_name)

    try:
        return attrs["_Record__field_positions"]
    except:
        return attrs
'''

sf = shapefile.Reader("resources/shape/ne_10m_admin_0_countries_lakes/ne_10m_admin_0_countries_lakes")

f = open('out.txt','w', encoding='utf-8')
svg = open('out.svg','w', encoding='utf-8')

colors = ["red", "green", "blue", "cyan", "gray"]
shapeRecords = sf.shapeRecords()

svg.write('<svg width="' + str(2 * r) + '" height="' + str(2 * r) + '" xmlns="http://www.w3.org/2000/svg">')

while len(shapeRecords) > 0:
    shapeRecord = shapeRecords[0]
    shapeRecords = shapeRecords[1::]
    shape = shapeRecord.shape
    record = shapeRecord.record

    color = colors[random.randrange(0, len(colors), 1)]
    parts = shape.parts

    #try:
    #print(parse_record(record))
    ##f.write(str(parse_record(record)))
    ##print(parse_record(record))
    ##print(str(parse_record(record)["NAME"]))
    #except:
    #    print("ERR")
    counter = 0

    for i in range(len(shape.points)):
        if len(parts) > 0 and i == parts[0]:
            if parts[0] != 0:
                svg.write('" />\n')
            asasasasa = record[17]
            svg.write('<polygon stroke="' + color + '" id="' + record[17] + str(counter) + '" stroke-width="1px" fill="none" points="')
            parts = parts[1::]
            counter += 1

        point = shape.points[i]
        x, y = proj(point)
        svg.write(" " + str(x) + "," + str(y))
    
    svg.write('" />\n')

svg.write('</svg>')

################
#print(str(vars(sf.records()[0])))

#for key, value in vars(sf.records()).iteritems():
#    f.write(str(key) + ":" + str(value) + "---")
    

'''
records = sf.records()

while len(records) > 0:
    record = records[0]
    records = records[1::]

    #for name in dir(record):
    #    if not name.startswith('__'):
    #        print(name)
    
    print(record[3])

    parse_record(record)
    try:
        print(str((record.NAME)))
    except:
        pass
'''
################

sf.close()
f.close()

def map(attrs):
    res = ""
    attrs = attrs.split(" ")
    sf = shapefile.Reader(attrs[0])

    colors = ["red", "green", "blue", "cyan", "gray"]
    shapeRecords = sf.shapeRecords()
    
    while len(shapeRecords) > 0:
        shapeRecord = shapeRecords[0]
        shapeRecords = shapeRecords[1::]
        shape = shapeRecord.shape
        record = shapeRecord.record

        color = colors[random.randrange(0, len(colors), 1)]
        parts = shape.parts

        counter = 0

        for i in range(len(shape.points)):
            if len(parts) > 0 and i == parts[0]:
                if parts[0] != 0:
                    svg.write('" />\n')
                asasasasa = record[17]
                res += '<polygon stroke="' + color + '" id="' + record[17] + str(counter) + '" stroke-width="1px" fill="none" points="'
                parts = parts[1::]
                counter += 1

            point = shape.points[i]
            x, y = proj(point)
            res += " " + str(x) + "," + str(y)
        res += '" />\n'
    sf.close()
    f.close()