import tkinter as tk
import tkinter as ttk

window = tk.Tk()

window.title("Language Translator")
window.geometry("640x400+100+100")
window.resizable(False, False)


text_var = tk.StringVar()
text_var.set("test")
entry = ttk.Entry(window, textvariable=text_var)

entry.pack()

window.mainloop()
