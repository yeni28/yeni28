#답이 잘 안나옴 수정 필요
def merge_sort(m):
    if len(m) == 1:
        return arr
    # 왼쪽 :  left, 오른쪽 :right
    left = right = []
    #가운데
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    #왼쪽 오른쪽 분할정복
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    global cnt


    ln = len(left) # 0 <= li < ln
    rn = len(right) # . <= ri <rn

    #합병하기 전에 left 제일 끝, right의 제일 끝을 비교한다.
    if left[ln-1] > right[rn-1]:
        cnt += 1

    # 왼쪽에서 다음에 꺼내올 원소의 위치 : li
    # 오른쪽에서 다음에 꺼내올 원소의 위치 : ri

    li = ri = 0
    result = []
    while li < ln or ri < rn : # li 가 끝까지 가면 더이상 꺼내올 게 없음. 반복문 탈출
        if li < ln and ri < rn : # 아직 왼쪽에도 꺼낼 게 남아있고 오른쪽에도 남아있다면
            if left[li] <= right[ri]:
                result.append((left[li]))
                li += 1
            else:
                result.append(right[ri])
                ri += 1
        elif li < ln:
            result.append(left[li])
            li += 1
        elif ri < rn:
            result.append(right[ri])
            ri += 1
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    sorted_arr = merge_sort(arr)

    print(f'#{tc} {merge_sort(arr)[N//2]} {cnt}')
