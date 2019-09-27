import os
import pty
from time import sleep

master, slave = pty.openpty()
s_name = os.ttyname(slave)
print(master)
print(s_name)

while True:
    print("Fake APRS Read: ")
    print(os.read(master, 1))

    os.write(master, b'w')
    sleep(0.1)
