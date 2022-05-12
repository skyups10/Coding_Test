# 6강. 다이나믹 프로그래밍
# : 연산 속도와 메모리 공간을 최대한으로 활용할 수 있는 효율적인 알고리즘

# 2가지 방식 : 탑다운, 보텀업
# 최적 부분 구조, 중복되는 부분 문제에 주로 사용

# 8-1.py 피보나치 함수 소스코드
def fibo(x):
  if x==1 or x==2:
    return 1
  return fibo(x-1) + fibo(x-2)

print(fibo(4))

# 8-2.py 피보나치 함수 소스코드(재귀적)
d = [0] * 100

def fibo(x):
  if x==1 or x==2:
    return 1
  if d[x] != 0:
    return d[x]
  d[x] = fibo(x-1) + fibo(x-2)
  return d[x]

print(fibo(99))

# 8-5.py 1로 만들기
x = int(input())

d = [0] * 30001 # 테이블 초기화

for i in range(2, x+1):
  d[i] = d[i-1] + 1
  if i % 2 == 0:
    d[i] = min(d[i], d[i//2] + 1)
  if i % 3 == 0:
    d[i] = min(d[i], d[i//3] + 1)
  if i % 5 == 0:
    d[i] = min(d[i], d[i//5] + 1)
 
print(d[x])
