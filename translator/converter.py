import tkinter

window = tkinter.Tk()

window.title("Language Translator")
window.geometry("640x400+100+100")
window.resizable(False, False)

text = "안녕하세요"
label = tkinter.Label(window, text="원문을 입력하세요.")
# label = tkinter.Label(window, textvariable="test")
label.pack()
window.mainloop()
