# 스타 토너먼트
# 두 사람이 무조건 이겨서 다음 라운드에 진출한다고 가정했을때,
# 과연 둘은 몇 라운드에서 붙는지?
import math
import sys
# A, B가 인접 번호인지?
def is_neighbor(A, B):
    N = math.ceil(max(A, B)/2)

    # 인접한 N번째 수들의 합은 3+4(N-1)이다.
    # 1:2 3:4 5:6 7:8 9:10 ...
    #  3   7   11  15  19  ...
    #    4   4    4   4

    if A + B == 3 + (4 * (N - 1)):
        return True
    else:
        return False
if __name__ == '__main__':
    N,KJM,LHS = map(int, sys.stdin.readline().rstrip().split())
    round = 1

    # 토너먼트 로직 작성 시작
    while True:
        if N == 1:
            print(-1)
            break
        else:
            if is_neighbor(KJM, LHS):
                print(round)
                break
            else:
                N = math.ceil(N / 2)
                KJM = math.ceil(KJM / 2)
                LHS = math.ceil(LHS / 2)
                round += 1