T = int(input())

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

cost = []

for tc in range(1, T+1):
    n,m = map(int, input().split())

    city = [list(map(int, input().split())) for _ in range(n)]

    #손해를 보지 않으면서 서비스 할 수 있는 최대 집의 수
    answer = [0] * 22

    for i in range(22):
        cost[i] = i **2 + (i-1)**2

    #모든 위치에서 한번시도해보자!
    for i in range(n):
        for j in range(n):
            # 모든 위치에서 범위 계산
            q = [(i,j)]
            visited = [[0] * n for _ in range(n)]
            # 현재 위치는 방문했다고 표시
            visited[i][j] = 1
            # 영역의 크기를 나타냄
            k = 0
            # 영역 안에 포함되어있는 집의 개수
            h_cnt = 0

            while q: #q가 비어있을 때까지 계속 반복하겠다.
                k += 1 # 영역의 크기는 1씩 증가한다.
                if k > n+1:
                    break
                for _ in range((len(q))):
                    next = q.pop(0)
                    if city[next[0][next[1]]] == 1: # 꺼내온 위치에 집이 있는지 검사
                        h_cnt += 1
                    for d in range(4):
                        ni = next[0] + di[d]
                        nj = next[1] + di[d]
                        if 0<= ni <n and 0 <= nj <n and visited[ni][nj] == 0:
                            visited[ni][nj] = 1
                            q.append((ni,nj))
                # for문이 끝나면  k =?? 일때 포함된 집의 개수를 알 수 있다.
                profit = h_cnt * m - cost[k]
                if profit >= 0:
                    answer = h_cnt if answer < h_cnt else answer
    print(f'#{tc} {answer}')

