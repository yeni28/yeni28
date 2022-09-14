import math
r= 5.74
holes = [
    [0,0],
    [127,0],
    [254,0],
    [0,127],
    [127,127],
    [254,127],
]




if x1 < 0 and y1 > 0 : #2사분면
    print(math.degrees(math.atan((x-x3)/(y-y3)) + math.radians(360)))
elif x1 > 0 and y1 < 0 : #4사분면
        print(math.degrees(math.atan((x-x3)/(y-y3)) + math.radians(180)))
elif x1 < 0 and y1 < 0 : #3사분면
        print(math.degrees(math.atan((x-x3)/(y-y3)) + math.radians(180)))

else:
    print(math.degrees(math.atan((x-x3)/(y-y3))))


for i in range(len(holes)):# 홀위치
    x2 = i[0] , y2 = i[1]
    x3, y3 =  63.5 , 63.5 #흰공의 위치
    # x2, y2 = 0,0 # 홀위치 
    x1, y1 = 200, 30 #타겟 공 위치
    if x1 > 0 :
        y1 = y1 * -1
        x1 = x1 * -1
        seta = math.atan((y2- y1)/ (x2-x1))
    else:
        seta = math.atan((y2- y1)/ (x2-x1))

    a = 2 * r * math.cos(seta)
    b = 2 * r * math.sin(seta)

    x = x1 - a
    y = y1 - b

    if ((x-x3)**2 + (y-y3)**2) + ((x2-x)**2+(y2-y)**2) > ((x2-x3)**2+(y2-y3)**2):
        print('둔각')
    elif ((x-x3)**2 + (y-y3)**2) + ((x2-x)**2+(y2-y)**2) < ((x2-x3)**2+(y2-y3)**2):
        print('예각')
