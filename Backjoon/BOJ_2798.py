N, M = map(int, input().split())
deck = list(map(int, input().split(' ')))
result=0
# 총 3개 카드에 대한 순차탐색(브루트포스) 실시
for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
                # 세 수의 합이 M 이하이고, (M - 세수의합) < M - 현재결과 인경우
            if (deck[i]+deck[j]+deck[k]) <= M and M - (deck[i]+deck[j]+deck[k]) < M - result:
                    result = deck[i]+deck[j]+deck[k]

print(result)

