# 연결요소찾기 문제, DFS로 풀이 가능하다.

# DFS로 특정한 노드를 방문한 뒤에 연결한 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나면 즉각 종료시킨다.
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드를 방문처리 한다.
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출한다.
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# N, M을 공백 구분하여 입력받기
# N x M
if __name__ == '__main__':
    n, m = map(int, input().split())

    # 2차원 리스트의 맵 정보 입력받기
    graph = []
    for i in range(n):
        graph.append(list(map(int, input())))

    # 모든 노드(위치)에 대하여 음료수를 채운다
    result = 0
    for i in range(n):
        for j in range(m):
            # 현재 위치에서 DFS를 수행한다.
            if dfs(i, j) == True:
                result += 1
    print(result)