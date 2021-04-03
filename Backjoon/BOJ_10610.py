# 미르코는 30의 배수를 좋아한다
# 그러므로 길거리에서 주은 숫자들을 조합해 30의 배수로 만들고자 한다.
N = input()
N = sorted(N, reverse=True)

result = int(''.join(N))
if result % 30 == 0:
    print(result)
else:
    print(-1)