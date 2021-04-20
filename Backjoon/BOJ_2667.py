# 단지번호 붙이기
# 연결요소는 몇개인지, *각 연결요소들은 몇개의 원소를 갖고 있는지?*
# DFS로 구현

def dfs(x, y):
    global cnt
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if apart[x][y] == 1:
        # 해당 노드를 방문처리 한다.
        apart[x][y] = 0
        cnt += 1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출한다.
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

if __name__ == '__main__':
    n = int(input())

    apart = [list(map(int, input())) for _ in range(n)]

    # 단지 수
    result = 0
    # 단지별 아파트 수
    c_complex = []
    cnt = 0

    for i in range(n):
        for j in range(n):
            if dfs(i, j) == True:
                result += 1
                c_complex.append(cnt)
                # 숫자 센 다음엔 0으로 초기화
                cnt = 0
                
    print(result)
    # 단지내 집의 수는 오름차순 하여 정렬 후 출력
    c_complex.sort()
    for x in c_complex:
        print(x)           
