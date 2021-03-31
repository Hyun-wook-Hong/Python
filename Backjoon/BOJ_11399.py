N=int(input())
remain_time=list(map(int, input().split()))

min_time=[]
mini=0

remain_time.sort()

for i in range(len(remain_time)):
    mini += remain_time[i]
    min_time.append(mini)

print(sum(min_time))