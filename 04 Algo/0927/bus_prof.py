T = int(input())

# idx 현재위치, cnt 충전횟수
def backtracking(idx, cnt):
    global min_v

    if idx == N-1:
        min_v = min(min_v,cnt)
        return

    #현재 위치에서 갈 수 있는 곳 가기
    for i in range(1,bus_stop[idx] + 1):
        backtracking(idx + i, cnt + 1)


for tc in range(1, T+1):
    answer = float('inf')
    arr = list(map(int, input().split()))
    N = arr[0]
    bus_stop = arr[1:] + [0]
    min_v = 101

    backtracking(0,-1) #함수에서 충전횟수를 0부터 하도록 했기 때문임

    print(f'#{tc} {answer}')
