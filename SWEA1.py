T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    scores = list(map(int,input().split()))
    cnt = [0] * 101

    for score in scores:
        cnt[score] += 1
    
    maxV = 0

    for i in range(0,len(cnt)):
        if cnt[i] >= maxV:
            maxV = cnt[i]
            maxidx = i
    print(f'#{test_case}{maxidx}')

