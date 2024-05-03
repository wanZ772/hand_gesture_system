import cv2 # type: ignore
import mediapipe  # type: ignore
from math import sqrt, pow
from os import system
from pyvolume import custom
from threading import Thread


cam = cv2.VideoCapture(0)

mediapipe_hands = mediapipe.solutions.hands
hands = mediapipe_hands.Hands()
mediapipe_draws = mediapipe.solutions.drawing_utils


thumb_finger = (0,0)
pointer_finger = (0,0)

max_finger_length = 0
min_finger_length = 1000

percentage = 0
current_percentage = percentage
def control_unit(percentage):
    global current_percentage
    # while True:
    if percentage != current_percentage:
        try:
            custom(percent=percentage)
            print(f"Volume: {percentage}%")
            current_percentage = percentage
            # system('cls')
        except:
            pass

# Thread(target=control_unit).start()
def image_processing():
    pass
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
                if id == 20:
                    pointer_finger = center_x, center_y


                if id == 4:
                    finger_length = int(sqrt(pow(thumb_finger[0] - pointer_finger[0], 2) + pow(thumb_finger[1] - pointer_finger[1], 2)))
                    if finger_length > max_finger_length:
                        max_finger_length = finger_length
                    if min_finger_length > finger_length:
                        min_finger_length = 50
                    percentage = int(finger_length / (max_finger_length - min_finger_length) * 100)
                    control_unit(percentage)
            mediapipe_draws.draw_landmarks(image, hand_landmarks, mediapipe_hands.HAND_CONNECTIONS)

    cv2.imshow("Motor Hand Gesture Controller", image)
    cv2.waitKey(1)


# Thread(target=image_processing).start()
