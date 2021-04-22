# 바이러스
# 한 PC가 웜에 걸리면 그 PC와 네트워크로 연결된 모든 PC가 웜에 걸린다.
# 1번 컴퓨터가 웜에 걸렸을때, 몇대의 컴퓨터가 웜에 걸리는가? (자기자신 제외)
from collections import deque

# BFS 메서드 정의 (1번 노드에서 시작)
def BFS(start):
    queue = deque()
    queue.append(start)
    # 큐가 빌 때 까지
    while queue:
        start = queue.popleft()
        # 방문하지 않은 곳이라면 그곳으로 이동
        if visited[start] == 0:
            visited[start] = 1
            for i in graph[start]:
                queue.append(i)

N = int(input())
pair = int(input())

count = 0

graph = [ [] for _ in range(N+1) ]
# 앞의 0번 노드는 일부러 비웠다.
visited = [0] * (N + 1)

for _ in range(pair):
    X,Y = list(map(int, input().split()))
    graph[X].append(Y)
    graph[Y].append(X)

BFS(1)
# 1노드 자기 자신을 포함한 방문 여부이므로 1을 빼준다.
print(sum(visited) - 1)