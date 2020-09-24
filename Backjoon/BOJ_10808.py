# A-Z까지 인덱싱해서 비교할 문자열과 빈도수 list 선언
alphabet='abcdefghijklmnopqrstuvwxyz'
result=[0 for _ in range (26)]
S=input()

for i in S:
    # loop 내에서 인덱싱하여 조건에 맞는 알파벳을 찾으면
    # 값을 +1 해준다
    idx = alphabet.find(i)
    result[idx] += 1
# 처음에 int값으로 init했으니 아래와같이 출력하기 위해 str으로 값을 치환함
result=[str(k) for k in result]
print(' '.join(result))
