from os import write
from time import sleep
from threading import Thread

from . import Device


class Iridium(Device):

    def __init__(self):
        Device.__init__(self, 'Iridium')
        data_writer = Thread(target=self.writer)
        data_writer.start()

    def writer(self):
        while True:
            write(self.master, b'q')
            sleep(2)
