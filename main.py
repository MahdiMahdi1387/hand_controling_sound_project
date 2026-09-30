import cv2
import mediapipe as mp
from pygame import mixer

mixer.init()
mixer.music.load('Davood Behboodi - Khoshgeleh.mp3')
mixer.music.set_volume(0.1)
mixer.music.play(-1)

mp_hand = mp.solutions.hands.Hands(max_num_hands=1)
draw_utils = mp.solutions.drawing_utils


cap = cv2.VideoCapture(0)

finger_counter = 0
finger_tips = [8, 12, 16, 20]
volume = 0.1

while True:
    volume = 0.1
    finger_counter = 0
    success, frame = cap.read()

    if not success:
        break

    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = mp_hand.process(frameRGB)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            landmark = hand.landmark

            for tip in finger_tips:
                if landmark[tip].y < landmark[tip - 2].y:
                    finger_counter += 1

    if finger_counter == 1:
        volume = 0.25
    if finger_counter == 2:
        volume = 0.5
    if finger_counter == 3:
        volume = 0.75
    if finger_counter == 4:
        volume = 1.0
    
    mixer.music.set_volume(volume)

    cv2.putText(frame, str(volume * 100), (50, 100),
                cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0,  0), 3)
                

    cv2.imshow('Hand-sound-controling', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

mixer.music.stop()
mixer.quit()
cap.release()
cv2.destroyAllWindows()

