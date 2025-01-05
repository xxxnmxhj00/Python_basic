# 자료 구조 복제 : 얕은 복사, 깊은 복사
print("-- 객체 주소 복사")
print("1. 얀츤 복사: 주소 복사")

name = ['홍길동','이순신','강감찬']
print(f"name={name}")


# name2에 name이 담고있는 객체 주소를 저장
name2 = name # 1000번지 할당 받은게 name 인데 이 주소를 name2에 복사를 한것 ,객체들은 데이터가 아니라 다 주소가 들어가는 것
print(f"name2={name2}")

print(f"name 주소: {id(name)},name2 주소:{id(name2)}")

# 복사본을 수정
name2[0] = "길순이" # name2 에 내용을 바궛지만 name 1도 바꿨다. 왜냐하면 같은 주소를 공유하기 때문이다.
print(f"name={name}")
print(f"name2={name2}")

print("-"*20)

# 깊은 복사
import copy # 모듈 이름 
print("2. 깊은 복사")
name3 = copy.deepcopy(name) # 주소를 복사하는게 아닌 데이터를 복사하는 것
print(f"name={name}, name3={name3}")
print(f"name 주소 ={id(name)}, name3 주소 ={id(name3)}") # 이 데이터는 따로 주소를 확보해서 받아온 것 

name3[0] = "동순이김"
print(f"name={name}, name3={name3}")