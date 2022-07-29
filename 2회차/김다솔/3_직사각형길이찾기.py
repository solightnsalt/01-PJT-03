import sys

sys.stdin = open("_직사각형길이찾기.txt")

T = int(input())
for test_case in range(1, T + 1):
    a, b, c = map(int, input().split())
    #print(a, c, b)
    if a == b: 
        d = a * c // b
    else:
        d = a * b // c
    print(f'#{test_case} {d}')    
    
