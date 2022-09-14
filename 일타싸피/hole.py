import math
r = 5.74
x1, y1 = 200, 30
x3, y3 = 63.5, 63.5

holes = [
    [0,0],
    [127,0],
    [254,0],
    [0,127],
    [127,127],
    [254,127],
]

for hole in holes: #홀 위치
    x2 , y2= hole[0], hole[1]
    
   
    a = 2*r
    rad = math.atan((x2-x3)/(y2-y3))
    if (x3 >= x2 and y3 <= y2) or (x3 <= x2 and y3 >= y2):
        y4 = y3 + math.cos(rad) * a
        x4 = x3 + math.sin(rad) * a
    else:
        y4 = y3- math.cos(rad) * a
        x4 = x3 - math.sin(rad) * a
    point = (x4,y4)


    a1 = ((x4 - x3)**2) + ((y4- y3)**2) #흰공이랑 보낼위치
    b1 = (x2-x4)**2 + (y2-y4)**2 #보낼 위치랑 홀 위치
    c1 = (x3-x2)**2 + (y3-y2)**2 #홀 위치랑 흰공 위치
    print(a1,b1,c1)
    if a1 + b1 < c1: #둔각이라면
        angle = math.acos((a1 + b1 - c1)/(2*(a1**0.5)*(b1**0.5))) 
        print(angle)

        max_angle = 0
        if 90 < math.degrees(angle) <= 180: #둔각 범위라면
            result_angle = math.degrees(angle)
            if max_angle < result_angle:
                max_angle = result_angle
                print(max_angle)
            


