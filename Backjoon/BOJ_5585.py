# 그리디 알고리즘 - 거스름돈 예제
# ** 가장 큰 화폐 순서대로 돈을 거슬러준다.
# 이 문제는 1000엔을 내고, 물건 가격을 입력하여 잔돈을 계산하는 방식이다

std=1000
price=int(input())

charge=std-price

count=0
coin_list = [500, 100, 50, 10, 5, 1]

for coin in coin_list:
    count += charge // coin  # list 내 동전으로 나누기 할때마다 세기
    charge %= coin  # 연산은 남은 거스름돈이 0이될때까지 계속된다

print(count)

# 380
# 300 *