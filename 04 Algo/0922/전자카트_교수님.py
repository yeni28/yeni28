
T = int(input())

def patrol(now, e_sum):
    global min_value
    # 지금 구한 합이 내가 알고있는 최소값보다 크면 더이상 진행할 필요가 없다.
    # 이후에 더해봤자 커지면 더 커질 뿐이므로 최솟값이 될 가능성이 없다.

    if e_sum < min_value:
    # 모든 방을 다 방문했으면 시작지점으로 돌아간다.
    #시작 지점까지 걸리는 양 추가해서 최소값을 계산
        if 0 not in visited:
            min_value = min(min_value, e_sum + e[now][0])
            return


    # 현재 위치에서 갈 수 있는 다음 방을 탐색

    for next_room in range(N):
        if next_room != now and visited[next_room] == 0:
            # 다음방으로 갔다고 체크하고 길을 차즌ㄴ다.
            visited[next_room] = 1
            # 합을 최신화 한 다음 재귀 호출
            patrol(next_room, e_sum + e[now][next_room])
            # 방문 체크 해제하고 다른 길 있나 찾아보기
            visited[next_room] = 0

for tc in range(1, T+1):
    N = int(input())
    # 각 칸에 값을 저장
    e = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N

    # 처음 방은 출발 이후에 다시 돌아오면 안되니, 마지막 방 방문이후에만 오도록

    visited[0] = 1
    min_value = 10000
    patrol(0,0)