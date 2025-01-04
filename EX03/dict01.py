# 딕트(dict) : 키 중복 불가, 값은 중복 가능, 키를 통해 값을 호출
# list = [1,2,3] - 리스트, tuple = (12.3.3), set = {1,2,3}
# 딕트 = {'a' : '1',...}

# 1. 생성자를 통해 값 설정 : 키 = 값,...
dic = dict(key1 = 100, key2 = 200, key3 = 300) # 생성자를 통해서 넣을때는 key => 키, 100 => 값 
print(dic, type(dict))

# 2. 초기값 설정 : 키 :값,... 
person = {'name' : '홍길동', 'age' : 35, 'addr' : '부산시'}
print(person, type(person))

# 3. key로 value를 호출(참조)
print(person['name'], person.get('age'))

# 4. 추가/수정
person['name'] = '동순이' # 수정
person['age']=10
person['gender'] = '여자' # 없는걸 쓰면 추가가 됨
print(person)

# 5. 삭제
del person['gender']
print(person)

# 6. 유무 체크
print('age' in person, 'gender' in person)

# 7. 반복
for key in person.keys(): # 키만 추출 
    print(key, person.get(key)) # *딕셔너리(dictionary)**에서 값을 가져오기 위해 사용되는 메서드, person.get()
for value in person.values(): # 값만 추출
    print(value)

for item in person.items() : # 키와 값 추출 
    print(item, item[0], item[1]) # 튜플 형식으로 키와 값 구성

# print(person.keys(), person.values())
# print(type(person.keys()), type(person.values()))

# dict 구조 : 값 호출 => dict객체 ['키이름'], 
# dict 객체.get('키이름'), dict 객체.get('키이름', 키가 없을 경우 설정할 값)

print('-' * 30)
print(person)
print(person['name'], person.get('age'),person.get('gender', '없다고')) 
# 값을 못찾으면 텅 빈 상태인 none 을 출력, gender라는 값이 없으면 0 이 나옴

