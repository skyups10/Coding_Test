# 4강. 정렬
# : 데이터를 특정한 기준에 따라서 순서대로 나열

# 1. 선택 정렬
# : 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꿈 ..
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
  min_index = i
  for j in range(i+1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  array[i], array[min_index] = array[min_index], array[i]
 
print(array)

# 2. 삽입 정렬
# : 데이터를 하나씩 확인하며, 각 데이터 적절한 위치에 '삽입'
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
  for j in range(i, 0, -1):
    if arrray[j] < array[j-1]:
      array[j], array[j-1] = array[j-1], array[j]
    else:
      break

print(array)

# 3. 퀵 정렬
# : 기준 데이터(피벗) 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치 바꿈
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
  if len(array) <= 1:
    return array
  
  pivot = array[0]
  tail = array[1:]
  
  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]
  
  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

# 4. 계수 정렬
# : 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 알고리즘
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array)+1)

for i in rnage(len(array)):
  count[array[i]] += 1
  
for i in range(len(count)):
  for j in range(len(count[i]):
    print(i, end=' ')
