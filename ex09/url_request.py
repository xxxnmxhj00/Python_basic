# 원격 서버에서 자료 수집하기

# request, BeautifulSoup 모듈을 import
import urllib.request # 원격 서버 파일 요청, Python에서 URL을 통해 데이터를 요청하고 가져오는 작업을 수행하기 위해 사용하는 표준 라이브러리
from bs4 import BeautifulSoup # html 파싱

# 요청할 url
url = 'http://www.naver.com/index.html'

# 원격 서버 파일 요청
resp = urllib.request.urlopen(url)
data = resp.read() # 서버로 부터 응답받은 객체를 파일 형식으로 읽기

# 문자 디코딩
src = data.decode('utf-8') # 디코딩,문자에 대한걸 디코딩 먼저 해줌
print('source')
print(src)
print('-'*30)

# # html 파싱
html = BeautifulSoup(src, 'html.parser')
print('html 파싱')
print(html)

print('-'*50)
# index.html 태그
a = html.find('a') # a 태그(하이퍼링크)를 찾고, 그 태그의 내용을 출력
print('a 태그 :', a)
print('a 태그 내용:',a.string)


