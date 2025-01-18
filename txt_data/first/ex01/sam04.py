# 대입 연산자 +, =, *, /, ,,, => +=, -=, /=, *=,...
i = tot = 10 # 숫자 10을 먼저 tot에 tot을 i 에
print(i, tot)

i += 1 # i = i + 1
print(i)

i += 1 # 12
print(i)

i += 1 # 13
print(i)

i *=3
print(i)

i /= 2 # i = i / 2
print(i)

v1, v2 = 100,200
print(v1, v2)

v1, v2 = v2, v1 # 스왑
print(v1, v2)

# 변수 : 단일 기억장소
# 리스트 구조 : 여러개의 데이터를 순차적으로 보관
list1 = [1,2,3,4,5]
print(list1, list1[0], list1[1], list1[2])

v1, *v2 = list1
print(v1, v2) # 처음꺼는 하나 들어가고 나머지는 리스트 형태로 들어간다

*v1, v2 = list1
print(v1, v2)
