import cec

cec.init()

tv = cec.Device(0)
tv.power_on()
tv.standby()
tv.power_on()
