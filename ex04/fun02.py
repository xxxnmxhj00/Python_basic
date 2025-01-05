# # builtins 내장 함수

# print(abs(10), abs(-10))

# # 모든 요소가 True => True => and 유사 기능
# # print( all([1,True,10,-15.2]))
# # print( all([1,True,10,-15.2,0])) # False "", [], {}, 0 all 은 and 연산자를 쓸 수 있다.
# # print( all([1,True,10,-15.2,""]))
# # print( all([1,True,10,-15.2,[]]))

# # 하나 이상의 요소가 True => True: OR 유사 기능
# print("-- any()")
# print(any([0,"",[],{}]) )
# print(any([0,"",[],{10}]) )

# print(10, bin(10), hex(10), oct(10))
# # "10+20" => 10+20
# print(eval("10+20"))

# # 문자의 아스키코드 번호
# print(ord("A"), ord("a"))

# print(pow(3,2)) # 3의 2승 
# # [1,-3,5,4] => [1,3,5,4] => 정렬
# print(sorted([1,-3,5,4], key = abs))

# names = ["BANANA","GRAPE","apple"]
# print(sorted(names)) # ASCII에선 대문자가 더 작음
# print(sorted(names, key=lambda x:x.lower()))

# nums = [[500,6], [10,20,30]] # 길이 2 , 3
# print(max(nums, key = len)) # 길이가 큰 쪽을 기준으로 정렬, 정렬의 기준치를 바꿀 수 있다
# print(max(nums, key = sum)) # 값의 기준을 만들 수 있다

# n1 = [1,2,3]
# n2 = ["one", "two", "three"]
# # n3 ="abc" # n3[0], n3[1], n3[2]
# n3 = "abcdefg"

# # # n1, n2 각각의 요소를 튜플 방식으로 묶어줌
# # for item in zip (n1,n2): 
# #     print(item)

# for item in zip (n1,n2,n3): # zip(n1, n2)는 n1과 n2의 요소들을 순서대로 짝지어 튜플
#     print(item) # 3개 있으면 3개도 다 묶어버림

# print("-" * 10)

# names2 = ["홍길동","홍길순","동길이"]

# # enumerate() 함수는 반복 가능한 객체(iterable)의 요소를 순회하면서 인덱스와 값을 함께 반환하는 Python의 내장 함수
# for i, n in enumerate(names2, 100):
#     print(i,n)

# chars = ["*","+","#","&"]
# for i, c in enumerate(chars,1): # 1을 스타트 끊으면 1부터 시작한다
#     print(c*i)

# 객체 타입 판별 
# isinstance() 함수는 Python의 내장 함수로, 객체가 특정 클래스의 인스턴스인지 확인하는 데 사용
print( isinstance(100, int), isinstance(10.2, int))
print( isinstance(100, float), isinstance(10.2, float))
print( isinstance(100, str), isinstance("10.2", str))
print( isinstance([1,2], list), isinstance((1,2), list))
print( isinstance([1,2], tuple), isinstance((1,2), tuple))
print( isinstance([1,2], dict), isinstance({"name":"holding"}, dict))
print(type("abc"), type([]), type({1,2}), type((10,)), type({"age":10}))


