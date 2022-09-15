def inorder(n):
    global answer
    if n:
        inorder(left[n])# 0이면 알아서 리턴해서 튀어나옴../ 왼쪽의 서브트리로 가보렴
        answer += str(tree[n])
        inorder(right[n])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    left = [0] * (N+1) #부모를 인덱스로 왼쪽 자식 저장
    right = [0] * (N+1) #부모를 인덱스로 오른쪽 자식 저장
    tree = [0] * (N+1) # 노드 데이터 저장
    for i in range(1, N+1):
        p = i #부모번호
        tree[p] = i # 데이터
        if len(arr) >= 3: #왼쪽자식이 존재하는 모든경우
            left[p] = int(arr[2]) # 왼쪽 자식
        if len(arr) == 4:
            right[p] = int(arr[3]) #오른쪽 자식

    answer = ''
    inorder(1)
    print(f'#{tc} {answer}')