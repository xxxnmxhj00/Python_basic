# # 자료 구조 : 데이터(객체)가 메모리에 배정될 때 기억공간에 적재되는 구조
# # 순서 자료 구조 : 리스트. 스트링(문자열), 튜플
# # 비순서 자료 구조 : 딕셔너리


# list1 = [100,200,300,400,500]
# print(list1, list1[0],list1[1]) 
# # print(list1[0:3],list1[:3])
# # print(list1[-3:-5]) # 슬라이싱은 항상 왼쪽에서 오른쪽으로
# # print(list1[-3:]) # 아무것도 안쓰면 뒤에거 까지 다 나옴

# # 리스트에 데이터 추가 : append()
# list1.append(1)
# print(list1)

# list1.append(["홍길동", "홍길순"])
# print(list1)
# print(list1[5],list1[6], list1[6][0],list1[6][1])

# # 데이터가 있는 인덱스 번호 추출, 그 데이터가 몇번째에 위치해 있냐
# print(list1.index(100), list1.index(500)) 

# # 리스트 : appned(), insert(), remove()
# num = ['one', 'two', 'three', 'four']
# print(num, len(num))

# # 추가 

# num.append('five')
# print(num, len(num))

# # 삭제
# num.remove('five') # 가장 처음 값만 제외하는거, 5 5 2개 있으면 처음만 지운다
# print(num, len(num))

# # 수정
# num[3] = '4'
# print(num, len(num))

# num.insert(0, 'zero') # 특정 위치에 꽂아넣고자 할 때
# print(num, len(num))

# # pop() 
# num.pop (0) # 데이터를 가지고 지우는거, 인덱스를 기준으로 제외 
# print(num, len(num))

# # clear() 몽땅 삭제, 리스트 데이터 모두 제거
# num.clear()
# print(num, len(num))

lst = [1,2,3,4,5]
print(lst, type(lst))

# for i in lst : # 1을 받아오고 2를 받아오고
#     print(lst[:i])

print( 5 in lst) # 값을 포함여부 판별
print( 5 not in lst) # 값을 포함하고 있지 않으면 True

# 리스트 내포( list 안에 for 와 if 문 )

x = [2,4,1,5,7]
lst = [i**2 for i in x] # 제곱하고 리스트 구조로 한번에 만들어 주는 것
print(x, lst)

# temp = []
# for i in x:
#     temp.append(i**2)
#     print(temp)
#     print("----")

# print(temp)

# 조건에 부합한 데이터만 처리
lst2 = [ i*2 for i in x if i%2 == 0] # x에서 i로 넣고 조건문 가고 짝수이면은 저장
print(lst2)


