##### HSV 확인하기 #####

# import numpy as np
# import cv2
#
# color = [255,0,0]
# #파란색 BGR
# pixel = np.uint8([[color]])
# print(pixel)
# hsv = cv2.cvtColor(pixel, cv2.COLOR_BGR2HSV)
# hsv = hsv[0][0]
#
# print("bgr : ", color)
# print("hsv : ", hsv)

##### 컬러 찾기 #####

# import cv2
#
# img_color = cv2.imread('color_circle.jpg')
# height,width = img_color.shape[:2]
# #이미지의 너비와 높이를 가져옴
#
# img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV)
# #이미지를 HSV컬러 이미지로 변환
#
# lower_blue = (120-10, 30, 30)
# #하한가는 30으로 해야함, 너무 어두워서 검은색 혹은 너무 색이 옅어서 흰색에 가까운 색 배제하기 위함
# upper_blue = (120+10, 255, 255)
# img_mask = cv2.inRange(img_hsv, lower_blue, upper_blue)
# #범위내의 픽셀은 흰색, 나머지는 검은색
#
# img_result = cv2.bitwise_and(img_color, img_color, mask = img_mask)
# #범위값에 해당하는 이미지 획득
#
# cv2.imshow('img_color', img_color)
# cv2.imshow('img_mask', img_mask)
# cv2.imshow('img_result', img_result)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()