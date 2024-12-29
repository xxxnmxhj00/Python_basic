# 제어문 : 프로그램 흐름을 제어
# if, while, for 유사 

# 단순 if, if else , elif문
# num = 10
# if num >= 5:
#     print('num=', num)
#     print('조건이 참인 경우 처리되는 문장')

# print('다음문장') 

# num = 10
# if num > 10:
#     print('num=', num) 
#     print('조건이 참인 경우 처리되는 문장') # 들여쓰기가 없어져버리면 밑의 print만 출력

# print('다음문장') 

# num1 = input("정수 : ")
# num1 = int(num1) # 문자형 -> 정수형

# 1. 단순 if
# if num1 % 2 == 0 :
#     print(num1,"짝수")

# if num1 % 2 == 1:
# #      print(num1,"짝수")



# # num1 = input("정수 : ")
# # num1 = int(num1) # 문자형 -> 정수형

# # # 2. if else 
# # if num1 % 2 == 0: # pass 는 아직 문장 완성은 아닌데 형식만 갖추겠다, 처리하고자 하는 문장 뒤에는 무조건 :
# #     print(num1, "짝수")
# # else:
# #     print(num1, "홀수")

# # # 3. elif문(else if의 약자)
# # score = int(input('점수입력: ')) # 점수 입력
# # grade = '' # 점수에 따른 등급

# # # if score >= 85 and score <= 100:
# # if 85<= score <=100:
# #     grade = '우수'
    
# # elif score >= 70: # 85미만 70이상
# #     grade= '보통'

# # # else:
# # #     grade = '저조'


# # print(grade) # 70미만

# # 점수 입력 
# # 90이상 : A, 80이상 : B, 70 이상 : c, 60 이상 : D, 60미만 F

# score = int(input('점수입력: ')) # 점수 입력
# grade = '' # 점수에 따른 등급

# if 90 <= score <= 100:
#         grade = 'A'

# elif score >= 80: # 80이상
#     grade = "B"

# elif score >=70: # 80미만 70 이상  
#     grade = "c"

# elif score >= 60: # 70미만 60이상 
#     grade = "D"

# else:
#     grade = 'F'

# print("당신의 점수는 {}이고 학점은 {} 입니다.".format(score, grade))
# print(f"당신의 점수는 {score}이고 학점은 {grade}")

# 삼항 연산자, 변수 = 참인경우 처리할 내용 if 조건식 else 거짓인경우 처리할 내용

num = 9
result = 0

#if num >=5:
#     result = num*2
#else:
#     result = num+2

retult = num *2 if num>=5 else num+2 # value_if_true if condition else value_if_false
# 간단한 식 한 개만 있을 때 적합하다


print(f"result={result}")

