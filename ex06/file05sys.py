
import os.path # 윈도우 파일 경로 조작하는 모듈

# 현재 경로 확인
path = os.getcwd()
print('현재 위치:',path)

# # 경로 변경
# os.chdir('ex06/data')
# print('변경된 위치:',os.getcwd())

# 절대 경로 , 실제 쓰고 있는 걸 기준
abspath = os.path.abspath('ex06/data/appendfile.txt') # python01 을 기준으로 베이스로 안에서 움직임
print(abspath)

# 파일 유무체크 
isfile = os.path.isfile('ex06/data/appendfile.txt')
print('파일 유무체크:',isfile)
print('파일 유무체크:',os.path.isfile('test02.txt'))

# 폴더 유무 체크
print(os.path.isdir('ex06'))
path_split = os.path.split('ex06/data/appendfile.txt')
print('경로와 파일 분리:', path_split)
print('경로와 파일 분리:', path_split, path_split[-1])

file_size = os.path.getsize('ex06/data/appendfile.txt')
print('파일 크기:', file_size/1024, 'KB')
