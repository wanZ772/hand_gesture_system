import cv2 # type: ignore
import mediapipe  # type: ignore
from math import sqrt, pow

cam = cv2.VideoCapture(0)

mediapipe_hands = mediapipe.solutions.hands
hands = mediapipe_hands.Hands()
mediapipe_draws = mediapipe.solutions.drawing_utils
thumb_finger = (0,0)
pointer_finger = (0,0)
while True:
    status, image = cam.read()
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for id, landmarks in enumerate(hand_landmarks.landmark):
                height, width, channel = image.shape
                center_x, center_y = int(landmarks.x * width), int(landmarks.y * height)
                if id == 4:
                    thumb_finger = center_x, center_y
                if id == 8:
                    pointer_finger = center_x, center_y

                print(f"Length: {int(sqrt(pow(thumb_finger[0] - pointer_finger[0], 2) + pow(thumb_finger[1] - pointer_finger[1], 2)))}")
                    
            mediapipe_draws.draw_landmarks(image, hand_landmarks, mediapipe_hands.HAND_CONNECTIONS)

    cv2.imshow("Motor Hand Gesture Controller", image)
    cv2.waitKey(1)