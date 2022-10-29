
def selection_sort(arr):
    # 0번 인덱스부터 제일 작은(제일 큰) 원소를 찾아서 채워나가는 방식
    for i in range(len(arr)-1):
        min_idx = i
        # i 의 다음 위치부터 비교를 하면서 제일 작은 원소의 위치를 찾고, 배열 순회가 끝나면 자리를 바꾼다.
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j #최소값 위치 기억
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def selection_sort2(arr,i):

    # 재귀적 정의

    # 기저 조건(범위에 따라 종료시켜줄 수 있도록)
    if i >= len(arr):
        return
    # 작은 문제의 결과를 통해 큰 문제를 해결하는 유도 조건

    #현재위치가 0일때부터 길이 -1 위치를 찾는다.
    # 작은 문제는 현재위치가 i 일때의 그 위치에 맞는 원소를 찾아 자리를 바꾼다.

    min_idx = i #최소 원소의 위치를 일단 i로 시작
    for j in range( i+1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

    #============================================
    # i 다음 위치로 가서 그 위치에 맞는 최소값으 찾아 바꾸는 일을 한다.
    selection_sort2(arr, i+1)
