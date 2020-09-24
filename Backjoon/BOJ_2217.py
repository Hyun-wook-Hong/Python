#가장 작은 무게를 들 수 있는 로프가 들 수 있는 질량 * 병렬 연결 로프 갯수 = 최종 무게

N=int(input())
ropes=[]

# N개만큼 로프 개수 입력받기
for _ in range(N):
    ropes.append(int(input()))

# 가장 무거운 무게를 들 수 있는 로프부터 내림차순 정렬한 후
# 각 인덱스마다 무게*순서를 곱하여
# 가장 높은 값을 뽑으면 된다
result=0
ropes.sort(reverse=True)

for i in range(N):
    ropes[i] = ropes[i] * (i+1)

print(max(ropes))