
# 단어 빈도수 구하기 
charset = ['abc', 'code', 'band','band', 'abc']

wc = {} # set, dict
for key in charset: # 리스트 객체
   print(key, wc.get(key), wc.get(key,0)) # 값이 없으니가 none이 나올거임
   wc[key] = wc.get(key,0)+1 # 키를 뽑아내서 거기다 0을 값으로 주겠다
#     # wc['abc'] = wc.get('abc,0)++1
#     print(wc)

# print('-' * 20)

# print(wc) 


# test = {}
# print(test.get('name')) # 키가 없으니까 none 이 나올거임

# # test['name'] = 1  # 없는 곳에다가 넣으니까 저걸 test 안에 만들어버릴거임
# test['name'] = test.get('name',0)
# print(test)

# test['name'] = test.get('name',0) +1
# print(test)

# test['name'] = test.get('name',0) +1
# print(test)