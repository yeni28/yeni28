T = int(input())

def solve(month, total):
    global minv

    # 인덱스 0 ~ 11 / 월 1 ~ 12
    if month > 11:
        minv = min(total, minv)
        return

    # 일, 월, 3월, 연에 따라 계산
    if plan[month] > 0:
        # 일권 계산
        cost_d = plan[month] * d
        # 월권 계산
        cost_m = m
        # 둘 중에 최소값 사용
        cost = min(cost_d, cost_m)
        # +1 달로 넘어가기(바로 다음달), 비용을 누적시켜서 전달
        solve(month+1, total + cost)
    # 해당월에 사용하는 날이 없다.
    else:
        solve(month+1, total)

    # 3개월권을 쓴 경우
    solve(month + 3, total + m3)
    # 연권
    solve(month + 12, total + y)


for tc in range(1, T+1):
    #일권, 월권, 3월권, 연권
    d, m, m3, y = map(int,input().split())

    #수영장 이용계획
    plan = list(map(int,input().split()))

    #최소값
    minv = 10000000

    solve(0,0)
    print(f'{tc} {minv}')