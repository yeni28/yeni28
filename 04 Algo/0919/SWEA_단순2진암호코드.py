number = {
    '0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3', '0100011': '4',
    '0110001': '5', '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9',
}

T = int(input())
for tc in range(1, T + 1):
    answer = 0
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    for i in range(N - 5):
        temp_str = ''
        if answer: break
        for j in range(M - 1, -1, -1):
            if answer: break
            if M - 55 < 0: break
            if arr[i][j] == '0': continue
            temp_array = arr[i][j - 55: j + 1]
            for z in range(8):
                temp_num = number.get(temp_array[z * 7:(z + 1) * 7], -1)
                if temp_num == -1:
                    break
                else:
                    temp_str += temp_num
                    if len(temp_str) == 8:
                        for k in range(4):
                            if temp_array != arr[i + k + 1][j - 55: j + 1]: break
                        else:
                            check_num = 0
                            for k in range(0, 7, 2): check_num += int(temp_str[k])
                            check_num *= 3
                            for k in range(1, 8, 2): check_num += int(temp_str[k])
                            if not check_num % 10:
                                for k in range(8):
                                    answer += int(temp_str[k])
                                break

    print(f'#{tc} {answer}')
