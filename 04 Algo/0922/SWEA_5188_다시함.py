dx = [1, 0]
dy = [0, 1]

def bfs(x, y, s):
    minv = (n ** 2) * 10
    #visited = [[0]*n for _ in range(n)]  # 방문배열 만들고
    q = []  # q 만들고
    q.append((x, y, s))  # q에 담고

    while q:
        x, y, s = q.pop(0)
        for d in range(2):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and s + arr[ny][nx] < minv:# 이동 조건에 맞으면
                # s += arr[ny][nx] 이러면 s 계속 갱신됨..
                if nx == n-1 and ny == n-1:
                    if s + arr[ny][nx] < minv:
                        minv = s + arr[ny][nx]
                else:
                    q.append((nx, ny, s + arr[ny][nx]))

                # i, j = ni, nj : 이렇게 하면 한쪽 방향으로 감/ 다른 방향 탐색X

    return minv

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = bfs(0,0,arr[0][0])
    print(f'#{tc} {ans}')