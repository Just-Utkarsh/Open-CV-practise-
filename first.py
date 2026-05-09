import cv2

img1 = cv2.imread("icon.png")   # filename must be a string
cv2.imshow("the original image", img1)  # show the loaded image
cv2.waitKey(0)                  # keep the window open      # close the window