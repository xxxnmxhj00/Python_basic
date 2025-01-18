# 자연어 전처리 예문

from re import findall, sub

# 더미 텍스트
texts = [
' 우리나라 대한민국, 우리나라%$ 만세',
'비타민&라 100GRAM 분량',
'나는 대한민국 사람',
'보험료 15000에 평생 보장 마감 임박',
'나는 홍길동?'
]

# 1단계 : 소문자 변경
texts_re1 =  [t.lower() for t in texts]
print(texts_re1)

# 2단계 : 숫자 제거
texts_re2 = [sub("[0-9]","", text) for text in texts_re1]
print(texts_re2)

# 3단계 : 문장부호 제거
texts_re3 = [sub("[,.?!:;]","",text) for text in texts_re2]
print(texts_re3)

# 4단계 : 영문자 제거

texts_re4 = [sub("[@#$%^&*()]","",text) for text in texts_re3]
print(texts_re4)

# 4 texts : 공백 제거 
texts_re5 = [sub("[@#$%^&*()]","",text) for text in texts_re3]
print(texts_re4)

texts_re5 = [''.join(findall("[^a-z]",text))' for text in texts_re4]
    texts_re6 = [''.join(texts_re5.split())