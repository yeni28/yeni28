
# data = [0,4,1,3,1,2,4,1]

# # # 숫자의 종류만큼 방을 만들어 줘요
# # cnt = [0] * 5

# # # 빈 방에 숫자들을 집어 넣어요
# # for i in data:
# #     cnt[i] = cnt[i] + 1 

# # # cnt = [1, 3, 1, 1, 2]
# # # 이제..방에 숫자가 몇개있는지 세볼까나..


# # for j in range(len(cnt)-1):
# #     cnt[j+1] = cnt[j] + cnt[j+1] 

# # tmp = [0] * len(data)

# # for idx in range(len(data)-1,0,-1):
# #     cnt[data[idx]] -= 1
# #     tmp[cnt[data[idx]]] = data[idx]

# # print(tmp)
# # x, y = y, x
# for j in range(len(data)-1,1,-1):
#     for i in range(j):
#         if data[i] > data[i+1]:
#             data[i],data[i+1] = data[i+1],data[i]

# print(data)

tall_size = [20,7,23,19,10,15,25,8,13]
result = sum(tall_size)
print(result)

for k in range(len(tall_size)-1):
    for j in range(k+1,len(tall_size)):
        sum_two = tall_size[k] + tall_size[j]
        
       
print(sum_two)
=======
p = 'is'
t = 'this is a book~!'
M = len(p)
N = len(t)


def BruteForce(p, t):
    i = 0 #t의 인덱스
    j = 0 #p의 인덱스
    while j < M and i < N :
        if t[i] != p[j]:
            i = i = j
            j = -1
        i = i + 1
        j = j + 1
    if j == M : return i - M #검색 성공!
    else : return -1 #검색 실패


print(BruteForce(p, t))
