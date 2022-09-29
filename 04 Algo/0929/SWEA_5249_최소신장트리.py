def prim(start, V):
    U = []
    D = [10000] * (V + 1)  # 밸류
    P = [10000] * (V + 1)  # 스타트
    D[0] = 0

    while len(U) < (V + 1):
        # curV = U에 D 중 가장 작은 값을 가진 정점을 선택
        minV = 10000
        for i in range(V + 1):
            if i in U:
                continue
            if minV > D[i]:
                minV = D[i]
                curV = i

        U.append(curV)
        # curV하고 연결된 정점들의 D값을 최선으로 바꿔준다.
        for i in range(V + 1):
            if i in U:
                continue
            if G[curV][i] and D[i] > G[curV][i]:
                D[i] = G[curV][i]
                P[i] = curV
    print(U, D, P)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    G = [[0] * (V + 1) for _ in range(V + 1)]
    for j in range(E):
        n1, n2, w = map(int, input().split())
        G[n1][n2] = w
        G[n2][n1] = w

