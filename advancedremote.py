from remote import Remote


class AdvancedRemote(Remote):

    def mute(self):
        self.__device.set_volumen(123)
