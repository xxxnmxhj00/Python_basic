# for 문, while문
# for 변수 in iterable: ## 반복자
    # 수행할 반복 구간
    # ...

# for c in "apple" : # 첫번재 값을 하나씩 빼와서 a를 c에 넣고 # apple 개수 만큼 계속 반복을 한다
#     print(c)
#     print("--")

# for n in [0,1,2,3]:
#     print(n, end = " - ")

# # apple [ 0,1,2,3] 을 반복자 iterable 이라고 한다

# for i in range(3): # 0, 1, 2 
#     print(i)

# for i in range(1,3) : # 1, 2 (3은 포함되지 않음)
#     print(i)

# for i in range (1,10+1):
#     print(i)

# 242 243 섞어서 함

# for num in range (1,100+1): # 1 ~ 100 까지 반복
#     if num % 10 == 0:
#         print(num, end = ",")

# 값이 있는 리스트 객체
files = ["apple.jpg", "banana.png", "names.txt","grape.jpg","profiles.txt"]
jpgs = [] # 비어 있는 리스트 객체

# apple.jpg 가 f 로 들어와서 안에서 뒤에서부터 .jpg가 들어오는거죠
for f in files:
    print (f, f[-4:])

# [ 1,2,3 ] + [5] = [1,2,3,5]
# [1,2,3] + " abc " =>?
    if f[-4:] == '.jpg': # 확장자가  '.jpg' 조건만 처리 
        jpgs += [f] # jpgs = jpgs + [f]
print(jpgs)


# list1 = []

# print([1,2,3]+[10])
# print([1,2,3] + 10) # error 걸리는거임
# list1 = list1 + [1,2] # [] + [1,2]
# list1 += [3,4]
# print(list1)
