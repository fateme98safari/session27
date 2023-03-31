import cv2

image=cv2.imread("Batman.py\Bat.jpg")

image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

_,image=cv2.threshold(image,100,255,cv2.THRESH_BINARY_INV)
image[305:340,480:503]=image[305:330,510:530]=image[290:310,495:515]=255
image[290:310,495:515]=255


cv2.putText(image,"BATMAN",(380,500),cv2.FONT_HERSHEY_SIMPLEX,2,255,2)

cv2.imwrite("result.jpg",image)

cv2.waitKey()
