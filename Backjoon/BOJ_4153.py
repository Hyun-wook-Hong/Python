import math

while True:
    num = list(map(int, input().split()))

    #가장 큰숫자 제곱 = 나머지숫자1 제곱 + 나머지숫자2 제곱
    great_num = max(num)

    if sum(num) == 0:
        break
    num.remove(great_num)

    if (num[0]**2) + (num[1]**2) == (great_num**2):
     print('right')
    else:
     print('wrong')

     '''
     while True:
        a = list(map(int, input().split()))
        max_num = max(a)
        if sum(a) == 0:
                break
        a.remove(max_num)
        if a[0] ** 2 + a[1] ** 2 == max_num ** 2:
                print('right')
        else:
                print('wrong')
     '''