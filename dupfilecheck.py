import os
import hashlib
from tkinter import *
from tkinter import filedialog
window=Tk()
name=[]
md=[]
pht=[".jpg",".gif",".png",".bmp",".webp",".jfif",".jpeg"]
k = open("log.txt", "w")#log.txt 생성
sergdir=filedialog.askdirectory(parent=window,title="검색하려는 디렉토리의 이름은?")#input("검색하려는 디렉토리의 이름은?:")
count=0
label1=Label(window,text="")
label2=Label(window,text="")
def fin():
    label2.config(text="분석완료")
    window.update()
    label1.after(100,label1.destroy())
    label2.after(100,label2.destroy())
    window.update()
for (path, dir, files) in os.walk(sergdir):#지정한 파일 경로 탐색
    for fn in files:#파일들을 순차적으로 탐색
        pt=os.path.join(path, fn)#파일 경로
        if(os.path.isdir(pt)):#pt가 디렉토리로 판명이 되면 오류가 남. 따라서 예외 처리를 해주어야 함.
            continue
        label1=Label(window,text=pt+"분석중")#print(pt+"분석중....")
        with open(pt, "rb") as f:#md5값을 만드는 부분. md5가 같으면 같은 파일이라고 볼 수 있음.
            data=hashlib.md5()
            while test := f.read(8192):
                data.update(test)
        md5=data.hexdigest()
        f.close()
        label2=Label(window,text="...")#print(md5)
        label1.pack()
        label2.pack()
        if md.count(md5)==0:#일치하는 md5 값이 없다면 해당 값과 이름을 기록
            md.append(md5)
            name.append(pt)
            fin()
            continue
        photocheck=False
        for i in pht:
            if i in pt:
                photocheck=True
                break
        if(photocheck):
            k.write(name[md.index(md5)]+"가"+pt+"와 같은 파일인거 같아 삭제하였습니다. md5="+md5+"\n")#파일이 겹치면 해당 사실을 log.txt에 기록
            label1.config(text=name[md.index(md5)]+"가"+pt+"와 같은 파일 인것 같아 삭제하였습니다.")
            window.update()
            os.remove(name[md.index(md5)])
            name[md.index(md5)]=pt
            fin()    
k.close()#log.txt 닫음
label1=Label(text="분석이 완료되었습니다.log.txt를 참고하여 어떤 파일들이 삭제되었는지 내용을 확인하실 수 있습니다.")
label1.pack()
window.mainloop()