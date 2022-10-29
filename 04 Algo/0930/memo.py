def pick(n, bucket, k):
    if k == 0:
        print(*bucket)
        return

    lastIndex = len(bucket) - k - 1

    if len(bucket) == k:
        smallest = 0
    else:
        smallest = bucket[lastIndex] + 1
    for i in range(smallest, n):
        bucket[lastIndex + 1] = i
        pick(n, bucket, k - 1)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    selected = [[0]* N for _ in range(N)]
    s = [list(map(int, input().split())) for _ in range(N)]
    min_v = 20000
    # backtracking(0,[],0)
    # print(f'#{tc} {min_v}')

    #일단 두짝으로 나누기
    arr = []
    for m in range(1,N+1):
        arr.append(m)
    group = []
    for k in range(1 << N):
        sub = []
        for h in range(N):
            if k & (1 << h):
                # j 번째 원소가 부분집합에 포함되어 있다.
                sub.append(arr[h])
            if len(sub) == N // 2:
                if sub not in group:
                    group.append(sub)

    # 원소가 다른 것들끼리 짝지어주기
    pair = []
    for g1 in group:
        for g2 in group:
            if g1 != g2:
                cnt = 0
                for i in g1:
                    if i not in g2:
                        cnt +=1
                        if cnt == N//2:
                            pair.append([g1,g2])
    # print(pair)

    print(pick(len(pair[0]),pair[0],2))
