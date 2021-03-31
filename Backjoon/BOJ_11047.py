# 동전 제로 - 최소 동전 개수
# N: 동전 개수, K: 계산해야될 돈

N, K = map(int, input().split())
coins=[]
count=0

for _ in range(N):
    coin = int(input())
    coins.append(coin)

# 큰 동전부터 계산하기 위해 뒤집기
coins.reverse()

for i in range(0, N):
    #print(coins[i])
    count += K // coins[i]
    K %= coins[i]

print(count)
