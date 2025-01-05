# # 자주 쓰이는 표현식
# names = ["홍길동", "동순이", "길동이"]
# # n1 = "/".join(names)
# n1 = "".join(names) # 아무것도 없이 한 덩어리가 만들어짐
# print(n1, type(n1), len(n1)) # class str

# num1 = int( input("숫자입력: ") ) # int를 안감싸면 string 이됨 , input 은 무조건 문자형
# print(f"입력받은 숫자는 {num1}") 
# isEvenOrOdd = "짝수" if num1 % 2 == 0 else "홀수"
# print(f"입력받은 숫자는 {num1}는 {isEvenOrOdd}")

# -----------------------------------------------#
# 리스트 컴프리헨션 : list 안에 for, if문 
# 리스트 컴프리헨션(List Comprehension)은 파이썬에서 리스트를 생성하고 조작하는 간결하고 효율적인 방법
# -----------------------------------------------#

# 1.
s1 = []
for i in range(5):
    print(str(i), type(str(i)))
    s1.append(str(i)) # 숫자 -> 문자 -> list 추가
print(s1)

# 0-> '0' 전환해서 list 에 저장 
str1 = [str(i) for i in range(5)] # 숫자를 받아서 바로 list 에 저장, 위의 3줄을 한 줄에 끝냄
print(str1)
print("-" * 60)

#2. 비교
s2 =[]
for i in range(1, 10+1):
    if i%2 == 0:
        # print(str(i), end ="\t")
        s2.append(str(i))
print(s2)


n2 = [str(i) for i in range(1,10+1) if i%2 ==0]
print(n2)

# 3. 
# for i in range(1,3): # i = 1,2
#     for j in range(1,3): # j = 1,2
#         print(i,j)

# for i in range[1,2,3]: # i = 1,2,3
#     for j in range[10,20,30]: # j = 10,20,30
#         print(i,j)

a = []
for i in ["slow","fast"]: # i = "slow", "fast"
    for j in ["dong","cat"]: # j = "dong", "cat"
        a.append("{} {}".format(i,j)) 
        print(i,j)
print(a)

n3 = [ "{} {}".format(i,j) for i in ["slow","fast"] for j in ["dong","cat"]]
print(n3)







