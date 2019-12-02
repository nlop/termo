import serial
import time

def main():
    with serial.Serial('/dev/ttyUSB0',9600,timeout=1) as ser:
        while(True):
            dbyte = ser.readline()[:-2]
            num = int.from_bytes(dbyte,"little")
            print('raw:',dbyte)
            print('int:',num)
            time.sleep(0.1)
main()
