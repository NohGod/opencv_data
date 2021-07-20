import cv2

img_color = cv2.imread('apple.jpg', cv2.IMREAD_COLOR)

cv2.imshow("apple", img_color)
cv2.waitKey(0)

img_gray = cv2.cvtColor(img_color,cv2.COLOR_BGR2GRAY)
cv2.imshow("blackapple",img_gray)
cv2.waitKey(0)

ret, img_binary = cv2.threshold(img_gray, 120, 255, cv2.THRESH_BINARY)
# threshold(이진화할 대상 이미지(그레이 스케일이여야함), threshold
# THRESH_BINARY인 경우 threshold를 초과하는 값을 3번째 아규먼트 값으로 표현
cv2.imshow("Binary", img_binary)
cv2.waitKey(0)

cv2.destroyAllWindows()


##### 트랙 바 사용하기 #####

def nothing(x):
    pass

cv2.namedWindow('Binary')
cv2.createTrackbar('threshold', 'Binary', 0, 255, nothing)
cv2.setTrackbarPos('threshold', 'Binary', 127)

img_color = cv2.imread('apple.jpg', cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img_color,cv2.COLOR_BGR2GRAY)

while(True):
    low = cv2.getTrackbarPos('threshold', 'Binary')
    ret, img_binary = cv2.threshold(img_gray, low, 255, cv2.THRESH_BINARY)

    cv2.imshow("Binary", img_binary)
    if cv2.waitKey(1)&0xFF == 27:
        break

cv2.destroyAllWindows()

##### Binarization #####

def nothing(x):
    pass

cv2.namedWindow('Binary')
cv2.createTrackbar('threshold', 'Binary', 0, 255, nothing)
cv2.setTrackbarPos('threshold', 'Binary', 107)
#사물만 보이는 값 찾기(107)

img_color = cv2.imread('apple.jpg', cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img_color,cv2.COLOR_BGR2GRAY)

while(True):
    low = cv2.getTrackbarPos('threshold', 'Binary')
    ret, img_binary = cv2.threshold(img_gray, low, 255, cv2.THRESH_BINARY_INV)

    cv2.imshow("Binary", img_binary)
    img_result = cv2.bitwise_and(img_color, img_color, mask = img_binary)
    cv2.imshow('Result', img_result)
    if cv2.waitKey(1)&0xFF == 27:
        break

cv2.destroyAllWindows()