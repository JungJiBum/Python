from tkinter import *
from tkinter import ttk

# 사용자 id와 password를 비교하는 함수
def check_data():
    if user_id.get() == "root" and password.get() == "root":
        print("Logged In Successfully")
    else:
        print("Check your Username/Password")


# create tkinter object
window = Tk()



user_id , password = StringVar(), StringVar()

# id와 password, 그리고 확인 버튼의 UI를 만드는 부분
ttk.Label(window, text = "Username : ").grid(row = 0, column = 0, padx = 10, pady = 10)
ttk.Label(window, text = "Password : ").grid(row = 1, column = 0, padx = 10, pady = 10)
ttk.Entry(window, textvariable = user_id).grid(row = 0, column = 1, padx = 10, pady = 10)
ttk.Entry(window, textvariable = password).grid(row = 1, column = 1, padx = 10, pady = 10)
ttk.Button(window, text = "Login", command = check_data).grid(row = 2, column = 1, padx = 10, pady = 10)

window.mainloop()


