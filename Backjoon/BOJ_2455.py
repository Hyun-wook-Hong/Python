# 지능형 기차
now=0
total=[]

for _ in range(4):
    out_cnt,in_cnt=map(int, input().split())
    now = now + (in_cnt-out_cnt)
    total.append((now))

print(max(total))