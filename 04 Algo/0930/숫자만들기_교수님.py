T = int(input())

# 연산자 사용가능한 횟수(남은 개수): opers
# 내가 지금까지 골라온 연산자 : exp
# 현재 자리에 채워넣을 연산자, 현재 자리 번호 : idx
def solve(opers, exp, idx):
    global minv, maxv

    if idx == N - 1:
        # 내가 선택했던 연산자
        exp = list(exp)

        # 연산자, 숫자를 통해서 식을 계산
        ni = 0
        result = nums[ni]

        # 연산자 하나씩 꺼내고, 숫자도 하나씩 꺼내서 결과 계산
        while exp:

            ni += 1
            right = nums[ni]
            op = exp.pop()
            if op == '+':
                result += right
            if op == '-':
                result -= right
            if op == '*':
                result *= right
            if op == '/':
                result = int(right/right)

        if minv > result:
            minv = result
        if maxv < result:
            maxv = result
        return

    # 현재 자리에 넣을 수 있는 연산자 넣기
    # 남은 개수가 0개 이상이면 넣을 수 있다.

    # +
    if opers[0] > 0:
        opers[0] -= 1
        solve(opers, exp+"+", idx + 1)
        opers[0] += 1
    # -
    if opers[1] > 0:
        opers[1] -= 1
        solve(opers, exp+"-", idx + 1)
        opers[1] += 1

    # *
    if opers[2] > 0:
        opers[2] -= 1
        solve(opers, exp+"*", idx + 1)
        opers[2] += 1

    # /
    if opers[3] > 0:
        opers[3] -= 1
        solve(opers, exp+"/", idx + 1)
        opers[3] += 1




for tc in range(1, T+1):
    N = int(input())
    # 연산자 사용 가능횟수
    # operations[0] : + 사용 가능 횟수
    # operations[1] : - 사용 가능 횟수
    # operations[2] : * 사용 가능 횟수
    # operations[3] : / 사용 가능 횟수

    operations = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    # 최대값, 최소값
    maxv = -100000001
    minv = 100000001

    solve(operations,"",0) #연산자, ,연산자가 들어갈 위치

    print(f'#{tc} {maxv - minv}')