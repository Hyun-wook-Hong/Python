# 1부터 입력받은 N까지 생성자가 될 수 있는 수는 모조리 대입한다

N = int(input())
result=0

for i in range(1, N+1):
    # 세 수는 list로 한자릿수씩 짜갠다
    divided_sum = list(map(int, str(i)))
    # 짜갠 숫자 합 + i가 N과 같으면 그 숫자는 생성자이다
    result = i + sum(divided_sum)

    if result == N:
        print(i)
        break
    if i == N:
        print(0)