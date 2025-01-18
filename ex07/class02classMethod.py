# 클래스 멤버 : 클래스 이름으로 호출할 수 있는 클래스 변수. 클래스 메서드
# 클래스 메서드는 'cls' 기본 인수 사용, classmethod 라는 함수 장식자 사용


class DatePro: #date에는 datepro 하나, year, month, day 이렇게 분리
    # 클래스 멤버변수 => 클래스이름.변수로 접근이 가능
    const = "날짜처리 클래스" # 여기는 다 접근이 가능한데

    def __init__(self,year, month, day): # 1 # 여기는 인스턴스하고 해야 가능하다
        # 클래스 이름 으로 접근하면 절대 안됨
        # 생성자에서 self.변수 => 객체.변수 => 객체이름.변수형식으로 접근
        self.year   = year
        self.month  = month
        self.day    = day
        # self 붙인건 인스턴스를 붙이고 들어와야 가능하다
        
    def display(self): # self는 객체 이름을 가지고 쓴다
        print(f"{self.year}-{self.month}-{self.day}")

    # 클래스 메서드
    @classmethod
    # self
    def date_string(cls, dateStr): # 근데 여기는 self 가 아닌 cls => Datepro 라고 쓴다, 클래스 이름으로 메서드를 수행
        year = dateStr[:4]
        month = dateStr[4:6]
        day = dateStr[6:]

        print(f"{year}년 {month}월 {day}일")

date = DatePro(2025,1,18)

# date 객체 이름으로 멤버 변수, 멤버메서드(함수) 접근 
# 여기로는 #1에 있는걸 부를 수 있지만
print(date.year, date.month, date.day)
print(date.const)
date.display()

# 클래스 멤버 : 클래스이름. 멤버변수
print( DatePro.const)

# 클래스 이름으로 접근이 불가능하다
# print(DatePro.year) # 객체 변수는 클래스 이름으로 접근 불가능
# DatePro.const
# Datepro.display() => 에러
# 왜냐하면 init 이랑 display 는 객체 개념으로 쓰이기 때문

DatePro.date_string('20300118') # 클래스이름.메서드(함수)명 접근 가능
date.date_string('20300118')
print(date.const)