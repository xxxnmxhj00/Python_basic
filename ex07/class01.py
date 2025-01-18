# # 클래스 : 메서드(함수) + 멤버변수(속성)
# # 함수(메서드) : 기능 수행
# # 멤버변수(속성) : 상태 : 데이터 저장소

# # 사용자가 원하는 특정한 기능을 가지는 자료형 설계
# # 객체 재사용(상속), 객체 캡슐화(정보 은닉) 

# # 함수와 클래스 비교
# def calc_func(a,b):
#     x = a # 지역변수
#     y = b
    
#     def plus ():
#         add = x+y
#         return add
    
#     def minus():
#         m = x-y
#         return sub
    
#     return plus, minus 

# # 함수 호출 내부함수를 수행
# p,m = calc_func(10,20)

# print("== 함수 실행 결과 ==")
# print(p(), m()) # 함수는 호출(실행)
    
# 클래스
class Calc_class: 
    # 클래스 안에 선언된 변수 => 속성, 상태 # 멤버변수
    # 기본설정 값: public => 공개형
    x = y = 0 

    # 생성자(특수 함수) : 생성자 키워드 => '__init__' 다른 이름을 써서는 안된다
    def __init__(self, a,b): # 반드시 self 자기 자신을 지칭하는 것
        self.x = a 
        self.y = b

    # 메서드
    def plus(self):
        p = self.x + self.y
        return p
    def minus(self):
        m = self.x - self.y
        return m 
    
# 클래스(객체를 생성하는 구조도) => 생성 => 객체(인스턴스, 참조형)
#     
# 객체 or 참조형 or 인스턴스 = 클래스()    
myCalc = Calc_class(10,20) # 생성자 호출 # 1이 작동
print('==클래스로 생성된 객체 ==')
print(myCalc.x, myCalc.y)
print(myCalc.plus(), myCalc.minus())

# 자동차 구조 설계(클래스)
class Car:
    cc       = 0
    door     = 0
    carType  = None # 상태를 나타내는 객체를 만듬
    # 값을 안주면 이 변수가 기본값으로 세팅됨

    # 생성자 => 객체가 생성되는 시점에 자동 호출해서 값을 초기화
    def __init__(self, cc=0, door=0, carType=None):
        print('생성자 수행합니다')
        # 속성에 초기값 설정, 객체를 구성하는 멤버 변수를 지칭함
        self.cc = cc
        self.door = door
        self.carType = carType


    # 소멸자(생성자 반대 역할) : 프로그램 종료 시점에 자동 호출
    def __del__(self):
        print('소멸자 수행했습니다')
        print(self.cc)

        # 변수 무효화
        del self.cc
        print(self.cc)

    # 메서드 
    def display(self):
        print("자동차는 %d cc이고, 문짝은 %d, 타입은 %s" %(self.cc, self.door, self.carType))

# 객체 생성 , car1 2 를 인스턴트라고 지칭
# 객체 생성 : 객체.변수, 객체.메소드
car1 = Car(2000, 4, "승용차")
print(car1.cc, car1.door, car1.carType)
car1.display()

car2 = Car(3000, 2, "승용차")
car2.display()
# display()는 공유하고 car1, car2 를 따로 따로 만들어서 이용함

car3 = Car() # 인자 없는 생성자 호출
car3.display()

# 소멸자는 프로그램이 종료되는 시점에 소멸자 발생

print(f"car1주소 : {id(car1)}, car2 주소 : {id(car2)}, car3 주소:{id(car3)}") # 메모리 각각 잡힘