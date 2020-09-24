xPoint = []
yPoint = []

# 먼저 3개의 좌표를 받는다
for i in range(3):
    x, y = map(int, input().split())
    xPoint.append(x)
    yPoint.append(y)

print(max(xPoint), min(yPoint))