def partition(l,r):
    # 초기의 피봇값이 중간값이나 오른쪽으로 하면 이 부분의 코드가 달라지니 감안해서 보길
    pivot = A[l]
    i, j = l, r
    while i <=j:
        while i<=j and A[i] <= pivot:
            i += 1
        while i<=j and A[j] >= pivot:
            j -= 1
        if i < j :
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j

def  qsort(l, r):
    if l < r:
        s = partition(l,r)
        qsort(l, s-1)
        qsort(s+1, r)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    qsort(0, N - 1)
    print(f'#{tc} {A[N//2]}')

