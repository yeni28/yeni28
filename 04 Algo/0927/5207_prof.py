
T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    R = 1
    L = 0
    A.sort()

    #조건에 맞으면서 A안에서 찾은 B의 원소 개수

    cnt = 0

    for number in B :
        left = 0
        right = N - 1
        dir = -1 # 처음 시작할 때는 방향이 없는 상태
        while left <= right:
            mid = (left + right )//2
            # 답 찾으면 개수 증가
            if A[mid] == number:
                cnt += 1
                break
            # 찾는 범위를 왼쪽으로 제한
            elif A[mid] > number:
                right = mid - 1
                # 내가 이전에 선택한 범위가 왼쪽이었다.
                # 조건 위반임
                # 탐색 중지하고 다으믕로 넘어가기
                if dir == L:
                    break
                dir = L
            # 찾는 범위를 오른쪽으로 제한
            else:
                left = mid +1
                # 내가 이전에 선택한 범위가 오른쪽이었다.
                # 탐색 중지하고 다음으로 넘어가기
                if dir == R:
                    break
                dir = R
    print(f'#{tc} {cnt}')