import cv2 as cv
import mediapipe as mp
import time
from Gestures import Gestures

"""
Realizacja projektu:
* Cezary Malejka
* Mateusz Grube

Projekt ma na celu przedstawienie działania bibliotek opencv oraz mediapipe w celu zaprezentowania rozpoznawania gestów wykonywanych przez obserwowanego przez kamerę użytkownika.

Instrukcja:
W celu uruchomienia projektu należy (będąc w katalogu gestrureDetect) użyć komendy
python3 main.py
"""

cap = cv.VideoCapture(0)
mpHands = mp.solutions.hands
VisionRunningMode = mp.tasks.vision.RunningMode

hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime, cTime = 0, 9

gestures = Gestures()

while True:
    success, img = cap.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:

            # SET h, w, c for
            h, w, c = img.shape

            # SET x and y position for index finger and hand palm
            f_x = int(handLms.landmark[8].x * w)
            f_y = int(handLms.landmark[8].y * h)
            sf_x = int(handLms.landmark[4].x * w)
            sf_y = int(handLms.landmark[4].y * h)
            palm_x = int(handLms.landmark[0].x * w)
            palm_y = int(handLms.landmark[0].y * h)

            cx, cy = int(handLms.landmark[8].x * w), int(handLms.landmark[8].y * h)

            gestures.recognize_gesture(f_x, f_y, sf_x, sf_y, palm_x, palm_y)

            cv.circle(img, (cx, cy), 15, (255, 0, 0), cv.FILLED)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    cTime = time.time()
    fps = 1 / (cTime - pTime)

    pTime = cTime
    cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv.imshow("Hand gestures", img)
    cv.waitKey(1)


cap.release()
cv.destroyAllWindows()

