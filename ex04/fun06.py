# # 재귀함수 (Recursive function) : 함수 내부에서 자신의 함수를 반복으로 호출
# # 재귀함수는 반드시 종료하는 조건을 만들어야 한다.
# def counter(n):
#     if n == 0:
#         print(n, end = " ")
#         return 0
#     else :
#         print(n, end = " ")
#         counter(n-1) # 0 -> 

# counter(3)

# # 5! => 5*4*3*2*1
# def fac(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fac(n-1) # 5*fac(4) => 4*fac(3) => 3*fac(2) => 2*fac(1)
    
# print(fac(5))

# 손 p 185

def sum_one_to_num(num):
    if num == 1:
        return 1
    else: 
        return num + sum_one_to_num(num-1)
print(sum_one_to_num(2))
print(sum_one_to_num(3))
print(sum_one_to_num(4))
print(sum_one_to_num(5))

def mul(*args):
    result = 1
    for i in args:
        result *=i
    return result
print(mul(3,4))
print(mul(5))
print(mul(2,2,2,2))