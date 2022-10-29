T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())

    # 컨테이너의 무게
    w = list(map(int,input().split()))

    # 트럭의 중량
    t = list(map(int, input().split()))

    #greedy? 큰 컨테이너 부터 큰 트럭에 담아 옮긴다

    # 각 배열을 내림차순으로 정렬하면 0번부터 확인하면 된다.
    w.sort(reverse=True)
    t.sort(reverse=True)

    # 배열의 원소가 1이다 => 해당 인덱스의 화물을 보냈다.
    # 해당 인덱스의 트럭을 보냈다.
    moved

    # 트럭 보냈나 체크

    #옮긴 화물 총 중량
    moved = 0

    while move:
        #남은 트럭 없으면 이동 불가
        if 0 not in moved_t:
            move = False
            break
        # 남은 트럭 중 가장 큰 트럭
        ti = 1
        for i in range(M):
            if moved_t[i] == 0:
                ti = i
                #트럭이 이동했다고 체크
                moved_t[i] = 1
                break
        #보낼 컨테이너가 없다면 이동 불가
        if 0 not in moved_w:
            move = False
            break
        # 남은 컨테이너중에 가장 큰 컨테이너, 실을 수 있는(트럭의 중량)
        for i in range(N):
            if moved_w[i] == 0 and w[i] <= t[ti]:
                moved += w[i]
                #해당 컨테이너를 옮겼다고 체크
                moved_w[i] = 1
                break
        else:
            # 남은 컨테이너 중에서 트럭에 실을 수 있는 게 없다.
            move = False
            break
    print(f'#{tc} {moved}')