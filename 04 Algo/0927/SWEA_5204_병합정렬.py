
# 분할과정
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    # for문 돌면서 append를 사용할 시 시간 초과
    # for i in range(len(arr)):
    #     if i < middle:
    #         left.append(arr[i])
    #     elif i >= middle:
    #         right.append(arr[i])

    # for i in range(middle):
    #     left.append(arr[i])
    # for i in range(middle, len(arr)):
    #     right.append(arr[i])

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

#병합과정

def merge(left, right):
    global cnt
    l, r = 0, 0
    i = 0
    result = [0] * (len(left) + len(right))

    if left[-1] > right[-1]:
        cnt += 1

    while l < len(left) or r < len(right):
        if l < len(left)  and r <len(right):

            if left[l] <= right[r]:
                result[i] = left[l]
                i += 1
                l += 1

            else:
                result[i] = right[r]
                i += 1
                r += 1

        elif l < len(left):
            result[i] = left[l]
            i += 1
            l += 1

        elif r < len(right):
            result[i] = right[r]
            i += 1
            r += 1

    return result



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    print(f'#{tc} {merge_sort(arr)[N//2]} {cnt}')
