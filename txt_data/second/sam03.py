# while 조건식 : => 참인 동안 반복 수행, 즉 참이 아니면 수행을 안하다
#   처리할 내용

# cnt = tot = 0 # 변수 초기화
# while cnt < 5: # cnt가 5보다 작으면 반복처리
#    cnt += 1 # 1씩 증가 => 1,2,3,4,5
#    print(cnt) # 여기서 더하기 1 된게 반복

# while cnt < -5 면 한번도 수행이 안됨

# 무한 반복 
# while True: 
#     pass 
# while False
#     pass

#cnt = tot = 0 # 변수 초기화
# while cnt < 5: # cnt가 5보다 작으면 반복처리
#    cnt += 1 # 1씩 증가 => 1,2,3,4,5
#    print(cnt, end = " ") # 여기서 더하기 1 된게 반복

#print()
#print("while end")

# 1 -100 사이 3의 배수 합과 원소 추출

#count = 0
#cnt = 1
#while cnt < 100:
#    cnt *= 3
#    print(cnt, end = " ")

#count = 0
#tot = 0
#while count < 10 :
#    count += 1          # 1,2,3,
#    tot += count        # +1, +2, +3, 
#    print(count, tot)

count = 0
tot = 0
dataset = [] # 리스트 생성
while count < 100 :
    count += 1          # 1,2,3,

    # 3으로 나눈 나머지가 0이면 3의 배수로 판단 
    if count % 3 == 0:
        tot += count  # tot = tot + count , # +1, +2, +3, 
        print(count, tot)

        dataset.append(count)


# while True: 
#     num = int(input("숫자:"))
#     if num == 0:
#         #continue
#         break
#     print(f"입력된 숫자는 {num}")


