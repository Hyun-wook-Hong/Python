# 방 번호
import sys

setCnt=0

S = sys.stdin.readline().rstrip()
arr = [False*i for i in range(0,10)]

for i in range(0,10):
    for x in S:
        if str(i) == x:
            arr[int(x)] += 1

# 9는 6으로, 6은 9로 뒤집어 쓸 수 있음
# 그런고로 전부 6으로 뒤집어서 계산한다
arr[6] = arr[6] + arr[9]
arr[9] = 0

#           짝수인 경우 2를 나눈 값이 9로 뒤집어서 나온 최솟값
if arr[6] % 2 == 0:
    arr[6] = arr[6] // 2
# 홀수인 경우 2를 나누고 1을 더한 값이 9를 뒤집어서 나온 최솟값
else:
    arr[6] = arr[6] // 2 + 1

print(max(arr)) 