def make_tree(n):

    if n > N :
        return 0
    else:
        if tree[n] != 0:
            return tree[n]
        else:
            left = make_tree(2*n)
            right = make_tree(2*n+1)
            tree[n] = left + right
            return tree[n]

T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)

    for i in range(M):
        idx, n = map(int, input().split())
        tree[idx] = n

        make_tree(1)
        print(f'#{tc} {tree[L]}')