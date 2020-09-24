# 유클리드 호제법: A와 B의 최대공약수, 최소공배수를 쉽게 구할 수 있음
def gcd(A, B):
    if (B == 0):
        return A

    #
    return gcd(B, A%B)

if __name__ == '__main__':
    A,B=map(int, input().split(' '))

    G = gcd(A, B)
    print('최대공약수: ', int(G))
    # 참고로 최소공배수 = 두수의곱 / 최대공약수 임
    print('최소공배수: ', int((A*B)//G))