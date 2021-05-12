# 프린터 큐
# 우선순위 큐 사용
# 이건 결국 로직 자체를 직접 구현해야 할 것 같다.

if __name__ == '__main__':
    # TestCase만큼 실행
    for _ in range(int(input())):
        # N: 큐의 크기
        # M: 나중에 순서 확인할 큐 속 요소의 index
        N,M = map(int, input().split())
        q = list(map(int, input().split()))
        indexes = list(range(len(q)))

        indexes[M] = 'value of M index'

        # 순서
        order = 0
        # loop
        while True:
            # 조건 1. 현재 가장 맨 앞에 있는 요소의 우선순위(값 자체)보다 큰 값이 있는지?
            if q[0] == max(q):
                order += 1

                # 조건 2. 현재 맨 앞의 indexes 값이 'value of M'이냐? (우리가 찾던것이면 loop 탈출)
                if indexes[0] == 'value of M index':
                    print(order)
                    break
                # 최댓값도, value of M도 아니면 그냥 없앤다
                else:
                    q.pop(0)
                    indexes.pop(0)
            # 조건 1과 일치하지 않으면 맨 뒤로 보낸다
            else:
                q.append(q.pop(0))
                indexes.append(indexes.pop(0))
