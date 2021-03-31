# 자체로 요일 계산을 해주는 calendar 모듈이 있다.
import calendar

# 일~토로 배열을 잡았네..
# 월~일로 잡았다 ㅡㅡ
dayofweek=["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
x,y=map(int, input().split())
#연, 월, 일을 받고 요일을 0~6 사이로 리턴한다.
day = calendar.weekday(2007,x,y)


print(dayofweek[day])

'''
import calendar
day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
a,b=map(int,input().split())

k = calendar.weekday(2007,a,b)

print(day[k])
'''