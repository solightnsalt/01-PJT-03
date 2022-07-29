import sys

sys.stdin = open("_문자열의거울상.txt")


mirror = {
        'b' : 'd', 
        'd' : 'b',
        'p' : 'q',
        'q' : 'p'
    }

T = int(input())
for test_case in range(1, T + 1):
    word = input()
    r_word = word[::-1]
    
    result = ''
    #print(r_word)    
    for alph in r_word:
        result += mirror[alph] 
        
    print(f'#{test_case} {result}')
        
    # 와 result 정의 위치 주의하기ㅠㅠ  #2 pqqbdbddqqqpppp