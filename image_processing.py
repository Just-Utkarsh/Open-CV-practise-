import cv2

img = cv2.imread("icon.png")

resizing = cv2.resize(img, (200,200))
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurring = cv2.GaussianBlur(img,(5,5),0)
edges = cv2.Canny(img , 100  , 200)

#cv2.imshow("resize", resizing)
#cv2.imshow("grey", grey)
#cv2.imshow("blur", blurring)
cv2.imshow("edge", edges)\

cv2.waitKey(0)
cv2.destroyAllWindows()