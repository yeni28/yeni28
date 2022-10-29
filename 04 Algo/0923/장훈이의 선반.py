# 리스트 원소의 합을 부분집합으로 나타내야 함.

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    manager_height = list(map(int, input().split()))
    bit = [0] * N
    gap_list = []
    min_gap = 10000

    for i in range(1, 1<<N):
        s = 0
        #합을 저장할 리스트
        for j in range(N):
            if i & (1<<j):
                s += manager_height[j]
        if s >= B:
            if s - B < min_gap:
                min_gap = s - B
            #B와 가장 차이가 작은 s를 구하면 됨
    print(f'#{tc} {min_gap}')

