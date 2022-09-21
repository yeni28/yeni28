def f(n,cnt):
    global maxV
    if i == cnt:
        tmp = int(''.join(num))
        if maxV < tmp:
            maxV = tmp
    else:
        for i in range(len(num)-1):
            for j in range(i+1, len(num)):
                num[i], num[j] = num[j], num[i]
                tmp = int(''.join(num))
                # 중복된 수 제거
                if tmp not in u[n]:
                    u[n].appen(tmp)
                    f(n+1,cnt)
                num[i], num[j] = num[j], num[i]

T = int(input())
for tc in range(1, T+1):
    num, cnt = input().split()
    num = list(num) #리스트로 숫자 받기
    cnt = int(cnt) #교환 횟수
    maxV = 0 #최댓값 구하기
    u = [[]* for _ in range(10)] #중복 노드 방지
    f(0,cnt)
    print(f'#{tc} {maxV}')