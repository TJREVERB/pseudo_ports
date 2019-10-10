from serial import Serial
from devices.aprs_device import APRS
from devices.iridium_device import Iridium

aprs = APRS()
iridium = Iridium()

aprs_s = Serial(port=aprs.port_name)
i_s = Serial(port=iridium.port_name)

while True:
    # aprs_s.write(b'r')
    # i_s.write(b'i')
    print(f"APRS Wrote {aprs_s.read()}")
    print(f"Iridium Wrote {aprs_s.read()}")
