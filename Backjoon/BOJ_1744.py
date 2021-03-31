def divide_list(l, n):
    # 리스트 l의 길이가 n이면 반복
    for i in range(0, len(l), n):
        yield l[i:i+n]

def single_list(L):
    # 리스트의 길이가 1이면 int값 반환
    temp = 0
    for i in range(len(L)):
        temp =L[i]
    return temp
if __name__ == '__main__':
    # 수 묶기
    N=int(input())
    num=[]
    tied_positive=[]
    tied_negative=[]

    result=0

    for _ in range(N):
        element=int(input())
        num.append(element)

    num.sort()

    # Attemp 5. 0은 어차피 있는지만 보고, 더해도 연산에 별 지장이 없기 때문에..
    #           만일 묶은 수 중 하나 남은 음수가 있다면 그 수와 묶어서 0이 되도록 만든다
    itHasZero=False

    # 0이나 1은 더하는 편이 낫다. (특히 0은 곱해서 0이 되는것 보단 더하면 아무 변화도 없기에)

    # Attempt 2. 양/음 분리 및 하나만 묶인 숫자는 그냥 더하기
    # 1. 양수는 양수끼리, 음수는 음수끼리 묶는다.
    # 2. 묶이지 못하고 낱개로 남은 양/음수는 더한다.
    for i in range(len(num)):

        if num[i] == 0:
            itHasZero=True

        elif num[i] == 1:
            result += num[i]

        elif num[i] > 1:
            tied_positive.append(num[i])

        elif num[i] <  0:
            tied_negative.append(num[i])


    # Attempt 3. 양수 리스트, 음수 리스트를 정렬하는 부분을 간과했다.
    # -998, -997, -996, ..., -1
    tied_negative.sort()
    # 1, 2, 3, 4, 5, ...
    tied_positive.sort(reverse=True)

    ties=list(divide_list(tied_positive, 2)) + list(divide_list(tied_negative, 2))

    # 묶은 숫자들 중에 하나만 묶인 숫자가 있는가?

    #result2=0
    # 묶은 숫자 더하기 (묶은숫자1*묶은숫자2) + (묶은숫자3*묶은숫자4) + ....
    for i in range(len(ties)):
        # 하나만 list에 묶여 남은 대상이 있으면 그 수는 그냥 더한다
        if len(ties[i]) == 1:
            temp = single_list(ties[i])
            # Attempt 4. 반례 추가, 하나 남은 음수는 0과 같이 곱하면 더 큰 수를 만들 수 있다. (입력받은 수열에 0이 있다면)
            if temp < 0 and itHasZero == True:
                temp = temp * 0
                result = result + temp
            else:
                result = result + temp
        # 2개씩 묶인 대상이라면 공식에따라 계산한다.
        else:
            result = result + (ties[i][0] * ties[i][1])
    #print(result2)
    print(result)

