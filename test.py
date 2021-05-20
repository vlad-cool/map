import shapefile

nam111 = "cities"

sf = shapefile.Reader("resources/shape/" + nam111 + "/" + nam111)

shapes = sf.shapeRecords()
out = open("out.txt", "w", encoding="utf-8")

records = sf.records()

#print(sf.shapes()[0].shapeType)
#print(sf.fields)

for record in records:
    for i in range(len(list(record))):
        out.write(str(i) + ":" + str(record[i]) + " " * (64 - len(str(i) + ":" + str(record[i]))))
    out.write("\n")