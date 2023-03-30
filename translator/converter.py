import tkinter as tk

window = tk.Tk()

window.title("Language Translator")
window.geometry("900x850+100+100")
window.resizable(False, False)

# Label 클래스 생성 및 window 상단에 고정
word_label = tk.Label(window, text="번역할 내용을 입력해주세요",font=("",20,"bold"))
translate_label = tk.Label(window,text="번역된 내용 입니다.",font=("",20,"bold"))

# Text클래스 생성
word_text = tk.Text(master=window, wrap="word",height=15,font=("",12,"")) # -> font=("Times",20,"italic") 폰트속성 설정가능 글꼴,크기,기타속성 공란도 가능
translate_text = tk.Text(master=window, wrap="word",height=15,font=("",12,""))

# btn 클릭시 동작 정의
def click_btn() : word_text.insert(1.0,"안녕하세요\n") 
# -> insert(글자를 입력할 줄 수.글자 입력할 문자 위치, "입력값")
# -> end 인자를 입력할 경우, word_text에 입력된 글자의 줄 수에 상관없이 가장 마지막 줄 첫 번째 위치에 문자를 추가하게 됨
def click_btn2() : word_text.delete(1.9, 3.1)
# -> delete(삭제를 시작할 문자의 행.위치 , 삭제를 끝낼 문자의 행.위치)
def click_btn3() : print(word_text.get(1.1,"end"))
# -> 인자가 필요없는 다른 위젯의 get() 메서드와 달리, Text위젯의 get()메서드는 두가지 인자를 필요로 한다.
# -> delete()와 동일한 인자다. get(문자열을 반환 받을 시작 문자의 행.위치 , 끝 문자의 행.위치)
def click_btn4() : 
    text = word_text.get(1.0,"end")
    translate_text.delete(1.0,"end")
    translate_text.insert("end",text)


# btn 클래스 생성
btn_insert = tk.Button(master=window, text="Insert", command=click_btn)
btn_delete = tk.Button(master=window, text="Delete", command=click_btn2)
btn_get = tk.Button(master=window, text="get",command=click_btn3)
btn_test = tk.Button(master=window,text="번역하기",command=click_btn4)

# 생성한 클래스 위젯들을 pack() 메서드로 배치
word_label.pack(side="top")
word_text.pack(side="top",fill="x")
translate_label.pack()
translate_text.pack(fill="x")
btn_test.pack()
# btn_insert.pack()
# btn_delete.pack()
# btn_get.pack()

# 창 유지하기 위한 코드
window.mainloop()