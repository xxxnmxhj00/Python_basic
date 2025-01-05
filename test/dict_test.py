# # 딕셔너리 -  dict()
# # (키, 쌍) 구성된 요소

# # 딕셔너리 생성
# # 1. 초기화
# name_price = {"apple" : 3000, "grap":5000}
# print(name_price)

# # 2. 생성자
# name_price2 = dict(apple=100, grape=500)
# print(name_price2)

# # 3. 텅빈 dict 
# d1 = {} # 자료형 타입만 선언

# # 값 호출 => 키를 통해 호출 => 객체['키']
# # print(d1["apple"]) # 키가 없으면 key 에러
# print(d1.get("apple")) # 키가 없으면 None
# print(d1.get("apple",10000)) # 키가 없으면 0으로 설정

# # 없는 키에 값을 설정하면 추가 기능이 됨
# d1["apple"] = 30
# print(d1, "apple" in d1, "grape" in d1)

# if "apple" in d1 :
#     print("apple 키가 존재합니다")
#     print(d1['apple'])

# else:
#     print("없는 키입니다")

# # dict 관련 함수
# keys(), values(), items()
d2 = {"name" : "홍길동", "age" : 10, "address" : "부산"}
print(d2)

for k in d2.keys():
    print("key: {}, \t value : {}".format(k, d2[k]))

for v in d2.values():
    print(f"value={v}")

for i in d2.items(): # key, value 튜플 구조 반환 
    print(f"items={i}, type={type(i)}")

    print("-----")
    for item in i:
        print(item)

for k,v in d2.items(): # key, value 원소로 호출
    print(f"key={k}, value={v}")
