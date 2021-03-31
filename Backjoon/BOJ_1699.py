# 제곱수의 합
N = int(input())
DP = [0 for i in range ( N+1 )]
square = [i * i for i in range(1, 317)]

for i in range(1, N+1):
    s = []
    for j in square:
        if j > i:
            break
        s.append(DP[i-j])
    DP[i] = min(s) + 1
print(DP[N])