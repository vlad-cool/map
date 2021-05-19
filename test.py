import shapefile

nam111 = "cities"

sf = shapefile.Reader("resources/shape/" + nam111 + "/" + nam111)

shapes = sf.shapeRecords()

print(sf.shapes()[0].shapeType)
print(sf.fields)

for shapeRecord in shapes:
    for i in sf.fields:
        print(sf.fields, end=" ")
    print("") 