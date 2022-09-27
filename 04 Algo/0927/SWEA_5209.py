T = int(input())

# row_num : 현재 행에서(단계)
#selected : 중복 체크 (세로)
#price : 가격의 합
def backtracking(row_num, selected, price):
    # 더이상 가망이 없는 노드는 탐색하지 않도록
    if price >= min_v:
        return

    # N개 골랐고 , row_num이 인덱스의 범위를 벗어났다면 계싼
    if len(selected) == N and row_num == N:
        min_v = min(min_v, price)
        return


    # i : 열번호
    for i in range(N):
        # 현재 row_num 행에서 i열을 골랐다면,
        # row_num +1 행으로 넘어가서 i 열을 제외한 다른 열을 골라보자
        if i not in selected:
            selected.append(i)
            backtracking(row_num+1, selected, price + factory[row_num])
            selected.remove(i)




for tc in range(1, T+1):
    N = int(input())

    factory = [list(map)

    min_v = 15 * 100
