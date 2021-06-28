# BOJ 12865번, 평범한 배낭

# 물건을 각각 쪼개어 넣을 수는 없는 유형의 배낭 문제(0-1)
# N: 물건 갯수, W: 물건 무게, V: 물건 가치
# K: 배낭에 넣을 수 있는 최대 무게

# knapsack[i][j] = max( V+knapsack[i-1][j-W], knapsack[i-1][j] )
N, K = map(int, input().split())
stuff = [[0,0]]
knapsack = [[0 for _ in range(K+1)] for _ in range(N+1)]

for _ in range(N):
    stuff.append(list(map(int, input().split())))

# 데이터를 뽑아서 위에 구한 수식을 적용
for i in range(1, N+1):
    for j in range(1, K+1):
        W = stuff[i][0]
        V = stuff[i][1]

        # j(현재무게)가 Weight보다 작으면 위(이전)의 값을 그대로 가져온다.
        if j < W:
            knapsack[i][j] = knapsack[i-1][j]
        # knapsack[i][j] = max( 가치+knapsack[이전물건][현재가방무게-현재물건무게], knapsack[이전물건][현재가방무게] )
        else:
            knapsack[i][j] = max( V+knapsack[i-1][j-W], knapsack[i-1][j] )
print(knapsack[N][K])