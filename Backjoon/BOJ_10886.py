# Cute or not cute
# N은 홀수이므로 같은 수가 나올수는 없다.
N = int(input())
yes = 0
no = 0

for _ in range(N):
    yn = int(input())

    if yn == 1:
        yes += 1
    elif yn == 0:
        no += 1

if yes > no:
    print('Junhee is cute!')
else: print('Junhee is not cute!')