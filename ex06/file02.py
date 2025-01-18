# 테스트 자료 읽기 관련 함수
# read() : 전체 텍스트 자료를 한 번에 읽기, 읽어온 자료는 문자열 (str) 자료형을 반환
# readlines() : 전체 텍스트 자료를 줄 단위로 읽기, 읽어온 자료는 리스트(list) 자료형으로 반환
# readline() : 한 줄 단위로 읽기, 읽어온 자료는 문자열 (str) 자료형으로 반환

try:
    #1. read()
    ftest = open('ex01/sam02.py', mode = 'r', encoding='utf-8')
    full_text = ftest.read()

    print('-'*30)
    print("#1. read()")
    print(full_text)
    print(type(full_text))

    # 2. readlines()
    ftest3 = open('ex01/sam03.py',mode = 'r', encoding='utf-8')
    lines = ftest3.readlines()

    print('-'*30)
    print("#3. readLines()")
    print(lines)
    print(type(lines))

    # 3. readlines()
    ftest4 = open('ex01/sam04.py',mode = 'r', encoding='utf-8')
    lines4 = ftest4.readline()

    print('-'*30)
    print("#3. readLines()")
    print(lines4)
    print(type(lines4))

except Exception as e:
    print('Error :', e)
