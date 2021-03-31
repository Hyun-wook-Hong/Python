N=int(input())
times=[]
count=0

# 키보드로 입력 받은 다음
for _ in range (N):
    start,end = list(map(int, input().split()))
    times.append([start,end])

# 첫번째 인덱스에서부터 검사하며
# 시간대가 겹치는 원소는 0으로 없애버린다

# times list를 정렬한다, x[1] --> 가장 빨리 끝나는 회의 순
times.sort(key=lambda x: (x[1], x[0]))
# 현재 시작시간이 다음 시작시간보다 작거나 같고
# 현재 종료시간이 다음 시작시간보다 크다면
temp_end=0

# loop 돌며 겹치는 원소 갯수를 센다
for i in range(len(times)):
    if temp_end <= times[i][0]:
        temp_end = times[i][1]
        count += 1

# 정답 = (전체 - 위에서 구한 겹친 갯수)
print(count)



