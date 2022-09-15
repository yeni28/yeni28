def inorder(v):
    if v <= N:
        inorder(v * 2) #왼쪽 서브트리의 루트로 이동
        answer.append(tree[v])
        inorder(v * 2 + 1) #오른쪽 서브트리의 루트로 이동

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N + 1)
    for i in range(1,N+1): #1부터 N까지 자연수 값을 저장
        tree[i] = i
    answer = []
    inorder(1) #완전이진트리의 루트부터 순회
    root = 1

    for k in range(N):
        if answer[k] == 1:
            root_value = k + 1
        elif answer[k] == N//2 : # N//2 의 값
            node_value = k+1

    print(f'#{tc} {root_value} {node_value}')