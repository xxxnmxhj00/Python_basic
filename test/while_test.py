# # while문
# while 조건식:
#     반복 수행구간 (참인동안 수행)

# while True:
#     num = int( input ("숫자:"))
#     if num == 0 : 
#         break # while 문을 완전히 빠져나옴
#     print("입력받은 숫자는 ", num)

# while True:
#     num = int( input ("숫자:"))
#     if num == 0 : 
#         continue # 다음 제어문으로 넘어감(조건식 판별) # 0 넣으면 밑에 print 안하고 다시 위로 가버림
#     print("입력받은 숫자는 ", num)

# # 곱하기
# for i in range(2,9+1): # 바깥쪽 for 문 (outer for)
#     print(f"---- {i} ----단")

#     for j in range(1,9+1): # 안쪽 for 문 (inner for)
#         print(f"{i} * {j} = {i*j}")

#  문장과 단어추출 하기
# # str ="""
# 나는 홍길동 입니다.
# 주소는 서울시 입니다.
# 나이는 15세입니다. => 빈 줄이 생김
# """

str ="""\
나는 홍길동 입니다.
주소는 서울시 입니다.
나이는 15세입니다.\
"""

print(str)
print(str.split(sep="\n"))

sents = [] # 문장을 저장할 리스트 객체
words = [] # 단어를 저장할 리스트 객체
# 1. 문단 => 문장
for sen in str.split(sep = "\n"): # ['나는 홍길동 입니다.', '주소는 서울시 입니다.', '나이는 15세입니다.']
    sents.append(sen) # 문장을 리스트에 추가

    # 문장 - > 단어
    for word in sen.split (): # [나는 홍길동 입니다] 를 가지고 와서 다시 자름
        words.append(word)

print("문장 :",sents)
print("문장 수:", len(sents))

print("단어 :",words)
print("단어 :",len(words))