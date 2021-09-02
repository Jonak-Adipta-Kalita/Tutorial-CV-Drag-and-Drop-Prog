import cv2
import HandTrackingModule as htm

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = htm.HandDetector(detectionCon=0.8)

colorRect = (255, 0, 255)
cx, cy, w, h = 100, 100, 200, 200

while True:
    _, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList, _ = detector.findPosition(img)

    if lmList:
        l, _, _ = detector.findDistance(8, 12, img)
        if l < 30:
            cursor = lmList[8]
            if cx-w//2 < cursor[0] < cy+h//2 and cx-h//2 < cursor[1] < cy+h//2:
                colorRect = 0, 255, 0

                cx, cy = cursor
            else:
                colorRect = (255, 0, 255)

    cv2.rectangle(img, (cx-w//2, cy-h//2), (cx+w//2, cy+h//2), colorRect, cv2.FILLED)

    cv2.imshow("JAK Virtual Drag and Drop Prog", img)
    cv2.waitKey(1)
