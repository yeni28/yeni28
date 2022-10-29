



T = int(input())

# x가 속한 집합의 대표 찾기
def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

# x 집합 , y 집합을 합치는 연산
def union(x,y):
    x = find_set(x) # x집합의 대표
    y = find_set(y) # y집합의 대표

    # 두 집합의 대표가 같다면 합칠 필요가 없다.
    if x == y:
        return

    # x랑 y중에 누구를 대표로 할 것인가?
    # 깊이가 깊은(rank) 가 더 큰 사람을 대표로 할 것이다.
    # 깊이가 깊은  집합을 x라고 하도록 y집합과 비교
    # 깊이가 깊은 집합이 x가 되도록 처리
    if rank[y] > rank[x]:
        x, y = y, x

    # y집합의 대표롤 x로
    p[y] = x

    # 두 집합의 깊이가 같다면 x의 깊이를 1 증가 시켜줘야한다.
    if rank[x] == rank[y]:
        rank[x] += 1


for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N : 사람수
    # M : 페어수 (신청서의 개수)
    # 1-1 매칭 누가 누구와 같은 그룹이 되고 싶다고 신청
    pairs = list(map(int, input().split()))

    # 처음에는 각 집합의 대표가 자기자신
    p = [i for i in range(N+1)]

    # rank를 통해서 서로소집합 합집합연산 최소화
    # rank[i] = i번째 집합의 깊이
    # 합집합 할 때 깊이가 깊은 집합의 대표를 대표로 정한다
    rank = [0] * (N + 1)

    # pair원소를 앞에서부터 두 개씩 쪼개서 신청서 처리
    for i in range(M):
        x = pairs[i * 2]
        y = pairs[i * 2 + 1]
        union(x,y)

    # 각 집합의 대표자가 몇 명인지 구하면 그게 곧 집합의 개수다.
    reps = set()
    # 1부터 N 번까지 각 사라밍 속한 집합의 대표를 구하고 SET에 추가
    for i in range(1, N+1):
        reps.add(find_set(i))
    print(f'#{tc} {len(reps)}')