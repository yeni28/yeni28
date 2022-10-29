def dfs(v):
    visited[v] = 1 #방문표시

    for k in graph[v]: #정점과 연결된 정점들을 순회
        if visited[k]: #방문하지 않은 정점들을 선택
            continue
        dfs(k)


T = int(input())
for tc in range(1, T+1):
    # dfs의 입력 받기
    N, M = map(int, input().split())
    # 보통 노드나 정점을 리스트로 받는다.
    tmp = list(map(int, input().split()))
    # 그래프를 만들어 연결 상태를 체크해줘야한다.
    graph = [[] for _ in range(N+1)]

    # 연결 상태 체크하기
    # 방향이 정해지지 않은 그래프의 연결상태
    for i in range(M):
        v1 = tmp[i * 2] #노드1(짝수)
        v2 = tmp[i * 2 + 1] # 노드1과 연결된 노드(홀수)
        graph[v1].append(v2)
        graph[v2].append(v1)

    # 방문 배열을 만들어 체크해준다.
    visited = [0 for _ in range(N+1)]
    cnt = 0

    for i in range(1, N+1):
        if visited[i]:
            continue
        dfs(i)
        cnt += 1
    print(f'#{tc} {cnt}')