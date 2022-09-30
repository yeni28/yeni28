T = int(input())
def make_recipe():
    # 부분집합 구하기
    for i in range(1<<N):
        # j번째 원소가 포함되어 있는지 검사
        # i번째 레시피가 재료를 N//2개 사용해야 한다.
        s_set = set()
        for j in range(N):
            # j를 왼쪽으로 한칸씩 밀면서 j번 째 칸에 원소가 있는지 검사
            if i & (1 << j):
                s_set.add(j)
        #부분집합의 원소의 개수가 N/2개인 부분집합 고르기
        if len(s_set) == N2:
            recipes.add(tuple(s_set))



for tc in range(1, T+1):
    N = int(input())
    N2 = N //2

    synergy = [list(map(int, input().split())) for _ in range(N)]

    recipes = set() #레시피 목록(음식재료 수 : N//2)
    used = set() # 사용한 레시피는 나중에 사용 x
    min_v = 10000000 # 최소값

    # 재료를 N//2개 사용해서 만들 수 있는 음식의 가지수
    # 원소의 개수가 N인 것 중에서 부분집합의 크기가 N//2 인 것 골라서 사용
    make_recipe()

    for r in recipes:
        #A를 만드는 데 쓰는 재료는 r
        #B를 만드는 데 쓰는 재료를 N - r

        #레시피 r을 사용해서 A를 만든적이 있다면 다음으로 넘어감(중복체크)
        if r in used:
            continue
        used.add(r)

        # A를 만들 때 쓴 재료 말고 나머지를 이용해서 B를 만든다.
        br = []
        for i in range(N):
            if i not in r:
                br.append(i)
        br = tuple(br)
        #br 레시피로 B를 만든적이 있으면 다음으로 넘어간다.
        if br in used:
            continue
        used.add(br)

        # A의 맛
        favor_a = 0
        for i in range(N2):
            s1 = r[i]
            for j in range(i+1, N2):
                s2 = r[j]
                favor_a += synergy[s1][s2] + synergy[s2][s1]

        # B의 맛
        favor_b = 0
        for i in range(N2):
            s1 = br[i]
            for j in range(i+1, N2):
                s2 = br[j]
                favor_b += synergy[s1][s2] + synergy[s2][s1]

        # 두 음식의 맛 차이 구하기
        val = abs(favor_a - favor_b)
        min_v = min(min_v, val)

    print(f'#{tc} {min_v}')
