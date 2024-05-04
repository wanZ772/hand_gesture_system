from pyvolume import custom
import serial
from time import sleep

board = serial.Serial('COM3', 9600)
board.timeout = 1
current_volume = 0
current_speed = -1
current_status = False
class Controller():
    
    def motor_speed(self, speed):
        global current_speed
        global current_status
        # speed = speed / 100 * 255
        if (speed != None) and (speed != current_speed):
            if speed > 50:
                board.write("on\n".encode())
            else:
                board.write("off\n".encode())
            current_speed = speed
            print(f"from board -> {board.readline().decode('ascii')}")
            # if speed > 50:
            #     board.write("on".encode())
            # else:
            #     board.write("off".encode())
            # sleep(2)
            # print(f"From board -> {board.readline().decode('ascii')}")

    def volume_controller(self, volume):
        global current_volume
        global current_volume
        if volume != current_volume and volume != None:
            try:
                
                custom(percent=volume)
            except:
                pass
            print(f"Volume: {volume}%")
            # current_volume = volume