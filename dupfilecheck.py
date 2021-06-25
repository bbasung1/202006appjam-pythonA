import os
import hashlib
from tkinter import *
from tkinter import filedialog
window=Tk()
window.withdraw()
name=[]
md=[]
k = open("log.txt", "w")#log.txt 생성
sergdir=filedialog.askdirectory(parent=window,title="검사하고 싶은 디렉토리는?")#input("검색하려는 디렉토리의 이름은?:")
count=0
for (path, dir, files) in os.walk(sergdir):#지정한 파일 경로 탐색
    for fn in files:#파일들을 순차적으로 탐색
        pt=os.path.join(path, fn)#파일 경로
        if(os.path.isdir(pt)):#pt가 디렉토리로 판명이 되면 오류가 남. 따라서 예외 처리를 해주어야 함.
            continue
        print(pt+"분석중....")
        with open(pt, "rb") as f:#md5값을 만드는 부분. md5가 같으면 같은 파일이라고 볼 수 있음.
            data=hashlib.md5()
            while test := f.read(8192):
                data.update(test)
        md5=data.hexdigest()
        f.close()
        print(md5)
        if md.count(md5)==0:#일치하는 md5 값이 없다면 해당 값과 이름을 기록
            md.append(md5)
            name.append(pt)
            print("분석 완료")
            continue
        k.write(pt+"와"+name[md.index(md5)]+"가 같은 파일인거 같습니다. md5="+md5+"\n")#파일이 겹치면 해당 사실을 log.txt에 기록
        os.remove(pt)#겹치는 파일 삭제
        print("분석 완료")
k.close()#log.txt 닫음