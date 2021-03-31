# 오븐 시계
import sys
HH,MM = map(int, sys.stdin.readline().rstrip().split())
time = int(sys.stdin.readline().rstrip())

HH += time // 60
MM += time % 60

# 분단위가 60 넘으면 +1HR, MN = MN-60
if MM >= 60:
    HH += 1
    MM = MM - 60
# 시단위가 24 넘으면
if HH >= 24:
    HH = HH - 24

print(HH, MM)