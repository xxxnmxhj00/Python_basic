
class XY: 
    def __init__(self, x, y):
        # __변수 => 외부에서 접근 불가능 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.__x = x
        self.__y -= y
        self.name = "동순이"
    
    # 함수와 데코레이터 기능을 활용하여 인스턴스 변수 접근
    @property
    def x(self):
        return self.__x
    
    # 동일한 이름의 메서드에 .setter 붙인 데코레이터 : setter기능

    def x(self, value):
        if value <0:
            pri

c = XY(3,4)
print(c.x)

c.name = '길순이'