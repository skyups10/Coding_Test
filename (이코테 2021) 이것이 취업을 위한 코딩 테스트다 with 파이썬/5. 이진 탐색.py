# 5강. 이진 탐색
# : '배열 내부의 데이터가 정렬되어 있어야만' 사용할 수 있는 알고리즘

# 순차 탐색
# : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
# 7-1.py 순차 탐색 소스코드
def sequential_search(n, target, array):
  for i in range(n):
    if array[i] == target:
      return i+1
    
print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0]) # 원소 개수라 int형 변환
target = input_data[1]

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

print(sequential_search(n, target, array))

# 7-2.py 재귀 함수로 구현한 이진 탐색 소스코드
def binary_search(array, target, start, end):
  if start > end:
    return None
  mid = (start+end) // 2
  
  if array[mid] == target:
    return mid
  
  elif array[mid] > target:
    return binary_search(array, target, start, mid-1)
  
  else:
    return binary_search(array, target, mid+1, end)
  
# 7-3.py 반복문으로 구현한 이진 탐색 소스코드
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
  print("원소가 존재하지 않습니다.")
else:
  print(result + 1)

# 코딩 테스트에서의 이진 탐색 -> 암기 필요!

# 7-4.py 한 줄 입력받아 출력하는 소스코드
# 데이터의 개수가 1,000만 개를 넘어가거나 탐색 범위의 크기가 1,000억 이상이라면 input() 함수 대신 sys 라이브러리의 readline() 함수 이용
# 해당 함수 사용시 꼭 rstrip() 함수 호출 필요!

import sys
input_data = sys.stdin.readline().rstrip()

print(input_data)

# 예제. 부품 찾기
# - 이진 탐색 이용
# - 계수 정렬 이용
# - 집합 자료형 이용

# 예제. 떡볶이 떡 만들기
