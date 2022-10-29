def arrive(i, s):
    global answer
    last = 0 # 마지막 충전 위치
    if answer < s:
        return
    if i >= N:
        answer = s
        return
    count = arr[i]
    for j in range(count,0,-1):
        arrive(i+j, s+1)




T = int(input())
for tc in range(1, T+1):
    answer = float('inf')
    arr = list(map(int, input().split()))
    N = arr.pop(0) -1
    arrive(0,-1)

    print(f'#{tc} {answer}')


