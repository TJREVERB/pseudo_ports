from os import ttyname, read
from threading import Thread
from pty import openpty


class Device:

    def __init__(self, name):
        self.master, self.slave = openpty()
        self.name = name
        self.port_name = ttyname(self.slave)

        read_thread = Thread(target=self.read_handler)
        read_thread.start()

    def read_handler(self):
        while True:
            byte = read(self.master, 1)
            print(f"{self.name} received data: {byte}")

