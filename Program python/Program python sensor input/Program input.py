import serial
import time

portRobot = 'COM4'
baudRobot = 115200
timeoutRobot = None
serRobot = serial.Serial(portRobot,baudRobot,timeout=timeoutRobot)

time.sleep(1)

def wait_complete_robot():
    waitstatus = 1
    while True:
        a = serRobot.readline()
        print(a.decode("utf-8"))
        if "ok" in a.decode("utf-8"):
            waitstatus = 0
            break                    

def calibrate():
    serRobot.write(b'G28\r')
    wait_complete_robot()
    pass

calibrate()

while True:
    # Membaca data dari port serial
    data = serRobot.readline().decode('utf-8').strip()

