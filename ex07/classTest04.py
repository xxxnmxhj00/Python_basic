
# 상위 클래스 정의 : 공통 기능 수행하는 클래스 정의
class FindPath:
    # 생성자(이름, 나이 초기화)
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def find(self, start, dest):
        print(start, dest)

# 하위 클래스 정의 : 공통 기능의 확장개념 정의
class FPBicycle(FindPath):

    # 생성자(주소)
    def __init__ (self, name,age,addr):
        # 부모클래스 멤버변수 초기화
        super().__init__(name, age)
        # 자식 클래스 멤버변수 초기화 
        self.addr = addr

    # 오버라이딩 (함수 재정의)
    def find(self, start, dest):
        # super(): 상속받은 부모 클래스를 지칭
        super().find(start, dest) # 부모가 가진 find()를 호출하겠다
        print("width Bicycle") # 서울 부산 보다 여기가 우선

bicycle = FPBicycle('동순이',10,'부산')
print(bicycle.name, bicycle.age, bicycle.addr)
# bicycle.name, bicycle.age