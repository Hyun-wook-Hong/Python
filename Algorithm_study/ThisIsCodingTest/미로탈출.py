# N x M의 공간에서
# 현재 (0,0)의 위치에 있으며
# 1로 표시된 곳은 빈 공간, 0으로 표시된 공간은 괴물이 있는 공간임.

# (0,0)에서 (N-1, M-1)까지 가는데 걸리는 최소 횟수는?
# BFS로 구현

from collections import deque

def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if area[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if area[nx][ny] == 1:
                area[nx][ny] = area[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return area[n - 1][m - 1]


if __name__ == '__main__':
    # N, M을 공백을 기준으로 구분하여 입력 받기
    n, m = map(int, input().split())
    # 2차원 리스트의 맵 정보 입력 받기
    area = []
    for i in range(n):
        area.append(list(map(int, input())))

    # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    print(bfs(0,0))