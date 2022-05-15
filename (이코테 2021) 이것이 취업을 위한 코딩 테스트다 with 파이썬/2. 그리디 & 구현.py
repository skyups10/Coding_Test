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

# 2강. 구현
# 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정

# 예제 4-1. 상하좌우
# 예제 4-2. 시각
# 예제 4-3. 왕실의 나이트
