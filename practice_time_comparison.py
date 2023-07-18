from random import randint
import time

# 배열에 10,000개의 정수 삽입
array = []
for _ in range(5000):
  array.append(randint(1,100))


# 선택정렬 프로그램 성능 측정
start_time = time.time()

# 선택정렬 프로그램 소스코드
for i in range(len(array)):
  min_index = i # 가장작은 원소의 인덱스
  for j in range(i+1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  array[i], array[min_index] = array[min_index], array[i] # 스와이프

end_time = time.time() # 측정종료
print("선택정렬 성능측정:", end_time-start_time) # 수행시간 출력


# 배열을 다시 무작위로 초기화
array = [ ]
for _ in range(5000):
  array.append(randint(1,100))  # 1에서 100까지의 랜덤한 정수

# 기본정렬 라이브러리 성능 측정
start_time = time.time()

# 기본정렬 라이브러리 사용
array.sort()

end_time = time.time() # 측정종료
print("기본정렬 라이브러리 성능측정:", end_time-start_time) # 수행시간 출력
