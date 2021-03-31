# 셀프넘버
arr = [i for i in range(1, 10001)]
del_target = []

for element in arr:
    for n in str(element):
        element += int(n) # 생성자(self number)가 있는 숫자
    if element <= 10000:  # 1 <= N <= 10000
        del_target.append(element)

# 위에서 찾은 생성자가 있는 숫자 대상을 arr 배열에서 없앰
for del_num in set(del_target):
    arr.remove(del_num) 

# 없애고 난 뒤 출력한 값
for self_num in arr:
    print(self_num)