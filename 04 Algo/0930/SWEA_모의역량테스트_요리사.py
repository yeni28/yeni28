def comb(arr,n): #조합을 구해주는 함수입니다.
    result = []
    if n > len(arr):
        return result
    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr) - n+1):
            for j in comb(arr[i+1:], n-1):
                result.append([arr[i]] + j)
    return result

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    a = N//2
    s = [list(map(int, input().split())) for _ in range(N)]
    min_v = 20000


    #일단 두짝으로 나누기 / 두개의 요리로 나누기 위해 식재료를 나누는 작업
    arr = [] # 식재료의 수(인덱스)를 받아줄 리스트
    for m in range(N): # for문 돌면서 인덱스 받아주기
        arr.append(m)
    group = [] # 부분집합을 받아줄 리스트
    for k in range(1 << N):
        sub = []
        for h in range(N):
            if k & (1 << h):
                # j 번째 원소가 부분집합에 포함되어 있다면 추가한다.
                sub.append(arr[h])
            if len(sub) == N // 2: # 식재료들을 매번 반틈 자르니까 그만큼의 길이만.
                if sub not in group: # 중복 제거해주기
                    group.append(sub)
    print(group)

                    # 이 작업이 끝나면 12,34 처럼 두짝으로 나뉩니다.


    # 원소가 다른 것들끼리 짝지어주기 / 나눈 식재료들 끼리 조합하는 작업
    pair = [] #이제 두개로 나눈 것들을 하나의 리스트로 또 짝지어줄겁니다.
    for g1 in group: # 둘로 나뉜 그룹을 순회하면서
        for g2 in group: #
            if g1 != g2: # 만약 두 그룹이 같지않고 [1,2] != [1,2]
                cnt = 0 # 카운트 초기화
                for i in g1: # 두 그룹의 원소가 포함되어있지않다면
                    if i not in g2: #[1,2] [3,4]인 상태라면
                        cnt +=1 # 카운트를 더해주는데,
                        if cnt == N//2: # 그게 둘로 나뉜 식재료의 길이와 같아지면
                            pair.append([g1,g2]) # 페어로 각각 추가해줍니다
    print(pair)

    # 페어로 나뉜 리스트를 돌면서 이제 시너지를 더해줘요
    for p in range(len(pair)):
        m1 = comb(pair[p][0],2)
        m2 = comb(pair[p][1],2)
        sum_m1 = 0
        sum_m2 = 0

        for i in range(len(m1)): # A음식
            sum_m1 += s[m1[i][0]][m1[i][1]] + s[m1[i][1]][m1[i][0]]
        for i in range(len(m2)): # B음식
            sum_m2 += s[m2[i][0]][m2[i][1]] + s[m2[i][1]][m2[i][0]]
        ans = abs(int(sum_m2)-int(sum_m1))
        if ans < min_v:
            min_v = ans

    print(f'#{tc} {min_v}')

