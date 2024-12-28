# 표준 입력 장치 (키보드), 표준 출력 장치 (모니터)
# 키보드를 통해 숫자를 받아서 전송로를 통해서 숫자를 메모리 기억 장소에 넣어줄 때는 절차가 필요하다
# 외부 장치로부터 넘어온 자료는 스트림 구조
# num = input("숫자 입력:") # 숫자를 넣어주면 된다
# print(num, num*3, type(num))
#print(int(num) * 3) # 정수 문자형 -> 정수형 변환
# print(float(num)) # 실수 문자형 -> 실수형 변환 

print('n1=',10, 100+20)
print('010','1234','5678', sep = ',') # 앞의 3개 사이를 콤마로 구분하겠다, 구분기호 콤마
print('010','1234','5678', sep = '\n') # 앞의 3개 사이를 콤마로 구분하겠다 # enter 키
print("-"*10)

# 1. format() : 형식이 있는 출력을 하고자 할 때 : %f, %d, %o, %x, %s,%c
print('원주율 =', format (3.14159,"8.2f"))
print('금액= ',format(10000,"10d")) # 자리수 10개 확보
print('금액= ',format(10000,"3,d")) # 자리수 10개 확보

# 2.
name = "홍길동"
age = 35
price = 125.456

# print("당신의 이름은 홍길동이고, 나이는 20세 입니다. 가진 돈은 10원 입니다.")
print("당신의 이름은 %s이고, 나이는 %d세 입니다. 가진 돈은 %.2f원 입니다."%(name, age, price))

# 3.
# print("이름 : 홍길동, 나이 :20세, 가진 돈은 10원")
print("이름 : {}, 나이 :{}세, 가진 돈은 {}원".format(name, age, price))
print("이름 : {2}, 나이 :{1}세, 가진 돈은 {0}원".format(name, age, price))

# 4. 
str1 = f"이름 : {name}, 나이 : {age}, 금액 : {price}"
print(str1)

# 여러 텍스트 쳐야될때,
m= """this is
multi line
string"""

print(m) # 줄바꿈 기능 안넣더라도 쭉쭉 나옴

m= """
this is
multi line
string
"""
print(m) # 줄바꿈 기능 안넣더라도 쭉쭉 나옴

# 유지하면서 줄바꿈도 안하고 싶다 ?
m= """\
this is
multi line
string\
"""
print(m) # 줄바꿈 기능 안넣더라도 쭉쭉 나옴