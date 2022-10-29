T = int(input())

for tc in range(1, T+1):
    N = int(input())
    x = N ** (1/3) #x는 N의 세제곱근
    num = int(x)
    if x + 0.01 >= num + 1: # 일정차이로 인해 float로 나타나는 수를 정수로 만들어주기
        answer = int(x + 0.1)
    elif x < 0 or N % x != 0: # 0보다 작거나 나눠지지 않으면
        answer = -1 # -1을 출력한다.
    else:
        answer = x # 나누어 떨어지면 x값을 출력
    print(f'#{tc} {int(answer)}') # int값으로 실수를 정수로 보정한다

