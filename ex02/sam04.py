# # # for

# # str = "홍길동홍길순동길이" # 스트링은 기본적으로 리스트 구조
# # # print(str)
# # # print

# # for name in str:
# #     print(name, end = " ")

# # print()

# nums = [1,2,3,4,5,6,7,8,9,10]

# for n in nums: # 순차적으로 불러오는 것
#     if n % 5 == 0:    # 5의 배수가 아니면 다시 위로
#         print(n, end = ' ')

# print()

# # for, range : 숫자 발생 객체
# # n1 = range(5) # 리스트는 아닌데 리스트 형태의 구조가 나온다 
# # for n in range(5): # 0~ 4
# # for n in range(1,5+1): 이러면 끝부분 까지 다 나온다

# for n in range(1,5+1): 
#     print(n , end = " ")

# print()

# for n in range(1,10+1,2): 
#     print(n , end = " ")

# print()

# # 난수 발생 모듈 임포트

# # 반복하는 횟수를 말하는 것인가??
# import random

# list1 = []
# for i in range(10): # 0~ 9 , 반복 횟수
#     r = random.randint(1,10) # 아무 숫자나 만들어주는 것 난수 발생

#     while r in list1: # r값이 list1에 있으면 반복수행
#         r = random.randint(1,10)

#     # 난수 발생 후 저장소에 유무 체크
#     list1.append(r) # 리스트에 저장
#     print (r, end = " ")

# 처음 r 에 난수 발생되고 while 로 내려와서 값이 없으면 false가 되서 밑으로 가서 append에 추가 되는거고
# 총 10개의 난수가 다 채워질때 까지 반복하는거임 ㅇㅇ


import random
list1 = [[],[],[],[],[]]

for out in range(5):
    #--------------------------
    for i in range(6): # 0~ 9 , 반복 횟수
        r = random.randint(1,45) # 아무 숫자나 만들어주는 것 난수 발생

        while r in list1 : # r값이 list1에 있으면 반복수행
            r = random.randint(1,45)

        # 난수 발생 후 저장소에 유무 체크
        list1[out].append(r) # 리스트에 저장
        print (r, end = " ")


# 처음 r 에 난수 발생되고 while 로 내려와서 값이 없으면 false가 되서 밑으로 가서 append에 추가 되는거고
# 총 10개의 난수가 다 채워질때 까지 반복하는거임 ㅇㅇ

    print("-"*10)

    for i in range(5):
        print(list1[i])

    print("="*10)
    list2 = [1,2,3,4,5]
    list3 = [*list2, *list2]

    print(list3)
    list4

    