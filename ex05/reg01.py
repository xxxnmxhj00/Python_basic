# 정규 표현식(Regular Expression)
# 특정한 규칙을 가진 문자열의 집합을 표현, 문자열 검색, 치환 용도로 사용 
# 메타문자
# . => .x 또는 x. : 임의의 한 문자가 앞에나 뒤에 오는 패턴 지정
# ^ => ^x : x로 시작하는 문자열
# $ => x$ : x로 끝나는 문자열
# * : x*  : x 가 0번 이상 반복
# + => x+ : x가 1번 이상 반복
# ? => x? : x가 0또는 1개 존재
# | => abc|ABC : abc 또는 ABC
# [] => =[x] : x문자 한개 일치
#[^] => [^x] : x 문자 제외
# {n} => x{n} : x문자가 n반복
# {n}, {n,}, {n,m}

import re # 이건 re 전부 임포트 
# # from re import final # re 안에서 final 임포트
# # findall 은 정규 표현식을 사용하여 문자열에서 특정 패턴과 일치하는 모든 부분 문자열을 찾아 리스트로 반환
# st1 = '1234 abc 홍길동 ABC_555_6 만세1234 이사도시'

# # 숫자 찾기
# print(re.findall('1234', st1)) # re 일때는 re.findall 이라고 지칭을 전부 해야함 근데 from 가지 하면 그냥 해도 바로 뜸
# print(re.findall('[0-9]',st1)) # 숫자들만 뽑아서 다 내라
# print(re.findall('[0-9]{3}',st1)) # 연속해서 숫자 3개 붙은 것들만 추출해라
# print(re.findall('[0-9]{3,}',st1)) # 3번이상 반복 그래서 1234, 555가 나옴
# print(re.findall('\\d{3,}',st1)) #\\d 가 [0-9]랑 같음

# # 문자열
# print(st1)
# print(re.findall('[가-힣]{3,}', st1))
# print(re.findall('[a-z]{3}', st1))
# print(re.findall('[a-zA-Z]{3}', st1))
# print(re.findall('\\w{3}', st1)) # 단어 문자는 [a-zA-Z0-9_]에 해당하며, 영어 대소문자, 숫자, 밑줄 _을 포함합니다.

# 특정 위치의 문자열 찾기
st2 = 'test1abcABC 123mbc 456test'
print(st2)
print(re.findall('^test',st2)) # ^ test로 시작하는 문자열
print(re.findall('st$',st2))  # st로 끝나는 문자열

print(re.findall('.bc',st2))  # 앞에 한자 그리고 bc로 끝나는거, 한 문자에 대한 와일드 문자
print(re.findall('t.',st2))  # 

st3 = 'test^홍길동 abc 대한*민국 123$tbc'
words =re.findall('\\w{3,}', st3)
print(words) # 문자는 없음 

words2 = re.findall('[^^*$]+', st3) # ^*$ 를 제외한 문자를 가지고 와
# + => 바로 앞의 패턴이 1개 이상 연속으로 나타나는 경우를 매칭
print(words2)


