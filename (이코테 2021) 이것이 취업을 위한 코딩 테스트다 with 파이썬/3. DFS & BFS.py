# 3강. DFS & BFS

# 스택 5-1.py
stack = []
stack.append(5)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력

# 큐 5-2.py
from collections import deque

queue = deque()

queue.append(5)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse()
print(queue) # 나중에 들어온 원소부터 출력

# 재귀 함수 5-3.py
def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()
  
recursive_function()

# 재귀 함수 종료 5-4.py
def recursive_function():
    if i == 100:
      return
    print(i, '번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀 함수를 종료합니다.')
  
recursive_function(1)

# 2가지 방식으로 구현한 팩토리얼 5-5.py
# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
      result *= i
    return result
  
# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1:
      return 1
    return n * factorial_recursive(n-1)

print('반복적으로 구현:', factorial_iteractive(5))
print('재귀적으로 구현:', factorial_iteractive(5))

# 인접 행렬 5-6.py -> 모든 관계를 저장하기 때문에 노드 개수가 많을수록 메모리 낭비 가능성 증가
INF = 999999999

graph = [
  [0, 7, 5],
  [7, 0, INF],
  [5, INF, 0]
]

print(graph)

# 인접 리스트 5-7.py -> 연결된 정보만을 저장하기 때문에 메모리 효율적으로 사용
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

graph[1].append((0, 7))

graph[2].append((0, 5))

print(graph)

-------------------------------------------------------------------------
# DFS(깊이 우선 탐색) 5-8.py
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

# BFS(너비 우선 탐색) 5-9.py
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

# 예제. 음료수 얼려 먹기
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] == 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1
            
print(result)

# 예제. 미로 탈출
from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append(x,y)
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                
    return graph[n-1][m-1]

print(bfs(0,0))
