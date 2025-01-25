# 웹 크롤링(Crawling): 웹 상의 정보들을 탐색하고 수집하는 작업

# 모듈 import 
import urllib.request as req
from bs4 import BeautifulSoup

# news 제공 포털 사이트 url
url = 'https://news.daum.net'

# 1. url 요청
res = req.urlopen(url)
source = res.read()

# 2. 소스 디코딩(문자 디코딩)
source = source.decode('utf-8')

# 3. html 파싱
html = BeautifulSoup(source, 'html.parser')

# 4. 링크된 뉴스 제목이 있는 태그 요소 추출 : 속성 추출
atags = html.select('strong[class=tit_txt]')
# print(atags)

print('제목 개수:',len(atags))

# 제목있는 자료 수집
crawling_data = []

cnt = 0
for atag in atags:
    cnt += 1
    # 태그의 내용을 추출해서 문자열로 전환
    atagsStr = str(atag.string)
    """ xxx.strip()
        문단 끝 공백, tab, \n\r(줄바꿈) 제거    
    """
    crawling_data.append(atagsStr.strip())

# 수집한 자료 확인
print('수집한 자료 확인')
# print(crawling_data)
for data in crawling_data:
    print(data)
    print('-'*50)

# -----------------------------------------------------------------------------#
# pickle save/load : 이진파일 처리
#  => 현재 자료의 객체를 그대로 유지하기 위해서
# object -> file(binary) -> load(object)

import pickle
# save
file = open('data.pickle', mode = 'wb') # 이진 파일 형식 저장
pickle.dump(crawling_data,file)
print('pickle save...')

# load
file = open('data.pickle', mode = 'rb')
crawling_data2 = pickle.load(file)
print('pickle load...')

for data in crawling_data2:
    print(data)
    print('-'*50)
