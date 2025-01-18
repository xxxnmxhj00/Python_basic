# # 문자열 검사 예문
# from re import match, sub 

# # 1. 패턴과 일치된 경우
# jumin = '121112-1234567'
# result = match('[0-9]{6}-[1-4][0-9]{6}',jumin)
# print(result)

# if result:
#     print('주민번호 일치')
# else:
#     print('잘못된 주민번호')

# jumin2 = '121112-5234567'
# result2 = match('[0-9]{6}-[1-4][0-9]{6}',jumin2)
# print(result2)

# if result2:
#     print('주민번호 일치')
# else:
#     print('잘못된 주민번호')

    
# st3 = 'test^홍길동 abc 대한*민국 123$tbc'
# # 특수문자 제거 => 치환가능 =>"기존문자", "바꿀문자"
# text1 = sub('[\^*$]+', '강', st3)
# print(text1)

# text2 = sub('[0-9]','',st3)
# print(text2)

from re import split, match, compile
# 더미 텍스트 자료

multi_line = """\
http://www.naver.com
http://www.daum.net
www.honhkildong.com"""\

print(multi_line)

# 구분자를 이용 하여 문자열 분리 

web_site = split("\n", multi_line)
print(web_site)

# 패턴 객체 만들기 

pat = compile("http://")

sel_site = [ site for site in web_site if match(pat,site)]
print(sel_site)