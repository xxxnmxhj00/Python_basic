# 함수 장식자 : 데코레이터(decorator)
# 함수의 기능을 변경하거나 확장할 경우에 사용, 보조역할을 해주는 느낌

# 레퍼 함수 
# def wrap (f): # hello() 함수의 주소가 인자로 전달 #3

#     def new_decorated():
#         print('반가워요') # 시작 부분
#         f() # hello() 함수를 지칭
#         print('잘가요') # 종료 부분

#     return new_decorated # return 하면서 new_decorated 자동 호출, 앞에서도 
# # 앞에서도 return 해도 

# # 함수 장식 적용
# @wrap # 이걸 장식함수로 사용하겠다 #2
# def hello():
#     print("Hello !!!!","홍길동") #1

# 함수 호출
# hello() # 만약에 @wrap 가 없으면 
# 주 기능 하기 전에 전 후에 장식하는 느낌
# hello 실행하면 wrap이 실행되고 그래서 반가워요 f 잘가요 순으로 실행하고 return 으로 감

# p196 

# def deco(f):
#     def new_f():
#         print("f() is called")
#         return f() # return hi()
    
#     return new_f 

# @deco
# def hi():
#     print("hi")

# hi()

def func_with_print(f):
    def new_func(x):
        y = f(x) # y = double(x)
        print(y)
        return y
    
    return new_func # new func() 함수를 실행한다는 의미     

@func_with_print
def double(x):
    return 2*x
print(double(5))