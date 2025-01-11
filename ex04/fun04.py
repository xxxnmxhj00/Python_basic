# # 사용자 정의 함수

# # def 함수이름():
# #     수행할 내용

# # 1. 기능 수행하는 단순 함수 : 매개변수 없고, 반환 값 없는 형태
# # 함수 선언
# def fun1():
#     print("*"*10)
#     print('전달 받은 인자가 없고 반환값 없는 함수')
#     print('Fun1()')
#     print("*"*10)

# # 함수 호출(tlfgod)
# # 실행하고 return 하고 없어지고 
# # fun1()

# # #2. 기능 수행하는 단순 함수: 매개 변수 있고, 반환 값 없는 형태
# # # 매개변수는 함수나 메서드의 정의에서 사용되는 변수로, 함수가 호출될 때 외부에서 전달되는 값을 받아들이기 위해 사용
# # def fun2(name): # name 이 매개변수
# #     print("-" * 20)
# #     print("안녕하세요. ",name,"님 !!!")
# #     print("-"*20)

# # # 던져 준 데이터로만 값이 반환됨
# # # 자원의 재사용
# # fun2("홍길동")
# # fun2("동순이")
# # fun2("강감찬")

# #3. 기능 수행하는 단순 함수 :매개견수 있고, 반환 값 있는 형태

# def fun3(x, y):
#     # 사칙연산 함수 수행
#     print("사칙연산 함수 수행")
    
#     # x와 y의 합계를 계산하여 지역변수 tot에 저장
#     tot = x + y  # 지역변수 실행하는 동안에는 남아있는데 리턴하고 나서는 사라짐
    
#     # x와 y의 차를 계산하여 지역변수 sub에 저장
#     sub = x - y
    
#     # x와 y의 곱을 계산하여 지역변수 mul에 저장
#     mul = x * y
    
#     # x를 y로 나눈 결과를 계산하여 지역변수 div에 저장
#     div = x / y
    
#     # 계산 결과를 튜플 형태로 반환 (tot, sub, mul, div)
#     return tot, sub, mul, div  # 내가 부른 쪽에 값을 주겠다

# # 함수 실행
# a, b, c, d = fun3(10, 3)  # fun3 함수 호출: 인자로 10과 3을 전달하고 결과를 각각 a, b, c, d에 저장

# # 결과 출력
# print(a, b, c, d)  # 출력: 합계, 차이, 곱셈 결과, 나눗셈 결과

# # 피타고라스의 정의 함수 만들기

# def pytha(s,t):
#     a = s**2 - t**2
#     b = 2+s*t
#     c = s**2 + t**2

#     print("3변의 길이 : ", a,b,c,)
#     return a,b,c

# a1,b1,c1 = pytha(2,1)
# print("함수 반환값 :" ,a1,b1,c1)

def mysum (start, end):
    sum = 0
    for i in range(start,end+1):
        sum += i

    return sum

print( mysum(1,10))
print( mysum(1,100))
print( mysum(5,10))

# 가변인자를 만들면 더 편하게 할 수 있다?
