def binarySearch(arr,l,h, key):
    global warigari
    global check
    if l > h:
        return 0
    else:
        mid = (l+h) // 2
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            warigari[check] = check
            check += 1
            return binarySearch(arr, l, mid-1, key)
        else:
            warigari[check] = check
            check += 1
            return binarySearch(arr, l, mid + 1, key)



T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    num_n = list(map(int, input().split()))
    num_m = list(map(int, input().split()))

    key_nums = []
    # 어떻게 이동하는지 체크해보기
    check = 0
    warigari = [0] * N

    # 공통 숫자 뽑기
    for i in num_m:
        if i in num_n:
            key_nums.append(i)

    # 공통 수 j를 A 리스트에서 이진탐색 하려한다.
    for j in key_nums:
        binarySearch(num_n, 0, N-1, j)

        cnt = 0  # 초기화
        for w in range(10):
            if warigari[w] > 0:
                cnt += 1  # 연속한 수가 몇 개인지 확인
                if cnt >= 3:
                    winner = 2
                    break
            else:  # 연속이 끊기면 0으로 초기화
                cnt = 0
        else:
            continue  # 이중 포문 탈출을 위한 컨티뉴
        break  # 이중 포문 탈출을 위한 브레이크




    # 정수가 각 숫자 리스트에 공통으로 있으면서
    # 탐색을 진행할 때, 양 쪽 구간을 번갈아 선택해야한다(오-오 / 왼-왼 안됨)
    # 이 조건을 만족하는 숫자의 개수는?