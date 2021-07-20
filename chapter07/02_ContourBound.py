import cv2
import numpy as np
img = cv2.imread("hand.png")
img1 = img.copy()
img2 = img.copy()

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]

hull = cv2.convexHull(cnt)

img_contour = cv2.drawContours(img, [cnt], 0, (0,255,0),3)
img_hull = cv2.drawContours(img1, [hull], 0, (0,255,0), 3)
#drawContours(input image, contours, contourindex(-1 all contours), color, thickness

x,y,w,h = cv2.boundingRect(cnt)
img_result = cv2.rectangle(img2, (x,y), (x+w,y+h),(0,0,255),2)

rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
img_result = cv2.drawContours(img2, [box], 0, (255,0,0), 2)

cv2.imshow("contour",img_contour)
cv2.imshow("hull",img_hull)
cv2.imshow("box",img_result)
cv2.waitKey(0)
cv2.destroyAllWindows()