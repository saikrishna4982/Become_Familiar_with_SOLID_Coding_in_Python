from abc import ABC,abstractclassmethod
class Device(ABC):
    power: bool
    def __init__(self, initial_state: bool=False):
        self.power = initial_state
    def turn_on(self):
        raise NotImplementedError
    def turn_off(self):
        raise NotImplementedError
class Switch:
    def __init__(self, device: Device, pressed: bool=False):
        self.device = device
        self.pressed = pressed
    def toggle(self):
        self.pressed = not self.pressed # Toggle
        if self.pressed:
            self.device.turn_on()
            print("Turned On")
        else:
            self.device.turn_off()
            print("Turned Off")
class LightBulb(Device):
    def turn_on(self):
        self.power = True
    def turn_off(self):
        self.power = False
d=Device()
l=LightBulb()
s=Switch(l)
s.toggle()
s.toggle()
