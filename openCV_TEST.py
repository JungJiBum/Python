import cv2
# print(cv2.__version__)    4.6.0

path = "C:/Users/tec/Desktop/python/Python/Inflearn/Inflearn_Python_Recipe/bs4_naver/image"
target = input("찾고자하는 이미지를 적어주세요. : ")
img = cv2.imread(path + '/' + target + '.jpg')

cv2.imshow('img', img)

cv2.waitKey(5000)
cv2.destroyAllWindows()
# Inflearn\Inflearn_Python_Recipe\bs4_naver\image\결혼공략.jpg
# C:\Users\tec\Desktop\python\Python\Inflearn\Inflearn_Python_Recipe\bs4_naver\image\결혼공략.jpg
# https://bskyvision.com/entry/python-cv2imread-%ED%95%9C%EA%B8%80-%ED%8C%8C%EC%9D%BC-%EA%B2%BD%EB%A1%9C-%EC%9D%B8%EC%8B%9D%EC%9D%84-%EB%AA%BB%ED%95%98%EB%8A%94-%EB%AC%B8%EC%A0%9C-%ED%95%B4%EA%B2%B0-%EB%B0%A9%EB%B2%95
