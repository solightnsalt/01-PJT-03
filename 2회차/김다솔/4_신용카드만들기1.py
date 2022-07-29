from ctypes.wintypes import HLOCAL
import sys

sys.stdin = open("_신용카드만들기1.txt")
T = int(input())
for test_case in range(1, T + 1):
    card_n = list(map(int, input().split()))
    # print(card_n)
    hol = card_n[0:15:2]
    jjak = card_n[1:15:2]
    #print(hol, jjak)
    a = sum(hol) * 2 + sum(jjak)
    #print(a) 
    for i in range(10):
        n = a + i
        if n % 10 == 0:
            print(f'#{test_case} {i}')
            

    