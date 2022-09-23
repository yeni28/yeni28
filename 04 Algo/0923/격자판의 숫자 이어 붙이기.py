dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y):
    q = []
    q.append((x,y))
    while q:
        x,y = q.pop(0)
        for d in range(4):
            # 여섯 번 이동해야 하는 데 어떻게 여섯번 이동시켜줄 수 있을까?





T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int,input().split())) for _ in range(4)]
