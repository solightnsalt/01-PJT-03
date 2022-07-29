import sys

sys.stdin = open("_소득불균형.txt")

T = int(input())
for test_case in range(1, T + 1):
    ppl = int(input())
    income = list(map(int, input().split()))
    avg_inc = sum(income) // ppl
    under_avg = []
    #print(aver_inc)
    for i in income:
       # print(i)
        if i <= avg_inc:
            under_avg.append(i)
            
    print(f'#{test_case} {len(under_avg)}')
            