# 이미지들을 Numpy 형식으로 변환하기
import numpy as np
from PIL import Image
import glob, os, random 

outfile = "./myproject/photos.npz" #저장할 파일 이름

max_photo = 200 # 사용할 장 수
photo_size = 32 # 이미지 크기

x = []          # 이미지 데이터
y = []          # 레이블 데이터

# 1. path 내부의 이미지 읽어 들이기
def glob_files(path, label):
    files = glob.glob(path+ "/*.jpg") # glob 폴더안의 파일들의 목록을 불러옴
    random.shuffle(files)
    # 파일 처리하기
    num = 0
    for f in files:
        if num >= max_photo:break
        num += 1
        #이미지 파일 읽어 들이기
        img = Image.open(f)
        img = img.convert("RGB")                     # 색공간 변환하기
        img = img.resize((photo_size, photo_size))   # 크기 변경하기
        img = np.asarray(img)
        
        x.append(img)
        y.append(label)
        
def main():
    # 2. 디렉터리 읽어 들이기
    glob_files("./myproject/Hamburger", 0)
    glob_files("./myproject/Salad", 1)
    glob_files("./myproject/Gimbap", 2)    
    
    # 파일로 저장하기
    np.savez(outfile, x=x, y=y)
    print(outfile, len(x), "장 저장했습니다.")

if __name__ == '__main__':
    main()

    

