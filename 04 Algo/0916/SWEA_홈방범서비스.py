T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]


    # 서비스 영역을 구하기
    di = [-1,1,0,0]
    dj = [0,0,-1,1]


    # 도시의 영역 내에서 서비스 영역을 탐색하자
    for i in range(N):
        for j in range(N):
            for
