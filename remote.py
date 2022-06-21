from device import Device


class Remote:
    def __init__(self, device: Device):
        self.__device: Device = device

    def toggle_power(self):
        return print(self.__device.is_enable())

    def volumen_down(self):
        if self.__device.is_on():
            return print(self.__device.set_volumen(-1))
        else:
            return print("Device Shutdown")

    def volumen_up(self):
        if self.__device.is_on():
            return print(self.__device.set_volumen(1))
        else:
            return print("Device Shutdown")

    def channel_down(self):
        if self.__device.is_on():
            return print(self.__device.set_channel(-1))
        else:
            return print("Device Shutdown")

    def channel_up(self):
        if self.__device.is_on():
            return print(self.__device.set_channel(1))
        else:
            return print("Device Shutdown")
