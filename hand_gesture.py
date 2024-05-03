import mediapipe  # type: ignore
from math import sqrt, pow


mediapipe_hands = mediapipe.solutions.hands
hands = mediapipe_hands.Hands()
mediapipe_draws = mediapipe.solutions.drawing_utils


thumb_finger = (0,0)
pointer_finger = (0,0)

max_finger_length = 0
min_finger_length = 300

percentage = 0

class HandGesture():

 
    # current_percentage = self.percentage
    

    # Thread(target=control_unit).start()
    def hand_processing(self, imageRGB, image):
        global percentage
        global pointer_finger
        global thumb_finger
        global percentage
        global max_finger_length
        global min_finger_length
        global mediapipe_draws
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


                    if id == 4:
                        finger_length = int(sqrt(pow(thumb_finger[0] - pointer_finger[0], 2) + pow(thumb_finger[1] - pointer_finger[1], 2)))
                        if finger_length > max_finger_length:
                            max_finger_length = finger_length
                        

                        if min_finger_length > finger_length:
                            min_finger_length = finger_length


                        percentage = int(finger_length / (max_finger_length - min_finger_length) * 100)
                        # control_unit(percentage)
                mediapipe_draws.draw_landmarks(image, hand_landmarks, mediapipe_hands.HAND_CONNECTIONS)

                return percentage


# Thread(target=image_processing).start()
