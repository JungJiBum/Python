import re
t1 = ["img12.png", "img10.png", "img02.png",
      "img1.png", "IMG01.GIF", "img2.JPG"]
t2 = ["F-5 Freedom Fighter", "B-50 Superfortress",
      "A-10 Thunderbolt II", "F-14 Tomcat"]


def sol(files):
    for i,file in enumerate(files):
        file = file.lower()
        print(i,file)
        


sol(t1)
print("-"*10)
sol(t2)
