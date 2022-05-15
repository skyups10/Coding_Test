# 2강. 그리디
# 그리디 = 탐욕법 = 현재 상황에서 지금 당장 좋은 것만 고르는 방법

# 예제 3-1. 거스름돈
n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin

print(count) # 거스름 동전 개수

# 예제 3-2. 큰 수의 법칙
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0
------------------
# 방법 1.
while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1
------------------
# 방법 2.
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)

# 예제 3-3. 숫자 카드 게임 -> 이중 반복문 사용하는 방법도 존재
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
    
print(result)

# 예제 3-4. 1이 될 때까지 -> 빠르게 동작하는 방법도 존재
n, k = map(int, input().split())
result = 0

while n >= k:
    n -= 1
    result += 1
n //= k
result += 1

while n > 1:
    n -= 1
    result += 1
    
prrint(result)

# 공백을 기준으로 int형 변수 2개 입력받는 코드 -> map 을 이용하면 편리
# n, k = map(int, input().split())

-------------------------------------------------------------------------
# 2강. 구현
# 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정

# 예제 4-1. 상하좌우
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x, y = nx, ny
        
print(x, y)

# 예제 4-2. 시각
h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count += 1
print(count)

# 예제. 왕실의 나이트
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 9
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)

# 예제. 게임 개발
n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
        
count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direciton]
    ny = y + dy[direction]
    
    if d[nx][ny] == 0 and arrray[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
        
print(count)
