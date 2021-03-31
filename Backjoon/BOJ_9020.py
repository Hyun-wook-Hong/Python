#Goldbach's strong conjecture
'''
** 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다
1. 두 수는 무조건 소수여야 한다
2. 골드바흐 파티션이 여러개일 수도 있는데,
   이때는 두수간의 차가 가장 작은 파티션을 정답으로 고른다

    해결방법..
   1) 2~N 사이의 소수를 먼저 구한다
'''
def get_prime(num):
    a = [False, False] + [True] * (num-1)

    primes=[]

    for i in range (2, (num+1)):
        if a[i]:
            primes.append(i)
            for j in range(2*i, num+1, i):
                a[j] = False
    return primes

if __name__ == "__main__":
    test_case = int(input())
    for _ in range(test_case):
        even = int(input())
        # 입력받은 짝수 이하의 숫자들 중 소수인 것을 구해 배열에 담는다
        prime_set = get_prime(even)
        even_half = even // 2 # 테스트케이스마다 돌며 입력받은 짝수를 2로 나눈다

        for i in range(even_half, 1, -1): #차이가 적은 두 수를 꺼내기 위해 큰수부터 꺼낸다 (두번째조건)
            # (입력받은 짝수)-i, i가 위에서 구한 소수 집합에 들어가있는가?
            if(even-i in prime_set) and (i in prime_set):
                print(i, even-i)
                break
