# 1. 직사각형의 경계선까지의 거리에서 대각선 길이는 최소가 아니다
# 2. 입력받은 (x,y)에서 (w,h), (0,0)까지의 거리를 고려해야 한다
x, y, w, h = list(map(int, input().split()))
print(min([x, y, w-x, h-y]))