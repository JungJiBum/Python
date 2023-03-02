import cv2
path = "C:/Users/tec/Desktop/python/Python/Inflearn/Inflearn_ImageProcessing/card_crop_4.png"
img = cv2.imread(path,0)

rows, cols = img.shape

flag = 0    # 스케일 줄이기 키우기 위한 플래그

scale = 1   # 초기값 설정
angle = 0   # 초기 0도


while True:
    M = cv2.getRotationMatrix2D((cols/2,rows/2),angle,scale)
    dst = cv2.warpAffine(img,M,(cols,rows))

    angle = angle +10
    if angle == 360:
        angle=0
    
    if flag == 0:   # 스케일 점점 줄어듬
        scale -= 0.01
        if scale <= 0:
            flag = 1
    if flag == 1:
        scale += 0.01
        if scale >= 1:
            flag = 0
    
    cv2.imshow('img',dst)
    if cv2.waitKey(50) == 27:
        break
cv2.destroyAllWindows()

