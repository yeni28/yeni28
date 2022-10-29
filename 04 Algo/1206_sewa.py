T = 10

for i in range(1, T+1): #테스트 케이스만큼 반복
    n = int(input()) #빌딩의 땅 너비

    building = list(map(int,input().split()))

    cnt = 0 # 조망권이 확보된 세대 수
    for i in range(2, n-2): #양쪽 2칸씩이 비어있다.
        height = building[i] # i위치에 있는 빌딩 높이 저장
        for floor in range(height,-1,-1): # 현재 건물의 가장 위층부터 하나씩 검사
            #현재 위치에서 왼쪽 두칸, 오른쪽 두칸 검사
            if floor > building[i-1] and floor > building[i-2] and floor > building[i+1] and floor > building[i+2]:
                cnt += 1
            else:
                #여기 밑에서부터는 검사할 필요가 없다
                break

print(f'#{t} {cnt}')


#상현님은 다섯개를 슬라이싱해서 최댓값을 구하는 방식으로 풀이함
