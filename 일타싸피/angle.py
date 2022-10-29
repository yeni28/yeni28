import math

x, y = -17.071067811865476,-17.071067811865476
x3, y3 = 0, 0
x1, y1 = -10, -1

if x1 < 0 and y1 > 0 : #2사분면
    print(math.degrees(math.atan((x1-x3)/(y1-y3)) + math.radians(360)))
elif x1 > 0 and y1 < 0 : #4사분면
        print(math.degrees(math.atan((x1-x3)/(y1-y3)) + math.radians(180)))
elif x1 < 0 and y1 < 0 : #3사분면
        print(math.degrees(math.atan((x1-x3)/(y1-y3)) + math.radians(180)))

else:
    print(math.degrees(math.atan((x1-x3)/(y1-y3))))