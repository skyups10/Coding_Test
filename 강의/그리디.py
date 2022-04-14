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

# 공백을 기준으로 int형 변수 2개 입력받는 코드 -> map 을 이용하면 편리
# n, k = map(int, input().split())
