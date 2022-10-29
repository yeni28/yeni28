def find_point(x3,y3,x2,y2,a):
    a = 2*r
    rad = math.atan((x2-x3)/(y2-y3))
    if (x3 >= x2 and y3 <= y2) or (x3 <= x2 and y3 >= y2):
        y4 = y3 + math.cos(rad) * a
        x4 = x3 + math.sin(rad) * a
    else:
        y4 = y3- math.cos(rad) * a
        x4 = x3 - math.sin(rad) * a
    point = (x4,y4)
    return point