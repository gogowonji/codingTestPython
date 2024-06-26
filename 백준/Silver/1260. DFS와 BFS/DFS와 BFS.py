from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def main():
    N, M, V = map(int, input().split())
    #print(N,M,V)

    # 인덱스 0 제외
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        src, dest = map(int, input().split())
        graph[src].append(dest)
        graph[dest].append(src)

    visited = [False] * (N + 1)
    dfs(graph, V, visited)
    print()
    
    visited = [False] * (N + 1)
    bfs(graph, V, visited)

if __name__ == "__main__":
    main()
