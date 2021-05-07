import shapefile
import math
import random
from turtle import Screen, Turtle

r = 1000

def proj(point):
    x = point[0] * r / 180 + r
    y = -point[1] * r / 180 + r

    #y = r * math.tan(math.pi * -point[1] / 180) + 800

    return x, y

sf = shapefile.Reader("resources/shape/ne_10m_admin_0_countries_lakes/ne_10m_admin_0_countries_lakes")

f = open('out.txt','w')
svg = open('out.svg','w')

###svg.write('<svg width="1600" height="1600" xmlns="http://www.w3.org/2000/svg">')

shapes = sf.shapes()


###screen = Screen()
### screen.setup(2 * r + 4, 2 * r + 8)  # fudge factors due to window borders & title bar
###turtle = Turtle()
###turtle.penup()


counter = 1

'''for k in sf.shapes():
    if counter > 0:
        counter -= 1
    else:
        break
    for i in k.parts:
        colors = ["red", "green", "blue", "cyan", "gray"]

        f.write(str(i.points) + "\n")

        first = i.points[0]

        y0 = first[1] * r / 180 + 800
        #####y0 = r * math.tan(math.pi * first[1] / 180) + 800
        x0 = first[0] * r / 180 + 800
        ###turtle.color(colors[random.randrange(0, len(colors), 1)])
        ###turtle.goto(x0, y0)
        ###turtle.pendown()

        svg.write('<polyline stroke="' + colors[random.randrange(0, len(colors), 1)] + '" stroke-width="1px" fill="none" points="')
        #svg.write(" " + str(x0) + "," + str(y0))


        for a, b in i.points:
            #print(str(a) + " " + str(b))
            #x = 400 + tg(j.first)

            y = b * r / 180 + 800
            #####y = r * math.tan(math.pi * b / 180) + 800
            x = a * r / 180 + 800
            #print(x, y)
            ###turtle.goto(x, y)

            svg.write(" " + str(x) + "," + str(y))

        ###turtle.goto(x0, y0)
        ###turtle.penup()

        svg.write(" " + str(x0) + "," + str(y0))
        svg.write('" />\n')



#turtle.exitonclick()
'''

colors = ["red", "green", "blue", "cyan", "gray"]
shapes = sf.shapes()

svg.write('<svg width="' + str(2 * r) + '" height="' + str(2 * r) + '" xmlns="http://www.w3.org/2000/svg">')

for shape in shapes:
    color = colors[random.randrange(0, len(colors), 1)]

    parts = shape.parts

    for i in range(len(shape.points)):
        if len(parts) > 0 and i == parts[0]:
            if parts[0] != 0:
                svg.write('" />\n')
            svg.write('<polygon stroke="' + colors[random.randrange(0, len(colors), 1)] + '" stroke-width="1px" fill="none" points="')
            parts = parts[1::]

        point = shape.points[i]
        x, y = proj(point)
        svg.write(" " + str(x) + "," + str(y))
    
    svg.write('" />\n')

svg.write('</svg>')

sf.close()
f.close()