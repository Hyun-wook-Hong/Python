# 골드바흐의 추측
# 4보다 큰 모든 짝수는 도 홀수 소수의 합으로 나타낼 수 있다?
import sys

# 구한 소수들 중에서 N = A + B인 적절한 두 수를 뽑는다
# 만약 값이 여러개가 나올 경우 B - A 차 값이 큰 쌍을 뽑는다
def two_elements(N, primes):
    result = []
    for i in range(0, len(primes)):
        if (N - primes[i]) in primes:
            result.append((primes[i], (N-primes[i])))
            break
    return result

# N이하의 모든 소수를 구한다
def get_two_primes(N):
    a = [False, False] + [True]*(N-1)

    primes = []
    for i in range(2, (N+1)):
        if a[i]:
            primes.append(i)
            for j in range(2*i,N+1, i):
                a[j] = False
    
    return two_elements(N, primes)

while True:
    # 6 <= N <= 1000000
    N = int( sys.stdin.readline().rstrip() )
    two_element = []
    if N == 0:
        break
    else:
        two_element = get_two_primes(N)
        # 값 나오면 출력하고, 못 구했으면 반례 출력한다
        if N % 2 == 0 and len(two_element) != 0:
            print("{} = {} + {}".format(N, two_element[0][0], two_element[0][1]))
        else:
            print("Goldbach's conjecture is wrong")
    
