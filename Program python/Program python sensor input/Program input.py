import serial
import time

portRobot = 'COM5'
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
#--------------------------------------------------------------------------------------------
def Play_robot():
    serRobot.write(b'G0 Z0\r') #sumbu Z ke posisi 0
    wait_complete_robot()

    serRobot.write(b'G0 Z50\r') #sumbu Z ke posisi 50
    wait_complete_robot()

    serRobot.write(b'G0 Z0 E150\r') #sumbu Z dan E ke posisi 0 dan 150 secar bersamaan
    wait_complete_robot()

    serRobot.write(b'G0 Z0 E0\r') #sumbu Z dan E ke posisi 0 dan 0 secar bersamaan
    wait_complete_robot()
    pass

#tambahkan instruksi lain di sini

#--------------------------------------------------------------------------------------------

calibrate() # saat program pertama run calibrasi di panggil

while True:
    # Membaca data dari port serial
    data = serRobot.readline().decode('utf-8').strip()

    # jika sensor S1 OFF
    if "S1 OFF" in data: # menunggu S1 OFF
        print("OK")
        
        Play_robot() # Jika S1 OFF program Play_robot di panggil

    time.sleep(0.5)# tunggu sebentar sebelum membaca data lagi 
      

