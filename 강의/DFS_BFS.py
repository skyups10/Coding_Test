# DFS 5-8.py
def dfs(graph, v, visited):
  visitied[v] = True
  print(v, end=' ')
  
  for i in graph[v]:
    if not visitied[i]:
      dfs(graph, i, visited)

graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited = [False] * 9
dfs(graph, 1, visited)

# BFS 5-9.py
from collections import deque

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    print(v, end=' ')
    for i in graph[v]:
      if not visitied[i]:
        queue.append(i)
        visited[i] = True

graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7],
]

visited = [False] * 9
bfs(graph, 1, visited)
