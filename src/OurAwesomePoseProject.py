import time
import cv2

from PoseModule import PoseDetector


cap = cv2.VideoCapture('PoseVideos/test.mp4')
pTime = 0
detector = PoseDetector()

while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw=False)
    print(lmList)
    
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break