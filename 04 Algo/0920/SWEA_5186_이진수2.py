

T = int(input())

for tc in range(1, T+1):
    ans = ""
    N = float(input())

    while True:
        N *= 2
        if N >= 1:
            N = N - 1
            ans += '1'
        else:
            ans += '0'

        if N == 0:
            break
    if len(ans) >= 13:
        ans = 'overflow'

    print(f'#{tc} {ans}')
