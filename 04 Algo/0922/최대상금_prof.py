# 최적화 하지 않은 상태
T = int(input())

# cnt : 카드를 교환한 횟수
def card_swap(cnt):
    global max_val
    # 중단조건
    # 교환 횟수를 다 썼으면 그 때 최대 상금을 구하면 된다.

    if cnt == n:
        num = int(''.join(s))
        max_val = max(max_val, num)
        return # 함수종료
    # 부분문제
    # 교환횟수가 남았으면 카드를 바꾸기
    # 교환시작 위치 i, 교환 대상위치 j 정하기
    for i in range(len(s)-1): # 뒤에 바꿀 카드가 하나는 남아있어야 함
        for j in range(i+1, len(s)): #j는 i보다 뒤에있다.
            s[i],s[j] = s[j], s[i]
            # 교환한 상태로 다음 교환으로 넘어가기
            card_swap(cnt+1)
            # 계산 했으면 교환 전의 상태로 되돌린다.(?)
            s[i],s[j] = s[j], s[i]


for tc in range(1, T + 1):
    s, n = input().split()
    s = list(s)
    n = int(n)

    # 똑같은 자리에서 교환 중복을 허용한다고 했지만,
    # 결국 우리가 해당 자리수로 만들수 있는 숫자는
    # 해당 자리수만큼 교환을 실행한 결과와 같을 것이다.
    # 주어진 교환 횟수가 카드의 수(숫자의 자리수) 보다 커지면 의미가 없어진다.
    # 그 경우에는 교환 횟수를 카드의 수로 제한

    if n > len(s):
        n = len(s)
    # 카드로 만들 수 있는 최대 값
    max_val = 0

    # 교환 횟수 0번부터 답을 구하기 시작
    card_swap(0)

    print(f'#{tc} {max_val}')

