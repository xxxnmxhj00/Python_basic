# try ~ except ~ : 시스템에 Error가 발생 시 정상적인 종료
# 예외 발생 코드

print("프로그램 시작하기!!!")
x = [10,30,25.2,'num',14,15]
for i in x:
    try:
        print(i)
        y = i ** 2 # 'num'**2 연산 => 예외 발생, 비 정상적으로 종료를 시켜줌
        print('y=',y)
    except:
        print('숫자 아님: ',i)

print('프로그램 종료하기!!!')

# 비 정상적인 종료를 막기 위해 예외 처리를 해줌

print("-"*20)
print("다중 예외 처리 프로그램 시작!!!")
list1 = [10,20,30]

try: 
    div = 1000 / 2.25 # 0으로 나눌 경우 예외 발생 
    print('div=%5.2f'%(div))

    print(list1[100])

    f = open('c:\\test.text') # 파일 열기 에러 발생
    num = int(input('숫자입력:'))
except ZeroDivisionError as e :
    print('산술적 예외 처리 발생')
    print('오류 정보: ', e)
except FileNotFoundError as e : 
    print('파일 열기 예외 처리 발생')
    print('오류 정보: ', e)
except IndexError as e : 
    print('인덱스범위 예외 처리 발생')
    print('오류 정보: ', e)
except Exception as e:
    print('기타  예외 처리 발생')
    print('오류 정보: ', e)

print("프로그램 정상 종료하기")
