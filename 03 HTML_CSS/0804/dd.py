for i in range(1,11):
    N = int(input())
    build = list(map(int, input().split()))
                 
view = 0
for t in range(2, N-2):
    if build[t] > build[t-1] and build[t]>build[t-2] and build[t] > build[t+1] and build[t] > build[t+2]:
        a1 = build[t] - build[t-2]
        a2 = build[t] - build[t-1]
        a3 = build[t] - build[t+1]
        a4 = build[t] - build[t+2]
        min_gap = a1
        for a in [a1,a2,a3,a4]:
            if a < min_gap:
                min_gap = a
        view += min_gap

print(f'#{i} {view}')
                 
                 