# 단순 if 

# 단순 if :
# if 조건식:
#     실행코드1
#     실행코드2
#     ........
# if 문 벗어난 다음 문장

# num = 10
# if num >=10:
#     num+=100
#     print(num)
#     print("조건이 참이면 수행중")

# print(" if문 다음 문장")

# if sum([1,2,3]) > 10:
#     print([1,2,3])
#     print("전체 합이 10보다 크다") # 거짓이면 19, 20 라인을 수행하지 않는다
# print("out of if")

# if 3: # 0을 제외한 모든 숫자는 True로 판별
#     print("3은 참")

# if - 3: # 0을 제외한 모든 숫자는 True로 판별
#     print("3은 참")

# if 0:
#     print("0은 참")

# if "홍길동" : # 문자 데이터가 들어있으면 참
#     print("문자 값이 있으면 참") 
# if "":
#     print("텅빈 문자")
# if " ": # 공백은 문자로 침, 그래서 데이터가 들어가있으면참
#     print("공백 문자") 

if [1,2,3]:
    print("리스트에 값이 있음")
if []:
    print("리스트에 값이 없음")

# 중첩 if 문

# num1 = 4
# num2 = 6
# if 12 % num1 == 0:
#     if 16 % num1 == 0:
#         print("num1 = {}".format(num1))

# score = 80
# if score > 70 :
#     print("score 점수가 70 이상 입니다.")

#     if score % 2 == 1: # 70이고 홀수인가 판별 # 조건에 조건을 물고 간다 
#         print("홀수")

# p.206
# 키보드로 값을 입력 = > 기본형이 문자형 => 숫자형 변환을 해줘야함 (int(), float())
# num = int(input("숫자를 입력하세요. ") )
# if num % 3 == 0 and num % 6 == 0 :
#     print (f"{num}은 3의 배수이면 6의 배수입니다.")

# if num % 3 == 0 or num % 6 == 0 :
#     print (f"{num}은 3의 배수이거나 6의 배수입니다.")


# # else 문 : if 참 else 거짓 
# score = int ( input ("점수를 입력하세요 : "))
# # if score >= 60:
# #     print("pass")
# # else :
# #     print("fail")

# # 위에걸 한줄로 쓰는법

# # 삼항 연산자
# print("pass") if score >= 60 else print("fail")

# num2 = -1
# if num2 > 0 :
#     print("양수")
# elif num2 == 0:
#     print("0")
# elif num2 < 0 :
#     print("음수")
# else :
#     print("기타")

# # p213
# score = int( input ("점수를 입력하세요 :"))
# if score >= 90 :
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else :
#     print("F")

