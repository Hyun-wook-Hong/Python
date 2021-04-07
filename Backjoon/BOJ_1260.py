# DFS와 BFS
# DFS는 깊이 우선 탐색, BFS는 너비 우선 탐색
# 보통 둘다 2차원 행렬로 구현,
# DFS는 재귀, BFS는 queue로 구현함


N,M,V = map(int, input().split())

matrix = [[0]*(N+1) for i in range(N+1)]

for i in range(M):
    a,b=map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1
visit_list = [0]*(N+1)

def DFS(V):
    visit_list[V] = 1 #이미 방문한 점은 1으로 표시
    print(V, end=' ')
    for i in range(1, N+1):
        # 방문하지 않았고, 그 위치가 입력받은 위치라면 그리로 이동한다.
        if(visit_list[i] == 0 and matrix[V][i] == 1):
            DFS(i)

def BFS(V):
    queue = [V] #들러야할 정점을 큐에 미리 저장함
    visit_list[V] = 0 #방문한 점은 0으로 표시 - DFS 실행할때 visit_list가 1로 init되었으므로
    while queue:
        V = queue.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if visit_list[i] == 1 and matrix[V][i] == 1:
                queue.append(i)
                visit_list[i] = 0

DFS(V)
print()
BFS(V)