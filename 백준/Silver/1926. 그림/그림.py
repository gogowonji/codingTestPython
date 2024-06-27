from collections import deque

directions = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우 위치벡터

def bfs(graph, i1, i2, n, m, visited):
    # 1이 몇개 있는지 세기 - 넓이 구하려고
    oneCount = 0
    # 좌표값을 큐로 초기화
    queue = deque([(i1,i2)])
    visited[i1][i2] = True

    while queue:
        # 좌표값 pop()
        x, y = queue.popleft()
        # 넓이 1 증가
        oneCount += 1
        
        # 상하 좌우 연결된 1이 있는지 체크할거야
        for dx,dy in directions:
            mx, my = x+dx,y+dy
            # 방문하지 않았고, 1인지 확인
            # 도화지 범위를 넘어가는지 함께 체크
            if 0 <= mx < n and 0 <= my < m and not visited[mx][my] and graph[mx][my] == 1:
                queue.append((mx,my))
                visited[mx][my] = True

    return oneCount

def main():

    n, m = map(int, input().split())
    
    # 색칠 여부 n번 받아오기
    paper = [list((map(int, input().split()))) for _ in range(n)] 
    
    # 2차원 배열로 m(가로) * n(세로) 만들기-> m 빼먹엇다..
    visited = [[False] * m for _ in range(n)] 
    # 몇개의 그림이 있는지 세기
    count = 0
    # 가장 큰 넓이 값 구하기 위해서 변수 선언
    maxArea = 0

    # 탐색하다가 탐색되지 않은 1이 나오면 bfs 실행 -> 연결된 1 확인 (count += 1)
    for i in range(n):
        for j in range(m):
            if paper[i][j] == 1 and not visited[i][j]:
                # 넓이 리턴 받기 - bfs에서 몇 개의 1이 나왔는지 리턴 해주기
                oc = bfs(paper, i, j, n, m, visited)
                
                # if(oc == 1): # 1이 하나면.. count 하면 안된다고 생각했음
                #     continue
                # else:
                
                # 가장 큰 넓이의 값 구하기
                maxArea = max(maxArea,oc)
                # 탐색하고 오면, 그림 1개 추가
                count += 1

    print(count)
    print(maxArea)


if __name__ == "__main__":
    main()

