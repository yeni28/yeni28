T = int(input())

for tc in range(1, T+1):
    bi_num = list(input())
    tri_num = list(input())

    bi_stack = [0] * len(bi_num)
    tri_stack = [0] * len(tri_num)

    for b in range(len(bi_num)):
        for t in range(len(tri_num)):
            if bi_num[b] == 0:
                bi_num[b] = 1
            else:
                bi_num[b] = 0

            print(bi_num)


                # if int(bi_num2,2) == int(tri_num2, 3):
                #     ans = int(bi_num2, 2)
                #     print(ans)
    # print(f'#{tc} {ans}')