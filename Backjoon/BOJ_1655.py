# BOJ 1655번, 가운데를 말해요
# min 힙(왼쪽배열), max 힙(오른쪽배열)을 생성해 활용한다.
# 중앙값은 max 힙의 첫번째 인덱스 값이 된다.

import heapq
import sys

left, right = [], []
N = int(sys.stdin.readline().rstrip())
A = []

for _ in range(N):
    number = int(sys.stdin.readline().rstrip())
    if len(left) == len(right):
        # max heap
        heapq.heappush(left, (-number, number))
    else:
        # min heap
        heapq.heappush(right, (number, number))

    # right 값에 원소가 있으면서,
    # left 값이 right 값보다 더 큰경우,
    # left 원소보다 right 원소가 더 커야하는 조건에 위배된다
    if right and left[0][1] > right[0][1]:
        vLeft = heapq.heappop(left)[1]
        vRight = heapq.heappop(right)[1]

        heapq.heappush(right, (vLeft, vLeft))
        heapq.heappush(left, (-vRight, vRight))

    print(left[0][1])
