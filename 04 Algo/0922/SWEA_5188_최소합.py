cnt = 0
def bfs_sum(i, j, N): #시작 위치와 N의 크기
    visited = [[0] * N for _ in range(N)]
    route_sum = 0 + arr[i][j]
    # visited[i][j] = 1  # 시작점 방문 표시

    di = [1, 0]
    dj = [0, 1]

    while True:
        # 현재 위치가 도착점인지 판단:
        if arr[i][j] == arr[N-1][N-1]:
            return route_sum # 최소합 출력

        for d in range(2):
            ni = di[d] + i
            nj = dj[d] + j
            # 이동 조건
            if 0 <= ni < N and 0 <= nj < N:  # 갈 수 있는 위치면
                # 현재 위치를 스택에 저장
                q.append((ni, nj))
                # visited[ni][nj] = visited[i][j] + 1
                # 현재 위치를 다음 위치로 최신화
                i, j = ni, nj
                route_sum += arr[i][j]
                break  # 현재 갈 수 있는 방향으로 더 가지않고 다음 방향으로 가게된다.
        else:
            if q:
                i, j = q.pop()
            # 스택이 비어있으면 반복을 종료.
            else:
                break

    return 0


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input(). split())) for _ in range(n)]
    ans = bfs_sum(0,0)

    print(f'#{tc} {ans}')