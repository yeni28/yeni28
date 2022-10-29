

di = [-1,1,0,0]
dj = [0,0,-1,1]


def find_path(i, j, length, start):
    global max_len
    global max_num

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if 0 <= ni < n and 0 <= nj < n and rooms[ni][nj] == rooms[i][j] + 1:
            find_path(ni, nj, length + 1, start)
    if max_len < length:
        max_len = length
        max_num = start
    if max_len == length:
        if max_num > start:
            max_num = start

T = int(input())

for tc in range(1, T+1):
    n = int(input())

    rooms = [list(map(int,input().split())) for _ in range(n)]

    max_len = 0
    max_num = 9999


    for i in range(n):
        for j in range(n):
            find_path(i,j,1,rooms[i][j])
    print(f'#{tc} {max_num} {max_len}')
