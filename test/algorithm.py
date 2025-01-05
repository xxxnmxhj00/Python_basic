# 알고리즘 : 어떤 문제를 해결하기 위한 일련의 절차
# 자원의 낭비가 적고 
# 정렬, 최대값, 최소값, 검색...

import random

dataset= []
for i in range(10): # 0~9
    rnd = random.randint(1,100) # 1과 100 사이 숫자 발생
    # print(rnd, end = ' ')
    dataset.append(rnd)

print(dataset)

# 2. 최댓값, 최솟값 변수 초기화
vmax = vmin = dataset[0]
# 3. 최댓값, 최솟값 구하는 기능

for i in dataset: # 비교할 데이터를 순차적으로 호출 
    if vmax < i : # 최댓값 보다 데이터가 더 크면 데이터를 최댓값으로 설정
        vmax = i

    if vmin > i:    # 최솟값 보다 데이터가 더 크면 데이터를 최솟값으로 설정
        vmin = i
print(f"최댓값 : {vmax}, 최솟값 : {vmin}")


