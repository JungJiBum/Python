# https://076923.github.io/posts/Python-tkinter-2/
from ast import main
from enum import auto
from itertools import count
from tkinter import *

def visible_window(text,n="1"):
    window = Tk()
    window.title("Hello tkinter") #상단 타이틀 네임
    window.geometry("1000x700+250+50")  # 너비 *높이 + x좌표 +y좌표
    window.resizable(False, False)  # 상화 좌우 크기조절 여부

    # print(type(n)) # str
    firstLabel = Label(window, text=text+n)
    n = int(n)+1
    secondLabel = Label(window, text=text+str(n))
    n = int(n)+1
    thirdLabel = Label(window, text=text+str(n))
    firstLabel.pack()
    secondLabel.pack()
    thirdLabel.pack()

    # label1 = Label(window, text="grid1")
    # label2 = Label(window, text="grid2")
    # label3 = Label(window, text="grid3")
    # firstLabel.grid(row=0,column=0)
    # secondLabel.grid(row=1,column=1)
    # thirdLabel.grid(row=2,column=2)

    def clickevent():
        text="Click!"
        print("click!")

    btn1 = Button(window, text='click1',padx=50,command=clickevent)
    btn1.pack()

    btn2 = Button(window, text='click2')
    btn2.pack()

    txt = Entry(window)
    txt.pack()

    window.mainloop()


text = "라벨 테스트 값"
visible_window(text)


'''
https://goodthings4me.tistory.com/552
https://wonhwa.tistory.com/42

'''