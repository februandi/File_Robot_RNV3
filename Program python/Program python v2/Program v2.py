import serial
import time

portRobot = 'COM7'
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
    a = serRobot.readline().decode("utf-8")
    print(a)
    while "ok" not in a:
        a = serRobot.readline().decode("utf-8")
        print(a)
    pass

def robot_robot_stepper_on():
    serRobot.write(b'M17\r') 
    wait_complete_robot()
    pass

def robot_robot_stepper_off():
    serRobot.write(b'M18\r') 
    wait_complete_robot()
    pass

def Robot_Main():
    def send_and_wait(command):
        serRobot.write(command.encode('utf-8') + b'\r')
        a = serRobot.readline().decode("utf-8")
        print(a)
        while "ok" not in a:
            a = serRobot.readline().decode("utf-8")
            print(a)

    send_and_wait('G0 X0.00 Y216.90 Z0.00 E0.00 F0.00')
    send_and_wait('G0 X0.00 Y216.90 Z100.00 E0.00 F0.00')
    send_and_wait('G0 X50.00 Y216.90 Z100.00 E0.00 F0.00')
    #send_and_wait('G4 S3') #tunggu 3 detik
    send_and_wait('G0 X-50.00 Y216.90 Z100.00 E0.00 F0.00')
    pass




calibrate()


mulai = input('Tekan y untuk mulai: ')
print("")
while True:
    if mulai == 'y':
        print("")
        print("Robots Start Working")
        break

while True:
    # Lakukan apa yang perlu dilakukan dalam loop utama
    Robot_Main()
    pass
