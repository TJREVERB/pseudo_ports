from serial import Serial

s = Serial(port='/dev/ttys000')

s.write(b'h')
