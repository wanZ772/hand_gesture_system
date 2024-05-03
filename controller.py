from pyvolume import custom
current_volume = 0
class Controller():
    
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