# 분산처리
import sys
N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    A,B = map(int, sys.stdin.readline().rstrip().split())

    # 뭘 곱해도 무조건 결과가 똑같은 밑수는 예외처리
    if A == 1:
        print(1)
        continue
    elif A == 5:
        print(5)
        continue
    elif A == 6:
        print(6)
        continue
    
    # String으로 간단히 해결될 문제가 아니다.. 
    # 시간초과난다.
    # 지수와 규칙을 갖고 구하는 방향이 더 빠르다.
    
    # 지수로 규칙을 뽑음
    result = []
    temp = 1

    for _ in range(B):
        temp *= A
        temp %= 10
        if temp in result:
            break
        result.append(temp)
    
    # 최종결과
    final_result = result[B % len(result) - 1]
    if final_result == 0:
        print(10)
    else: print(final_result)
        