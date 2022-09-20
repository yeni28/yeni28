number = {
    '0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3', '0100011': '4',
    '0110001': '5', '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9',
}

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    sum = 0
    arr = [list(map(int,input())) for _ in range(n)]

    for i in range(n):
        # 한 줄 가져오기
        row = arr[i]

        # 한줄을 가져와서 끝에서부터 검사하는데, 1을 발견한 순간 암호코드가 있다는 소리
        end = -1 #1을 발견한 끝 지점
        for j in range(len(row)-1,0,-1):
            if row[j] == 1:
                end = j
                break
        else:
            #중간에 1을 만났다면 break, 1을 만나지 못했다면 암호가 없다!
            #다음줄 검사로 넘어가기
            continue
        # 중간에 1을 찾았다면 암호 추출 (길이는 56고정)
        code = []
        for j in range(end - 55, end + 1):
            code.append(row[j])

        # 추출한 암호를 복호화, 숫자 1부터 세니까 0번 인덱스를 채우고 시작
        nums = [-1]
        for j in range(0,56,7):
            numbers = ""
            for k in range(7):
                numbers += str(code[j+k])
            nums.append(number[numbers])

        # 만든 코드가 제대로된 암호인지 검사
        odd = 0
        even = 0
        for j in range(1,9):
            if j % 2 == 0:
                even += nums[j]
            else:
                odd += nums[j]
        # 홀수 * 3 + 짝수 = 10의 배수
        if (odd*3 + even) % 10 == 0:
            sum = odd + even
        else:
            sum = 0
        #암호를 검사했으니, 다른줄은 살펴볼 필요 없음
        break
    print(f'#{tc} {sum}')