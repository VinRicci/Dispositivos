from device import Device


class Radio(Device):
    def __init__(self):
        self.__volumen: int = 50
        self.__estacion: list[float] = [90.1, 90.3, 90.5, 90.7, 90.9, 91.0]
        self.__index: int = 0
        self.__encendido: bool = False

    def is_on(self):
        return self.__encendido

    def is_enable(self):
        if self.__encendido:
            self.disable()
        else:
            self.enable()
        return self.__encendido

    def enable(self):
        self.__encendido = True

    def disable(self):
        self.__encendido = False

    def get_volumen(self):
        return self.__volumen

    def set_volumen(self, percent: int):
        if percent == 1 or percent == -1:
            if 0 == self.__volumen and percent == -1:
                self.__volumen = 0
            elif 100 == self.__volumen and percent == 1:
                self.__volumen = 100
            elif -1 < self.__volumen < 101:
                self.__volumen += percent
        else:
            self.__volumen = percent
        return self.get_volumen()

    def get_channel(self):
        return self.__estacion[self.__index]

    def set_channel(self, channel: int):
        if self.__index >= 5 and channel == 1:
            self.__index = 0
        if self.__index == 0 and channel == -1:
            self.__index = 5
        else:
            self.__index += channel
        return self.get_channel()
