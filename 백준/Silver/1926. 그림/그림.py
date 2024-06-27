from collections import deque

directions = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우

def bfs(graph, i1, i2, n, m, visited):
    oneCount = 0
    queue = deque([(i1,i2)])
    visited[i1][i2] = True

    while queue:
        x, y = queue.popleft()
        oneCount += 1
        # 상하 좌우 연결된 1이 있는지 체크
        for dx,dy in directions:
            mx, my = x+dx,y+dy
            # 범위를 넘어가는지...
            if 0 <= mx < n and 0 <= my < m and not visited[mx][my] and graph[mx][my] == 1:
                queue.append((mx,my))
                visited[mx][my] = True

    return oneCount

def main():

    n, m = map(int, input().split())

    paper = [list((map(int, input().split()))) for _ in range(n)]

    visited = [[False] * m for _ in range(n)] # 2차원 배열로 m......빼먹엇다..
    count = 0
    maxArea = 0

    # 탐색하다가 탐색되지 않은 1이 나오면 bfs 실행 -> 연결된 1 확인 (count += 1)
    for i in range(n):
        for j in range(m):
            if paper[i][j] == 1 and not visited[i][j]:
                # bfs에서 몇 개의 1이 나왔는지 리턴 해주면 좋겠다
                oc = bfs(paper, i, j, n, m, visited)
                # if(oc == 1): # 1이 하나면.. count 하면 안돼
                #     continue
                # else:
                maxArea = max(maxArea,oc)
                count += 1

    print(count)
    print(maxArea)


if __name__ == "__main__":
    main()

