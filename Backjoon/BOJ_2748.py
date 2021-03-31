import sys
if __name__ == '__main__':    
    N = int(sys.stdin.readline().rstrip())

    # N번째는 index
    arr = [0 for _ in range(N+1)]
    # 0번째=0, 1번째=1
    arr[1] = 1

    # 피보나치 수 구하기 연산은 idx 두번째부터 시작
    for i in range(2, N+1):
        arr[i] = arr[i-1] + arr[i-2]
    
    print(arr[-1])