# 암호코드는 8개의 숫자(앞 7자리 : 고유번호, 마지막자리 : 검증코드)
# 고유번호의 홀수자리*3 + 짝수자리의 합은 10의 배수가 되어야한다.
# 16진수를 2진수로 변환해서 검증해야한다.

num_dict = {'1101': 0, '11001': 1, '10011': 2, '111101': 3, '100011': 4, '110001': 5, '101111': 6, '111011': 7,
            '110111': 8, '1011': 9}
six_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
            'D': 13, 'E': 14, 'F': 15}

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())

    # check 리스트에 암호가 적힌 행만 넣어주기
    check = []
    for _ in range(n):
        s = input()
        if s == '0' * m:
            continue
        else:
            check.append(s)

    # ten리스트에 16진수를 10진수로 변환한 수 넣어주기
    ten = [[0] * m] * len(check)
    for i in range(len(check)):
        for j in range(m):
            ten[i][j] = six_dict[check[i][j]]

    # two리스트에 10진수를 2진수로 변환한 수 넣어주기
    two = [[0] * m] * len(check)
    for i in range(len(check)):
        for j in range(m):
            a = [0] * 4
            k = ten[i][j]
            for v in range(3, -1, -1):
                a[v] = k % 2
                k = k // 2
            two[i][j] = a

    # 한줄씩 문자열로 넣어주기
    pw = ""
    for i in range(len(check)):
        for j in range(m):
            for v in range(4):
                pw += str(two[i][j][v])
    pw = pw.strip('0')

    # 암호를 넣기
    numbers = num_dict.keys()
    result = []
    check_num = ""
    for i in range(len(pw)):
        if pw[i] == '0':
            if len(check_num) == 0:
                continue
            if check_num in numbers:
                result.append(num_dict[check_num])
                check_num = ""
            else:
                check_num += pw[i]
        else:
            check_num += pw[i]

        # 확인해야하는 암호가 주어진 딕셔너리로 해결이 안될 때
        if len(check_num) >= 7:
            pass

        # result의 길이가 8일때 암호가 맞는지 확인
        if len(result) == 8:
            a_number = 0
            for v in range(0, 8, 2):
                a_number += result[v] * 3
                a_number += result[v + 1]
            if a_number % 10 == 0:
                print(f'#{tc} {sum(result)}')
                break
            else:
                result = []