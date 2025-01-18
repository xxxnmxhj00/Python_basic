# 산술 연산자 : +, -, *, 나누기 : /, 나머지 : %, 몫 : //, **(누승)

n1 = 100
n2 = 20
add = n1 + n2
sub = n1 - n2
mul = n1 * n2

div = n1 / n2
div2 = n1 % n2
div3 = n1// n2

print('add:', add, 'sub:', sub, 'mul:', mul)
print('div:', div, 'div2:', div2, 'div3:', div3)

print(3**2, 3*2, '홍길동'*2)
print("-"*30)

# 관계연산자
print(5>2, 5>=2, 5<2, 5<=2, 5==2, 5!=2)

# 논리연산자 

print('- 논리 연산(and,or,not)')
print(5>2 and 3>2 and 4>2) # 모두 True => True
print(5<2 or 5<3 or 5<4) # 모두 False => False , 한개라도 참이되면 무조건 참
print(5>2, not(5>2))

