import cv2
import numpy as np
import matplotlib as plt

img = cv2.imread("D:\\Python Project\\python_programming\\tamrin10\\SuperMan.jpg")
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img3 = cv2.resize(img2, (640, 480))
#cv2.imshow("resize.img", img3)

img4 = cv2.cvtColor(img3, cv2.COLOR_RGB2HSV)
H, S, V = cv2.split(img4)
#cv2.imshow("gray0", H)
#cv2.imshow("gray1", S)
#cv2.imshow("gray2", V)

background = cv2.imread("D:\\Python Project\\python_programming\\tamrin10\\images.jpg")
background1 = cv2.cvtColor(background, cv2.COLOR_BGR2RGB)
background2 = cv2.resize(background1, (640, 480))

rows, cols = H.shape

for i in range(rows):
    for j in range(cols):
        if (37 < H[i, j] < 75 and 40 < S[i, j] and V[i, j] > 81): 
            img[i, j] = background2[i, j]


#u__green = np.array([104, 153, 70])
#l_green = np.array([30, 30, 0])

#mask = cv2.inRange(background2, l_green, u__green)
#res = cv2.bitwise_and(background2, background2, mask= mask)

#final = background2 - res
#final = np.where(final == 0, img3, final)

img_result = cv2.merge((H, S, V))

cv2.imshow("finally", img_result)
cv2.imwrite('result.jpg', cv2.cvtColor(background1, cv2.COLOR_RGB2BGR))
cv2.imshow("result", img)
#cv2.imshow("mask", final)

cv2.waitKey(0)
cv2.destroyAllWindows()