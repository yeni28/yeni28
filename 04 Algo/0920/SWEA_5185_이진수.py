change = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

def Bbit_print(i):
    output = ""
    for j in range(3,-1,-1):
        output += "1" if i & (1 << j) else "0"
    return output

T = int(input())

for tc in range(1, T+1):
    ans = ""
    N, num = input().split()
    for i in num:
        if '0' <= i <= '9':
            number = int(i)
            ans += str(Bbit_print(number))
        else:
            number = int(change[i])
            ans += str(Bbit_print(number))
    print(f'#{tc} {ans}')



