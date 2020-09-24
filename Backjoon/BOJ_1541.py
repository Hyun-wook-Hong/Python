# 잃어버린 괄호
# - 나올때까지 더하고, 그렇지않으면 뺀다. 그래야 최솟값이 나옴
form = input().split('-')
result=0

for x in form[0].split('+'):
    result += int(x)

for x in form[1:]:
    for y in x.split('+'):
        result -= int(y)

print(result)
