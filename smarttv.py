from device import Device


class SmartTv (Device):
    def __init__(self):
        self.__volumen: int = 50
        self.__estacion: list[str] = ["Netflix", "HBO", "Disney+", "Prime Video", "Star+", "Crunchyroll"]
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
        if 0 == self.__volumen and percent == -1:
            self.__volumen = 0
        elif 100 == self.__volumen and percent == 1:
            self.__volumen = 100
        elif -1 < self.__volumen < 101:
            self.__volumen += percent
        elif percent == 123:
            self.__volumen = 0
        return self.get_volumen()

    def get_channel(self):
        return self.__estacion[self.__index]

    def set_channel(self, channel: int):
        if -1 > self.__index < 6:
            self.__index += channel
        elif 0 == self.__index and channel == -1:
            self.__index = 5
        elif self.__index == 5 and channel == 1:
            self.__index = 0
        return self.get_channel()
