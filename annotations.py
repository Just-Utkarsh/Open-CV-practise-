import cv2
import numpy as np

canvas = np.zeros((512,512,3) , dtype=np.uint8)

cv2.line(canvas, (0,0), (511,511), (255,0,0), 5)
#cv2.rectangle(canvas, ())
#cv2.putText()

cv2.imshow("Canvas with shapes", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows() 