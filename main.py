from device import Device
from advancedremote import AdvancedRemote
from radio import Radio
from remote import Remote
from tv import Tv
from smarttv import SmartTv

radio: Device = SmartTv()
control: Remote = Remote(radio)
control.volumen_up()
control.toggle_power()
control.channel_down()
control.channel_up()
control.channel_down()
control.volumen_down()
control.volumen_up()
control.volumen_up()
control.volumen_down()
control.toggle_power()
