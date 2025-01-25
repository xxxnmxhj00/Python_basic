# pandas 모듈

import pandas as pd
import os
print('현재 폴더 위치:',os.getcwd())

# csv 형식 파일 읽기
score = pd.read_csv('score.csv')

# 파일 정보
print(score.info())
print(score.head()) # 컬럼명 포함 앞 5개 행

# 컬럼 추출
kor = score.kor # 객체 컬럼
eng = score['eng']
mat = score['mat']
dept = score['dept']

print(type(kor))

from statistics import mean
print('max kor = ', max(kor))
print('max eng = ', max(eng))
print('min mat = ', min(mat))
print('avg dept = ', round(mean(dept)))

# dept 빈도수
dept_count = {} # dict, set 

for key in dept:
    dept_count[key] = dept_count.get(key,0) + 1 # 만약 해당 키가 없다면, 기본값 0을 반환합니다

print('dept:',dept_count)

