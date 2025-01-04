dic = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고,","설탕","치자황색소"], # 얘는 출력하면 리스트 구조로 나옴
    "origin" : "필리핀"
}

# for key in dic.keys(): 
#     print(key, dic.get(key)[0]) # 리스트 구조 나오는건 바로 못씀 # dic.get(key)**는 딕셔너리에서 특정 키의 값을 가져오는 메서드

for key in dic.keys():
    print(key, dic.get(key))

    if type(dic.get(key)) == type([]): # 자료형 타입이 list면 처리
        print("------")

        for i in dic.get(key):
            print(i, end = " ")
    print("\n-----------------")

    