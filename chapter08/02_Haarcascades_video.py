import cv2

def videoDetector(cap, cascade):
    while True:
        ret, img = cap.read()
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(img_gray,  # 입력 이미지
                                           scaleFactor=1.1,  # 이미지 피라미드 스케일 factor
                                           minNeighbors=5,  # 인접 객체 최소 거리 픽셀
                                           minSize=(20, 20)  # 탐지 객체 최소 크기
                                           )

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)

        cv2.imshow("img_result",img)
        if cv2.waitKey(1)&0xFF == 27:
            break

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

cap = cv2.VideoCapture("sample.mp4")
videoDetector(cap,faceCascade)
cv2.destroyAllWindows()