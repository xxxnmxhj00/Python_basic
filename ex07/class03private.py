# 캡슐화 : 클래스에서 여러함수와 여러 변수를 묶어주는 역할
#        : 외부에서 접근이 불가능하게 하는 정보 은닉 역할
# "__" 기호 붙여서 사용하면 private 기능으로 설정

class Account:
    # private 멤버 변수
    __balance = 0 # 잔액
    __accName = None # 예금주
    __accNO = None # 계좌번호

    test = "hong"

    # 생성자 : 멤버 변수 초기화
    def __init__(self,bal, name, no):
        self.__balance = bal
        self.__accName = name
        self.__accNO = no

    # 계좌 정보 확인 
    def getBalance(self):
        return self.__balance, self.__accName, self.__accNO
    
    # 입금하기(setter)
    def deposit(self, money):
        if money < 0 : 
            print('금액 확인')
            return 
        
        self.__balance += money

    # 출금하기(setter)

    def withdraw(self, money):
        if self.__balance < money:
            print('잔액 부족')
            return
        self.__balance -= money
    
acc = Account(1000,'홍길동', '111-123-1234-12')
bal = acc.getBalance()
print(bal, type(bal))

# acc.balance # Error: private 외부에서 접근 불가능
acc.test    # public 외부에서 접근 가능

acc.deposit(10000)
bal = acc.getBalance()
print(bal, type(bal))

acc.withdraw(10000)
bal = acc.getBalance()
print(bal, type(bal))

acc.withdraw(10000) # 잔액부족
acc.deposit(-10) # 금액 확인

