import sys

# 재귀제한 높이 설정 (DFS로 구현했을때 선언 안해놓으면 런타임 에러남)
sys.setrecursionlimit(50000)

# 유기농 배추 -> 연결요소 문제
# DFS로 특정한 노드를 방문한 뒤에 연결한 모든 노드들도 방문
def DFS(x,y):
    if x>=0 and x<n and y>=0 and y<m:
      if graph[x][y]==1:
        # 0이 아니라 2로 바꿔야 recursive error 안나는듯
        graph[x][y]=2
        DFS(x,y+1)
        DFS(x,y-1)
        DFS(x-1,y)
        DFS(x+1,y)
        return True
    return False


if __name__ == '__main__':
    # 테스트케이스 갯수만큼 실행
    TestCase = int(input())
    for _ in range(TestCase):

        # (N x M) n, m, 배추심은 갯수
        m,n,cabbages = map(int, input().split())

        # 밭 지도 키보드 입력받기 + 방문여부
        graph = [([0] * m) for i in range(n)]

        # 배추 갯수만큼 어느 포인트에 배추가 심어져있는지 입력받고 그래프 구성
        for _ in range(cabbages):
            x,y = map(int, input().split())
            graph[y][x] = 1

        #print(graph)

        worms = 0
        # 구성된 그래프의 모든 요소에 대해 DFS 실행
        for i in range(n):
            for j in range(m):
                # 그래프를 싹 뒤져서 현재 위치가 1인경우 DFS를 수행해 count해줌 (DFS 수행한 갯수 자체를 count함)
                if DFS(i, j) == True:
                    worms += 1
        print(worms)