# 이진 파일( 이미지, 동영상, 음원, ....)

import os
from glob import glob

print("현재 경로:", os.getcwd())

# 1. image 파일 경로

img_path = 'img\\' # 윈도우는 \ 하나만 쓰면 에러걸림, 그래서 2번
img_path_copy = os.getcwd() + '/ex06/imgcopy/' # 이게 타겟이라고 먼저 생성

if os.path.exists(img_path):
    print('원본 이미지 폴더가 존재합니다.')

    # image 파일 저장, 이동
    images = []
    # print(img_path_copy)
    # print(os.path.exists(img_path_copy), not(os.path.exists(img_path_copy)) )

    # 이동할 이미지 폴더가 없으면
    if not (os.path.exists(img_path_copy)): 
        os.mkdir(img_path_copy)
    else: # 이동할 이미지 폴더가 있으면
        # image 검색
        for pic_path in glob(img_path + '*.jpg'): # 'img\*.gif' 패턴
            print('원본 이미지 경로:', pic_path)
            # for pic_path in glob(img_path + 'apple0[3-4].gif')
            # for pic_path in glob(img_path + '연예인0[1-2]jpg'): # 'img\*.gif' 패턴

            print(pic_path)

            # 튜플(경로, 파일이름) 형식으로 분리 , 파일이름만 필요 하기 때문
            img_path_slice = os.path.split(pic_path)
            # print(img_path_slice, img_path_slice[1])

            # 파일 이름만 추출
            # images = ['apple01.gif'] # 이 부분에서 아직 images 는 만들어지지 않음
            images.append(img_path_slice[1])

            try: # 파일 단위로 계속 반복 하는 것이다

                # 이진 파일 읽기
                rfile = open(file=pic_path, mode= 'rb') # rb 바이너리 데이터
                output = rfile.read() # read()는 파일 전체를 읽어서 output 객체 생성

                # 이진 파일 쓰기(생성) : file = 이동할 이미지 경로 + 이미지 이름
                # 'ex06/imgcopy
                wfile = open(file=img_path_copy + img_path_slice[1], mode = 'wb') # 복사 경로와 파일 이름
                # img_path_copy 여기다가 파일을 계속 넣어주는 느낌으로 가는것
                # 경로에 저 파일 이름으로 이진파일 쓰기 하겠다
        
                wfile.write(output) # 파일을 생성한다, 이 코드가 저장을 하는 기능
                # 위의 output 에서 읽어와서 밑의 output에서 쓰기를 하는 것


                print('이미지 파일 복사 완료:' +img_path_copy + img_path_slice[1])

            except Exception as e:
                print('Error:', e)
            
            finally:
                rfile.close()
                wfile.close()

    
