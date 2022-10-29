dx = [1, -1, -1, 1]
dy = [1, 1, -1, -1]


def search_cafe(x, y):
    q= []
    q.append((x, y))
    max_len = 0
    de_list = []
    while q:
        x, y = q.pop(0)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                q.append((nx, ny))
                if dessert[ny][nx] in de_list:
                    break
                else:
                    de_list.append(dessert[ny][nx])

        if len(de_list) > max_len:
            max_len = len(de_list)

    return max_len





T = int(input())
for tc in range(1, T+1):
    n = int(input())
    dessert = [list(map(int, input().split())) for _ in range(n)]

    ans = search_cafe(0, 0)
print(f'#{tc} {ans}')
