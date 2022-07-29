import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())
for test_case in range(1, T + 1):
    card_n = list(input()) # int 하면 -때매 valueerror
    #card_n.remove('-') # 첫번째꺼 없어서 에러
    #print(card_n)
    start_w = ['3', '4', '5', '6', '9']
    for i in card_n:
        if i == '-':
            card_n.remove(i)
    # print(card_n)
    if card_n[0] not in start_w or len(card_n) < 16:
        print(f'#{test_case} {0}')
    else:
        print(f'#{test_case} {1}')  