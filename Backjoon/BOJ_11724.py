# 연결 요소의 개수 DFS
# 첫째줄: 노드갯수(N), 간선갯수(M)
# 들째줄 ~ M번째줄: 간선의 양 끝점 (u,v)

# 시간초과나서 sys.stdin.readline() 추가함
import sys
from collections import deque
def BFS():
    count = 0
    #visited[start] = 1
    queue = deque()

    #1번부터 N번까지 노드를 전부 탐색한다.
    for i in range(1, N+1):
        # 방문하지 않은 번호의 노드만
        if visited[i] == 0:
            visited[i] = 1
            queue.append(i)
            count += 1

            while queue:
                v = queue.popleft()
                # 큐에서 뽑은 그래프번째 노드 탐색
                for j in graph[v]:
                    # 만약 방문하지 않은 노드라면 방문처리 하고 해당 노드를 큐에 삽입
                    if visited[j] == 0:
                        visited[j] = 1
                        queue.append(j)
    return count




if __name__ == '__main__':
    N,M = map(int, sys.stdin.readline().rstrip().split())
    graph = [[] for _ in range(N+1)]

    visited = [0] * (N + 1)

    count = 0

    # 인접행렬 생성
    for _ in range(M):
        u,v = list(map(int, sys.stdin.readline().rstrip().split()))
        graph[u].append(v)
        graph[v].append(u)

    # 1번부터 차례로 시작
    count = BFS()
    print(count)


