# 단순히 재귀나 무한 loop를 사용하면 이 문제를 해결할 수 없다.
# list에 append해서 한글자씩 검사하다가 폭발 문자열이 있으면 삭제하는 방식으로
# 구현해야한다.

# ???: 예술은 폭발이다!
def art(S, bomb):
    last_char = bomb[-1]
    arr = []
    bomb_length = len(bomb)

    # 문자열 하나씩 검사하면서
    for char in S:
        arr.append(char)
        if char == last_char and ''.join(arr[-bomb_length:]) == bomb:
            del arr[-bomb_length:]

    result = ''.join(arr)

    if result == '':
        result = "FRULA"
        return result
    else:
        return result

if __name__ == '__main__':
    S = input()
    bomb = input()

    answer = art(S, bomb)

    print(answer)
