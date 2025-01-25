# excel 파일 처리

import pandas as pd

# excel 파일 열기
sam = pd.ExcelFile('sam_kospi.xlsx') # sam은 파일 핸들러

# excel 파싱 
kospi = sam.parse("sam_kospi")
print(kospi.info())

# 컬럼 추출
high = kospi['High']
low = kospi['Low']

# 평균
from statistics import mean

print('high mean= ', mean(high), high.mean())
print('low mean= ', mean(low), low.mean())


