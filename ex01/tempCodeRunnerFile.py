# 문자열 색인 => 리스트 구조형식
s = "PYTHON"
print(s)
print(s[0], s[1], s[2], s[3], s[4], s[5])

# 잘라서 범위를 줄 수 있는 것이 슬라이싱 (slicing)
# 문자열 [인덱스 번호], 문자열 [시작 : 끝 번호: 증감값]
print('문자열 길이:', len(s))
print(s[0:4]) # start, end - 1
print(s[:4])
print(s[:]) # 전체 다 나오게 함
print(s[::2])

# 반대방향 , 우측 기준
print(s[-1],s[-2])
