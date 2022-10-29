def postorder(v): #후위순회(좌/우값으로 부모노드 값을 출력하므로)
    global answer
    if v <= N:
        postorder(v * 2) #왼쪽 서브트리의 루트로 이동
        postorder(v * 2 + 1) #오른쪽 서브트리의 루트로 이동
        answer.append(int(tree[v]))


T = int(input())
answer = []
node = []
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1) #완전 이진트리를 만들자
    for i in range(M):
        arr = input().split()
        tree[int(arr[0])] = arr[1] #인덱스 번호에 데이터를 저장한다.
    postorder(1)
    print(answer)

    #내가 구하고 싶은 값 : L 노드번호에 있는 값

    # print(f'#{tc} {}')