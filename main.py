class Car:
    wheels = 4
    headlight = 2
    steeringwheel = 1

    def __init__(self, color, doors,window):
        self.color = color
        self.doors = doors
        self.window = window


car1 = Car(color="red", doors=5, window=4)

class Bowedinstruments:
    strings = 4
    bow = 1
    musicalholes = 2
    def __init__(self, material, bowsize,playstile):
        self.material = material
        self.bowsize = bowsize
        self.playstile = playstile

bowedinstrument1 = Bowedinstruments(material="wood",bowsize="big",playstile="presto")




