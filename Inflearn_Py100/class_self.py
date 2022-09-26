#[1] 클래스 생성
#--------------------------
'''
self 란?
--> self가 없으면 누군가 외부에서 호출은 하고 있는데 누가 호출했는지 알수가없다.

'''
class Pet:
    #bow
    def bark_dog(self):
        print("bow bow")

    def bark_cat(self):
        print("meow meow~")

    def bark_hamster(self):
        print("PPI - PPI")

#[2] 클래스 선언
p1  = Pet()
p1.bark_dog();
p2 = Pet()
p2.bark_cat()
p3 = Pet()
p3.bark_hamster()

