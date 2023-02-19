import pyfirmata
import time

pin= 6
port = 'COM3'
board = pyfirmata.Arduino(port)

while True:
    board.digital[pin].write(1)
    time.sleep(0.2) # delays for 5 seconds
    board.digital[pin].write(0)
    time.sleep(0.2) # delays for 5 seconds
    
board.exit()