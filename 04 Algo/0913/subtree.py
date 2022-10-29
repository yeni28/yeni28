T = int(input())
for tx in range(1, T+1):
    e, n = map(int,input().split())

    #노드(트리)를 표현하기 위한 배열
    # 왼쪽
    c1 = [0] * (e + 2)
    c2 = [0] * (e + 2)

    #간선정보
    edges = list(map(int,input().split()))
    for i in range(0, e*2, 2):
        p = edges[i]
        c = edges[i + 1]

        #트리 만들어주기
        # 왼쪽 자식이 없다 => 왼쪽에 추가
        # 왼쪽 자식이 있따 => 오른쪽에 추가

    # 노드의 개수를 세기 시작
    # 중위순회, 후위순회, 전위순회
    # 자식노드가 없으면 탐색을 중지
    # c1[node] != 0:
    #   preorder(c1[node]) 전위순회의 경우우