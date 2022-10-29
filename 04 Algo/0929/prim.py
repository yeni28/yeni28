def prim1(r, V):
    MST = [0]*(V+1)         # MST 포함여부(visited 배열과 비슷하다)
    key = [10000]*(V+1)     # 가중치의 최대값 이상으로 초기화
    # key[v]는 v가 MST 에 속한 정점과 연결될 수 있음
    key[r] = 0              # 시작정점의 key
    for _ in range(V):      # V+1 개의 정점 중 V개를 선택
        # MST에 포함되지 않은 정점 중(MST[u] == 0), key가 최소인 u 찾기
        u = 0
        minV = 10000
        for i in range(V+1):
            if MST[i] == 0 and key[i] < minV:
                u = i
                minV = key[i]
        MST[u] = 1              # 정점 u를 MST 에 추가
        # u에 인접인 v에 대해, MST 에 포함되지 않은 정점이면
        for v in range(V+1):
            if MST[v] == 0 and adjM[u][v] > 0:
                key[v] = min(key[v], adjM[u][v])
                # u를 통해 MST 에 포함되는 비용과 기존 비용을 비교해서 최소값을 사용
    return sum(key)     # MST 가중치의 합


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjM = [[0]*(V+1) for _ in range(V+1)]  # 인접 행렬

    for _ in range(E):
        u, v, w = map(int, input().split())
        adjM[u][v] = w
        adjM[v][u] = w      # 가중치가 있는 무방향 그래프