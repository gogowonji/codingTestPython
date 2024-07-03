# 2644 촌수 계산
# n : 전체 사람의 수 (그래프 행수)
# p1, p2 : 촌수를 계산해야 하는 서로 다른 두사람의 번호
# m : 부모 자식간의 관계의 개수
# x,y : 부모 자식간의 관계를 나타내는 두 번호 (m번 만큼)

from collections import deque

def bfs(graph, start, target, visited):
    queue = deque([(start,0)]) # 쌍은 괄호, 리스트, 함수
    visited[start] = True
    
    # dfs로 풀라 그러다가..
    # for _ in graph[visited]:
    # if not visited[i]:
    #     if i == p2:
    #         return
    #     else:
    #         # 어떻게 처리하지..
    
    while queue:
        current, count = queue.popleft()
        if current == target:
            return count
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, count+1))
    return -1




def main():
    n = int(input())
    # n+1 만큼 리스트 만들어 주기 (0이 없음)
    graph = [[] for _ in range(n+1)]

    p1, p2 = map(int, input().split())
    m = int(input())

    # 해당 되는 부모에 값 넣어주기~
    for _ in range(m):
        x,y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    # 방문했나 안했나
    visited = [False]*(n+1)

    result = bfs(graph,p1,p2,visited)
    print(result)
    
    # 원래는 visited 값으로 촌수를 세려고 했었음
    # result = 0
    # for b in visited:
    #     print(b)
    #     if b:
    #         result += 1

    # print(result)





if __name__ == "__main__":
    main()

