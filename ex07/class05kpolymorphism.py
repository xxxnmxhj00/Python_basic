
# 다형성 : 여러 가지 형태를 가질 수 있는 기능
# 하나의 참조 변수로 여러 타입의 객체를 참조 할 수 있는 것
# ex)  "+" 연산자 => 10+20 : 산술식 연산, "10"+"20" : 문자열 연결

# 상속 : 부모 클래스(공통기능), 자식 클래스(공통 기능 확장)

# 1. 상위 클래스 (부모, 수퍼, 베이스)
class Fligt:
    title_name ='다형성'
    def fly(self): 
        print('날다, fly 원형 메서드')

# A B P 전부 Flight를 상속 받는다

# 2. 자식 클래스 : 비행기, 1의 기능을 다 가지고 나온다
class Airplane(Fligt):
    name = '비행기'
    # 함수 재정의(오버라이딩)
    def fly(self):
        print('비행기가 날다')

class Bird(Fligt):
    name = '새'
    def fly(self):
        print('새가 날다')

class PaperAirplane(Fligt):
    name = '종이비행기'
    def fly(self):
        print('종이 비행기가 날다')  

print('--부모 클래스--')
fligt = Fligt()
print(fligt.title_name)
fligt.fly()

print('-- 자식 클래스 : 비행기')
air = Airplane()
print(air.name, air.title_name)
air.fly()

print('-- 자식 클래스 : 새')
bird = Bird()
print(bird.name,bird.title_name)
bird.fly()

print('--자식클래스 : 종이비행기')
paper = PaperAirplane()
print(paper.name,paper.title_name)
paper.fly()

print('--- 다형성 구현')
fligt2 = Fligt() # 상위요소는 하위 요소의 주소를 관리할 수 있다, 그니까 fligt2의 거를 사용할 수 있다.
# 요소마다 바껴서 값을 받는다고 생각을 하면 될듯

# 저장한 곳의 하위요소들에 다른 주소가 들어가는것임, 자식요소의 주소를 받아와서 쓰더라도 인식이 된다는 뜻
# 상위 클래스 객체 = 하위(자식)클래스 객체
fligt2 = air
fligt2.fly()

fligt2 = bird
fligt2.fly()

fligt2 = paper
fligt2.fly()
