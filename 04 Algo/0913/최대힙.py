


def enq(n):
    global last
    last += 1
    heap[last] = n

    #만약 새로 추가된 원소가 부모 노드보다 더 커버린 경우 자리를 바꿔줘야한다.
    c = last
    p = c //2

    #부모가 존재하고, 부모보다 자식이 더 크면 자리 바꾸기
    while p and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        # 혹시 바꾸고 난 다음 또 바꿔야 할 수 있으니
        # 부모와 자식을 바꿔준다.
        c = p
        p = c // 2

heap = [0] * 100
last = 0