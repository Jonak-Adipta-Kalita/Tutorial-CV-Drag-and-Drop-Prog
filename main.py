import cv2
import HandTrackingModule as htm
import drag_rect as dr
import cvzone
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = htm.HandDetector(detectionCon=0.8)

colorRect = (255, 0, 255)

rectList = []

for i in range(5):
    rectList.append(dr.DragRect([i*250+150, 150]))

while True:
    _, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList, _ = detector.findPosition(img)

    if lmList:
        l, _, _ = detector.findDistance(8, 12, img)
        if l < 30:
            cursor = lmList[8]
            for rect in rectList:
                rect.update(cursor)

    imgNew = np.zeros_like(img, np.uint8)
    for rect in rectList:
        cx, cy = rect.posCenter
        w, h = rect.size

        cv2.rectangle(imgNew, (cx-w//2, cy-h//2), (cx+w//2, cy+h//2), colorRect, cv2.FILLED)
        cvzone.cornerRect(imgNew, (cx-w//2, cy-h//2, w, h), 20, rt=0)

    out = img.copy()
    alpha = 0.5
    mask = imgNew.astype(bool)
    out[mask] = cv2.addWeighted(img, alpha, imgNew, 1 - alpha, 0)[mask]

    cv2.imshow("JAK Virtual Drag and Drop Prog", out)
    cv2.waitKey(1)
