# # P194
# # 함수의 객체화(주소개념)

# # def mul(a,b):
# #     return a*b

# # mul2 = mul # mul 주소를 mul2에 저장
# # print( id(mul2), id(mul))
# # print( mul2(3,4))

# # 메개변수 -> 인자값(데이터), 함수식(함수의 주소)도 전달 가능
# def func01(f): # f에는 func02 함수의 주소를 넘겨받음
#     print( "f(2,3)={}".format(f(10,20)))

# def func02(a,b):
#     return a*b

# # r1 = func01(10,20)
# # r2 = func02 # 함수 하나에 이름이 2개 붙음, 주소를 공유한다는 느낌
# # print(r1, r2(100,200), id(func02), id(r2))

# func01( func02 ) #매개변수 함수 인자를 넘긴다는 것은 함수의 주소를 넘긴다는 것이다

# def func01(f): # f는 함수 객체를 받는 매개변수
#     # f(10,20)을 호출하고 그 결과를 포맷팅하여 출력
#     # 여기서 f는 func02 함수를 가리킴
#     print("f(2,3)={}".format(f(10,20)))
#     # 주의: f(2,3)은 단순 문자열이며, 실제로는 f(10,20)이 실행됨

# def func02(a,b):
#     # 두 인자를 곱한 결과를 반환
#     return a*b

# # func01 함수 호출, func02를 인자로 전달
# func01(func02)
# # 이 호출은 다음과 같이 해석됨:
# # 1. func02 함수 객체(주소)가 func01의 매개변수 f로 전달됨
# # 2. func01 내부에서 f(10,20)이 호출되며, 이는 func02(10,20)과 동일
# # 3. func02(10,20)은 200을 반환
# # 4. "f(2,3)=200"이 출력됨


def func03():
    def new_func03(a,b):
        # return 의미는 new_func03() 함수를 종료
        return a * b
    
    # return 의미는 func03() 함수를 종료
    return new_func03 # new_func03() 함수 주소를 가지고 반환

m = func03() # m에는 new_func03() 함수의 주소를 저장
print( m(10,20) )

# 변수를 주는게 기억장소를 주는게 그냥 일급함수라고 이해합시다
# 중첩함수에서 외부함수나 내부함수를 변수에 저장
# => 일급함수(First class Function)
# 내부함수는 외부함수의 return 명령문을 이용하여 반환 
# => 함수 클로저 (Function Closure)

#1. 일급함수와 함수 클로저

# def a(): # outer function
#     print('a()함수 : outer function')

#     def b(): # inner function
#         print('b()함수 : inner function')

#     print('a()함수 종료시 b()함수의 주소를 반환')
#     return b

# f1 = a()
# f1() # inner function b() 함수가 실행

# 함수 클로저 예시
data = list(range(1,101))
print(data)

def out_func(data):
    dataset = data

    def tot():
        tot_val = sum(dataset)
        return tot_val

    def avg(tot_val):
        avg_val = tot_val / len(dataset)
        return avg_val

    return tot, avg
    
# 외부 함수 호출(실행)
total, average = out_func(data) # tot(), avg() 함수의 주소를 반환 total 은 tot average 는 avg 의미

tot_data = total() # 함수 이름을 전달해준거, total() 함수를 실행하라고 위해서 받았으니까
print('tot=', tot_data)

avg_data = average(tot_data) # average()를 받아가지고 온거임
print('avg=', avg_data)

# 외부함수가 종료됐다고 하더라도 내부함수에 함수가 소멸이 안된다는 것이 특징

# 195 

def double(x):
    return 2*x
def func_with_print(f): # f에는 double() 함수 주소
    def new_func(x):
        y = f(x) # y = double(x)
        print(y)
        return y
    return new_func

# 함수의 주소 전달 받기
new_double = func_with_print(double)
print(new_double(5))
