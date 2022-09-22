



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 각 칸에 값을 저장
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 중간까지의 합을 다시 계산하지 않도록 기억해놓는 방법을 이용

    dp  = [[0] * N for _ in range(N)]
    # dp의 각 칸의 숫자는 그 칸 까지 왔을 때의 최소합의 저장 값이다.

    # 이동방향은 왼-> 오, 위-> 아래
    for i in range(N):
        for j in range(N):
            # 현재 i,j 위치일때 위에서도 올 수 있고, 왼쪽에서도 올 수 있다.
            if i-1 >= 0 and j-1 >= 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + arr[i][j]
                # 위에서만 올 수 있고, 왼쪽에서는 올 수 없다.
            elif i-1 >= 0 and j - 1 < 0:
                dp[i][j] = dp[i-1][j] + arr[i][j]
                # 왼쪽에서만 올 수 있고 위엣는 올 수 없다.
            elif i-1 < 0  and j-1 >=0:
                dp[i][j] = dp[i][j-1] + arr[i][j]
            elif i - 1 <0 and j - 1 <0:
                dp[i][j] = arr[i][j]
    # 반복이 다 끝나면 맨 오른쪽 아래칸에는 최소값이 들어있을 것이다.
    print(f'#{tc} {dp[N-1][N-1]}')