T = int(input())

for case in range(0,T+1):
    N = int(input())
    cards = input()
    card_list = []
    for card in cards:
        card_list.append(int(card))

    print(card_list)
    # card_list = [4,9,6,7,9]
    card_count = [0] * 10

    print(card_list[5])
    # print(card_count) = [0,0,0,0,0,0,0,0,0]

    # for idx in range(0, N+1):
    #     card_count[card_list[idx]] += 1


print(card_count)

