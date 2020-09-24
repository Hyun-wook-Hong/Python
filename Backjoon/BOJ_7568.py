# 덩치- 자기보다 덩치가 크다: 키, 몸무게 둘다 크다
# 입력받은 사람들에 한해 모두 덩치 크기를 비교해야 한다

N = int(input())

people=[]
result=[]

for _ in range(N):
    w, h = map(int, input().split())
    people.append((w, h))

# 모든 사람에 대해 덩치 무차별 비교를 통해 랭킹(k)을 붙인다
# target: 현재 대상, next_target: 다음 비교대상
for target in people:
    k = 1

    for next_target in people:
        # 비교대상 서로 키, 몸무게 둘다 같지 않다는 가정 하에
        if(target[0]!=next_target[0] & target[0]!=next_target[0]):
            # 키, 몸무게 둘다 크다면 덩치가 큰것
            if(target[0]<next_target[0] and target[1]<next_target[1]):
                k += 1
    result.append(k)

for i in result:
    print(i, end=' ')