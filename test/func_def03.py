# def mul(*a): # 전달 받는 인자의 개수가 특정 개수로 정해지지 않을 경우, 선언문 자체가 튜플 
#     result = 1

#     # print(a, type(a))
#     for i in a:
#         result *= i 
#         # print(f"{i} 까지 누승: {result}") # 변수값을 넣을때는 format 문을 써야됨

#     return result # result 값만 가지고 와서 출력


# r1 = mul(3,4,100,20,3)
# print(r1)

# "**매개변수" => 딕트 타입
# def group_by_age(**kwargs):
#     print(kwargs)
#     group ={"adult" : [], "non_adult" : []}

#     for name, age in kwargs.items():
#         print(name, age)
#         if age> 18:
#             group["adult"] += [name]
#         else :
#             group["non_adult"] += [name]
    
#     return group # return 문은 함수의 실행을 즉시 종료, group 딕셔너리를 함수의 호출자에게 전달

# r1 = group_by_age(kim = 25, jeong = 16, a=17, b =20, c=30, d=45)
# print(r1)
    
# p 188

# def len_args(*args):
#     # *args: 가변 인자를 튜플로 받습니다.
#     # len(args): args 튜플의 길이를 반환합니다.
#     return len(args)

# # 개별 인자로 함수 호출
# print(len_args(1,2,3,4,5))  # 출력: 5
# # 설명: 5개의 개별 인자가 전달되어 args는 (1,2,3,4,5) 튜플이 됩니다.

# # 리스트를 단일 인자로 함수 호출
# print(len_args([1,2,3,4,5]))  # 출력: 1
# # 설명: 리스트 하나가 단일 인자로 전달되어 args는 ([1,2,3,4,5],) 튜플이 됩니다.


# # def print_kwargs(**kwargs):
# #     print(kwargs)

# # print_kwargs(animal="ape", fruit="apple")

# def len_args_kwargs(*args, **kwargs):
#     print(len(args), len(kwargs))

# len_args_kwargs(1,2,3,animal="ape", fruit="apple")

# def test1(*a, **b): # *a 는 일반데이터 , *b는 키와 값이 같이 들어가는 데이터
#     print(len(a), len(b))

# test1(10,20,30,animal ="ape",fruit="apple")

# # 변수의 타입을 명시적으로 선언 추세, 타입 힌트

# def test2(name:str, age:int):
#     print(f"당신의 이름은{name}, 나이는 {age}")

# test2("홍길동",20)

# def test3(nums : list) -> int:
#     return sum(nums) # sum을 return 해서 test3 에다가 넣어주는 것이다

# r1 = test3([1,2,3,4,5])
# print(r1)

# 람다 함수 
eq = (lambda a,b: a+b)(10,20)
print(eq)
eq2 = lambda a,b,c : "{}x+{}y={}".format(a,b,c)
print( eq2(5,4,3))

# 실행 print( "{}x+{}y={}".format(5,4,3) )

# lambda 함수를 사용하여 test3이라는 이름의 익명 함수를 정의합니다.
# join은 문자열 메소드로, 리스트의 모든 요소를 하나의 문자열로 결합
test3 = lambda x : "/".join(x)

# test3 함수를 호출하고 그 결과를 출력합니다.
print(test3(["apple", "banana", "grape"]))

# 출력 결과: apple/banana/grape

def test4(x):
    t = "/".join(x)
    # print(t)
    return t

r1 = test4(["apple", "banana", "grape"])
print(r1)