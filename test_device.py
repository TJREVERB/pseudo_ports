from serial import Serial
from devices.aprs_device import APRS

device = APRS()

s = Serial(port=device.port_name)

while True:
    s.write(b'r')
    print(f"APRS Wrote {s.read()}")
