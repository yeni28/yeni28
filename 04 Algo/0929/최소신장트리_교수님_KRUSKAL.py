
T = int(input())


def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

# x 집합 , y 집합을 합치는 연산
def union(x, y):
    x = find_set(x)  # x집합의 대표
    y = find_set(y)  # y집합의 대표

    # 두 집합의 대표가 같다면 합칠 필요가 없다.
    if x == y:
        return



for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = []
    for i in range(E):
        s ,e ,w = map(int, input().split())
        edges.append((w ,s ,e))
    edges.sort()

    # 부모가 누군지 가리키는 집합 p
    p = [i for i in range(V+1)]
    # rank

    rank =[0] * [V+1]

    # N은 정점수, V가 정점 번호인데, V+1(마지막 정점 번호+1)
    N =  V+1
    # cnt는 지금까지 선택한 edge 수
    cnt = 0
    # 가중치의 합
    total = 0

    # 크루스칼 알고리즘
    # edge를 모두 확인하면서 하나씩 선택(가중치가 작은 것 부터)
    # 추가하다가 사이클이 생디면, 그 다음 간선을 선택
    # 사이클이 안생기도록 제일 작은 간선부터 추가
    # 사이클이 생긴다 == 루트 노드가 같다 == 같은 집합에 속해있다.

    for w,s,e in edges:
        # 간선하나 가져옴 ( 제일 작은 거 부터)
        # 가져왔는데 s정점과 e 정점이 같은 집합에 속해있다.
        # 사이클이 생긴다
        if find_set(s) != find_set(e):
            cnt += 1
            union(s, e)
            total += w
            if cnt == N - 1: #MST구성이 완료되었다.
                break
    print(f'#{tc} {total}')