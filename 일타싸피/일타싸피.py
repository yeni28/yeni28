import math

# def play(conn, gameData):
#     angle = 0
#     power = 0

#     conn.send(angle, power)

#     whiteBall_x = balls[0][0]  #x3
#     whiteBall_y = balls[0][1]   #y3

#     whiteBall_nx =   #x
#     whiteBall_ny =    #y

#     targetBall_x= balls[0][0]   #x1
#     targetBall_y = balls[0][1]  #y1

#     hole_x= balls[0][0]   #x2
#     hole_y = balls[0][1]  #y2
    
r = 5
x2, y2 = 0,0
x1, y1 = -10, -10
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

print(x, y)


