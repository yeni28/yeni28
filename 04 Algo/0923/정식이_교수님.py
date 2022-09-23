T = int(input())

for tc in range(1, T+1):
    # 이진수
    b = list(input())
    # 삼진수
    t = list(input())

    answer = -1

    decimal = set()

    # 이진수부터 앞자리 하나씩 바꾸고, 십진수로 변환한 후에 집합에 저장
    for i in range(len(b)):

        # 자리수를 하나 바꾼 이진수 만들기
        new_b = [0] * len(b)
        for j in range(len(b)):
            if j == i:
                new_b[j] =='1' if b[i]=='0' else '0'
            else:
                new_b[j] = b[j]

        # 이진수를 십진수로 바꾸고 세트에 추가
        x = 0
        dec = 0
        for j in range(len(new_b)-1,-1,-1):
            dec += (2**x) * int(new_b[j])
            x += 1
        decimal.add(dec)
    # 삼진수를 십진수로 바꾸고, 그 결과가 세트 안에 있으면 정답 !
    for i in range(len(t)):
        # 자리수 하나 바꾼 삼진수 만들기
        for j in range(3):
            if t[i] != j:
                temp = t[i] #원래 자리수 기억

                t[i] = j
                # 바꾼 다음 십진수로 변환

                x = 0
                dec = 0
                for k in range(len(t)-1,-1,-1):
                    dec += (3**x) * int(t[k])
                    x += 1
                # 바꾼 결과가 십진수 전에 이진수로 계산했던 세트안에 있으면 정답

                if dec in decimal:
                    answer = dec
                # 바꿨던 것 원복
                t[i] = temp
    print(f'#{tc} {answer}')