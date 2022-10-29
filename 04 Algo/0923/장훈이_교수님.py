T = int(input())

for tc in range(1, T+1):
    N, B = map(int,input().split())

    p = list(map(int,input().split()))

    answer = 10000 * 21
    for i in range(1<<N):
        min_h = 0
        #j번째 원소가 포함되어있는지 확인
        for j in range(N):
            if i & (1<<j):
                min_h += p[j]
    