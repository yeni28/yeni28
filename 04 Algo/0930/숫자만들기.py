# 하다 실패함
def perm(idx, check):
    if idx == (N-1):
        print(cal)
        return
    for j in range(N-1):
        if check & (1<<j):
            continue
        cal[idx] = cals[j]
        perm(idx+1, check | (1<<j))



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cal = [0] * (N - 1)
    cals = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    cal_list = []



print(cals_list)
