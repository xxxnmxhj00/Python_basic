# __call__() : 인스턴스를 함수처럼 호출

class Multiplier:
    def __init__(self,mul):
        self.mul = mul
    def __call__(self, num):
        return self.mul*num
    
double = Multiplier(2)
triple = Multiplier(3)
print(double(100),triple(5))

# double 객체(인스턴스)는 __call__ () 함수 이름을 지칭
print(double(100))

class Data:
    def __init__(self,data):
        self.data = [-1] + data # 리스트 구조 연산 : [1] + [2,3,4]

    def __len__(self):
        print("__len__()함수 호출")
        return len(self.data)
    
d = Data([1,2,3])

print(d.data)
print(len(d), d.__len__())

