#입력문제
#입력이 어떻게 들어오는가?

# 맨 첫줄에 테스트 케이스의 개수가 입력됩니다.
# 우리가 적용시켜야할 상황의 개수가 몇개인지

testcase = int(input())

# 테스트 케이스의 개수만큼 반복
# 그 반복 안에서 문제의 풀이를 작성

for t in range(1, testcase+1):
    # 상자가 몇개씩 들어오나?
    # n =>방의 너비 (탑이 최대로 들어올 수 있는 개수)
    n = int(input())
    # 상자의 형태(탑의 높이가 리스트로 주어진다.)
    # 7 4 2 0 0 6 7
    # 파이썬의 입력은 모두 문자열
    # 리스트 형태로 받아서 사용을 할 것이다.

    #문자열을 모두 숫자로 바꿔주는 처리까지 필요하다.


numbers = list(map(int,input().split()))
# 상자의 맨 위 꼭대기 층에서 오른쪽에 상자 탑이 존재하는 지
# 오른쪽에 빈칸이 몇 개 있는지를 세서
# 그 빈칸 중 최댓값을 구하면 ==> 낙차의 최댓값을 구할 수 있다.
answer = 0

for i in range(n):
    number = numbers[i] #상자의 최대 높이(꼭대기층 상자)
    count = 0 #빈칸의 개수

    for j in range(i+1,n):
        if number <= numbers[j]:
            #오른쪽에 있는 상자의 높이가 지금 내 높이보다 크거나 같으면 장애물이 있음. 빈칸이 아니니까 세지 않는다.
        else:
            #지금 내 높이보다 작으니까 빈칸이다.
            count += 1
    answer =  count if count > answer else answer #count의 최댓값 구하기


print(answer)

