import cv2

img = cv2.imread("hand.png")
img1 = img.copy()
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#findContours(input image(binary), mode, method)

#mode
#RETR_EXTERNAL = all outline
#RETR_LIST = all outline without hierarchy
#RETR_CCOMP = all outline to 2 layer
#RETR_TREE = all outline to tree architecture

#method
#CHAIN_APPROX_NONE : all the coordinate without APPROX
#CHAIN_APPROX_SIMPLE : vertex coordinate

#contours = contour coordinate(list)

cnt = contours[0]

hull = cv2.convexHull(cnt)
# img_contour = cv2.drawContours(img, contours, 0, (0,255,0),3)
img_contour = cv2.drawContours(img, [cnt], 0, (0,255,0),3)
img_hull = cv2.drawContours(img1, [hull], 0, (0,255,0), 3)
#drawContours(input image, contours, contourindex(-1 all contours), color, thickness

cv2.imshow("contour",img_contour)
cv2.imshow("hull",img_hull)

cv2.waitKey(0)
cv2.destroyAllWindows()