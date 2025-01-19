# 클래스 : 변수 + 함수

# 클래스 안에 있는 함수 : self 인자가 있어야 한다
# 클래스 안에 있는 변수 : self.변수
# 클래스 생성자: 생략시 , python이 기본값으로 자동 생성 \

class XY: # name과 self 둘다 멤버 변수
    # 멤버 변수 => 클래스 멤버 변수
    name = 'hong'
    def set_xy(self,x,y):
        # self.변수 => 인스턴스 변수
        # self.x : 현재 클래스 안에 선언되는 변수 => 멤버변수 
        self.x = x  # 멤버 변수 x에 값 저장, self는 객체 주소
        self.y = y # 멤버 변수 y에 값 저장
        # self 는 주소가 넘어가는 거임
        # obj2가 200번지라고해도 self 에다가 주소 넘겨주고 , x y 를 값을 넘기는 거싱

# XY클래스 구조를 생성자로 통해 객체를 생성 obk 스택 xy 힙 : 인스턴스, 참조형, 객체
obj1 = XY() # 객체를 생성한다는 것은 주소를 받아온다 , xy 생성자, 생성자를 통해서 obj1을 받아옴
# XY()생성자가 없기 때문에 100, 200 으로 만들어지는 것
obj1.set_xy(100,200) # 여기서 함수가 만들어지고 

obj2 = XY()
obj2.set_xy(10,20) # 1 에서 만든거 그대로 받아씀

print(id(obj1), id(obj2))
print(obj1.x,obj1.y, obj1.name, XY.name) # obj1 인스턴스, 여기도 인스턴스 변수
# 객체 이름, 클래스 이름 해도 다 나옴
print(obj2.x,obj2.y )