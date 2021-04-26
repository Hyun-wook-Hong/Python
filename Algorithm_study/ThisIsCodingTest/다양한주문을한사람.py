import sys
'''
4/26 스터디 문제.
가장 다양한 주문을 한 손님을 구해라.
입력은 다음과 같이 구성된다.

첫번째줄: 주문 테이블 갯수 N개
두번째줄~N+1번째 줄: 이름 (음식1) (음식2)
→ 음식 인자 값은 아무거나 와도 상관없다
'''
def get_maxlen(arr):
    max_len=0
    for i in range( len(arr) ):
        if max_len <= len(arr[i])-1:
            max_len = len(arr[i])-1
    return max_len

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())

    arr = [sys.stdin.readline().rstrip() for _ in range(N)]
    name = []

    # 이름 먼저 추출
    for i in range( len(arr) ):
        str_v = arr[i].split()
        
        if str_v[0] not in name:
            name.append( str_v[0] )

    result = []

    for i in range( len(name) ):
        tray = []
        #print([name[i]])
        tray.append( name[i] )
        for j in range( len(arr) ):
                str_a = arr[j].split()
                if name[i] == str_a[0]:
                        for k in range( 1, len(str_a) ):
                                if str_a[k] not in tray:
                                    tray.append(str_a[k])
        
        #print(tray)
        result.append(tray)

    answer = []
    max_value = get_maxlen(result)

    for i in range( len(result) ):
        # 같은 max값이 있을수도 있음, 그런 경우엔 같이 배열로 정답 출력 
        if max_value <= len(result[i]) - 1:
                answer.append(result[i][0])
    print(answer)
              
