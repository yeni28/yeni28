number = {
    '0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3', '0100011': '4',
    '0110001': '5', '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9',
}

change = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
def Bbit_print(i):
    output = ""
    for j in range(3, -1, -1):
        output += "1" if i & (1 << j) else "0"
    return output


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input().split()) for _ in range(N)]

    for i in range(N):
        # 한 줄 가져오기
        first_row = arr[i]
        row = first_row[0]


        # 한 줄을 가져와서 끝에서부터 검사하는데, 0이 아니면 암호코드가 있다는 소리!
        for j in range(len(row)-1, 0, -1):
            if row[j] != '0':
                break
        else:
            continue
        # 0이 아닌 16진수의 암호코드를 찾았다면 이진수로 바꾸어준다!
        hex_code = ""
        while True:
            if row[j] == '0':
                break
            else:
                hex_code += row[j]
                j -= 1
        h_code = hex_code[::-1]


        # 16진수를 2진수로 바꿔주기

        bin_code = ""
        for i in h_code:
            if '0' <= i <= '9':
                number = int(i)
                bin_code += str(Bbit_print(number))
            else:
                number = int(change[i])
                bin_code += str(Bbit_print(number))

        print(bin_code)




