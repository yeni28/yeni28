T = int(input())

for tc in range(1, T+1):
    n = float(input())
    b = ""
    # 자릿수 계산을 위해
    cnt = 0

    #반복문을 돌면서 이진수로 바꾸기
    # 원래 수 * 2한 결과가 1 이상==> 이진수 1 추가하고, 1을 빼준 뒤 계산이어나감
    # else, 이진수 0
    while cnt < 13 and n!= 0:
        n *= 2
        cnt += 1
        if n >= 1:
            b += '1'
            n = n - 1

        else:
            b += '0'

        if c