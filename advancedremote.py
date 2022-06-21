from remote import Remote
from device import Device


class AdvancedRemote(Remote):

    def __init__(self, device: Device):
        super().__init__(device)
        self.__device: Device = device

    def mute(self):
        return print(f"Volumen: {self.__device.set_volumen(0)}")
