# 문자열 처리 함수
# 1. 특정 글자 수 반환
str1 = "this is one line string"
print('길이:',len(str1))
print('t 글자수:', str1.count('t'))

# 특정 문자 비교 판단
# startswith() 함수는 문자열이 특정 접두사(문자열)로 시작하는지 확인할 때 사용하는 메서드
print(str1.startswith('this'))
print(str1.startswith('that'))

# 특정문자 교체 
print(str1.replace('this','that'))
print(str1.replace(" ","")) # 공백을 찾아서 공백을 지우는 것

# 문자열 분리
str2 = """\
홍길동
여러줄을 사용하기
길순이 동길이\
"""
print(str2)

# sent = str2.split(' ')
# print(sent)

sent = str2.split('\n') # 특정 문자를 기준으로 분리해서 리스트구조 저장
print('sent=',sent)

sent2 = ','.join(sent)
print(sent2)

# \',\",\\ 파일 입출력 할때 경로 설정  c:\abc\ttt.txt

print("홍길동\n홍길순\n동길이")
print("홍길동\t홍길순\t동길이")
print("홍길동\t홍길순\t동\길이")

# 특정문자 포함여부 판별
print("안녕" in "안녕하세요") # 문자 포함 여부를 판별할 때 씀
print("바보" in "안녕하세요")
print(1 in [1,2,4,5]) # True
print([1] in [1,2,4,5]) # False [1]은 리스트이고, 1은 정수입니다. 두 값은 전혀 다른 타입이기 때문에 False가 반환됩니다.
print([1] in [1,2,4,5, [1]]) # True