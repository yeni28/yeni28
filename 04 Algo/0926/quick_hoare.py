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




A = [7, 2 ,5, 3, 4, 5]
N = len(A)
qsort(0, N-1)
print(A)


# [[4,5],[2,3],[2,1]] 에서 뒤의 값을 기준으로 정렬하라고 했을 때,
# 슈도코드에서 compare라고 적혀있는 것을 발견할 수 있다.
# 현재는 1차원 배열이지만 아닌 경우에는 파티셔닝 내부에 비교하는 함수를 만들어서 별도로 비교하도록 할 수도 있다.
# pivot을 정할때 A[l][1] 이라든지, 비교할 인덱스만 정렬에 맞게 작성해주면 된다.(비교하는 부분만 변경해주도록)