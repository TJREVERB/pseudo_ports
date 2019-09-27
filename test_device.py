from serial import Serial

s = Serial(port='/dev/ttys000')

while True:
    s.write(b'r')
    print("APRS Wrote")
    print(s.read())
