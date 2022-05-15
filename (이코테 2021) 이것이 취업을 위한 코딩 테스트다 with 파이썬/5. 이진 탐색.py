# 5강. 이진 탐색
# : '배열 내부의 데이터가 정렬되어 있어야만' 사용할 수 있는 알고리즘

# 순차 탐색
# : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법

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
