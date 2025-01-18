# 상속(Inheritance) : 코드의 재사용과 다형성
# 부모 클래스 (슈퍼 클래스, 상위클래스) : 공통 기능을 가진 클래스
# 자식 클래스 (하위 클래스. 파생클래스) : 공통 기능을 확장하는 클래스

# 부모 클래스(공통 기능)
class Super:
    def __init__(self,name,age):
        print('부모 클래스 생성자 호출')
        self.name = name
        self.age = age

    def display(self):
        print(f"name: {self.name}, age: {self.age}")

# 부모 클래스로 객체 생성
sup = Super('부모 클래스', 55)
sup.display()

print("-"*20)
# 하위클래스 (공통 기능 확장)
class Sub(Super): # 클래스(부모클래스 이름) => 상속개념, name age도 쓸 수 있다
    gender = None
# 부모 변수 초기화
    def __init__(self, name, age, gender): # 받아서 쓰는 것이지 자기가 생성한건 아님
        # super 클래스의 생성자를 무조건 호출하게 되어있음
        # 상위클래스 멤버변수 초기화 : 생성자 호출 => super()
        super().__init__(name, age) # 부모클래스의 __init__ 생성자를 지칭하는 것, 자기가 안만든건 한번더 적어줘야함
        print('자식 클래스 생성자 호출')
        
        # gender 자식 클래스의 자원
        self.gender = gender

    def display(self): # sub 클래스에서 정의한 display
        print(self.name, self.age, self.gender)

# 자식 클래스 객체 생성
sub = Sub('자식 클래스', 25, '여자')
sub.display()
sup.display()


print(sub.name, sub.gender, sub.age)