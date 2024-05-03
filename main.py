import cv2
from hand_gesture import HandGesture
from controller import Controller


def main():
    cam = cv2.VideoCapture(0)

    while True:
        status, image = cam.read()
        imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        percentage = HandGesture().hand_processing(imageRGB = imageRGB, image = image)
        Controller().volume_controller(volume=percentage)
        cv2.imshow("Motor Hand Gesture Controller", image)
        cv2.waitKey(1)

if "__main__" == __name__:
    main()