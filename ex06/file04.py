# with 블러와 인코딩

try:

    # with 블럭을 벗어나면 자동으로 open한 객체는 소멸됨
    with open('ex06/test.py', mode = 'w', encoding= 'utf-8') as ftest:
        ftest.write('파이썬 파일 자석 연습')
        ftest.write('\n파이썬 파일 쓰기 테스트2')
    
    with open('ex06/test.py', mode= 'r', encoding='utf-8') as ftest2:
        print(ftest2.read()) # 전체 다 읽어오는 것

except Exception as e:
    print('Error 발생:', e)
finally: # 예외와 상관없이 무조건 수행
    print('무조건 수행하는 구간')
    print('자원 해제할 때 사용')