import sys

from pyparsing import counted_array

sys.stdin = open("_최빈수구하기.txt")

T = int(input())
for test_case in range(1, T+1): # tc 다음 순서, 점수 번갈아 나오니까 한 번 돌 때 인풋 두개여야,, 
    #print(test_case)
    seq = int(input()) # 얘를 왜 줬지??????? 
    scores = list(map(int, input().split()))
    # print(seq, len(scores))
    #0~100, 101개의 숫자니까 그거 인덱스화해서 바로 카운트 할 빈 리스트 생성
    freq = [0] * 101
    #print(freq)
    for score in scores:
        freq[score] += 1
        #print(freq, freq.index(max(freq)))
        #max_freq = freq.index(max(freq))
        max_freq = max(freq)
        bigger = []
    # cnt.appned()
    for i in range(len(freq)):
        if freq[i] == max_freq:
            bigger.append(i)
    print(f'#{test_case} {max(bigger)}')  
        
    # if freq.count(max(freq)) < 2:
    #     max_freq = freq.index(max(freq))
    #     print(f'#{test_case} {max_freq}')
    # else:
    #     mmax_ = 
    #     print(f'#{test_case} {i)
        
    #print(max_freq)
    # for i in max_freq: 
    #     print(i)
    # if max_freq >= 2:
    #     mmax_ = max(max_freq)
    #     print(f'#{test_case} {mmax_}')
    # else:
    #     print(f'#{test_case} {max_freq}')
    

        
    
    
    
    
    



