# 터렛이 돌며 그려지는 원의 접점을 구하면 된다
# -1: 두 원이 좌표, 거리 모두 똑같다면 올 수 있는 경우의 수가 무한대
#  0: 두 원이 아예 서로 겹치지 않는경우
#  1: 두 원이 외접/내접하는 경우
#  2: 두 원이 좌표가 같진 않지만 교집합 형태로 겹치는경우
def missile_turret():
    x1,y1,r1,x2,y2,r2 = map(int, input().split())

    d = ((x2 - x1)**2 + (y2 - y1)**2) **0.5
    rs = r1 + r2
    rm = abs(r1 - r2)

    if d == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if d==rs or d==rm:
            print(1)
        elif d<rs and d>rm:
            print(2)
        else:
            print(0)

if __name__ == "__main__":
    test_case=int(input())

    for i in range(test_case):
        missile_turret()