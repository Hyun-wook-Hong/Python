import sys
# 홀수
# 7개의 자연수 중 홀수인 것들의 합
# 이 7개의 홀수들 중에서 최솟값
number = []
odds = []

for _ in range(7):
    N = int(sys.stdin.readline().rstrip())
    number.append(int(N))

sum = 0
for i in range(len(number)):
    if number[i] % 2 != 0:
        sum += int(number[i])
        odds.append(int(number[i]))

# 구한 홀수값에 따라 출력
if len(odds) != 0 and sum != 0:
    print(sum)
    print(min(odds))
# 홀수 아예 없으면 -1
else: print(-1)