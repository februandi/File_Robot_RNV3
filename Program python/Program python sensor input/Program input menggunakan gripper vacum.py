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
#-------------------------robot tes gripper vacum (pakai rell)-----------------------------
def Play_robot():
    serRobot.write(b'G0 X0.00 Y216.90 Z138.00 E0.00 F0.00\r') 
    wait_complete_robot()
    serRobot.write(b'G0 X0.00 Y216.90 Z-93.00 E0.00 F0.00\r')
    wait_complete_robot()
    serRobot.write(b'M6\r') 
    wait_complete_robot()
    serRobot.write(b'M207\r')
    wait_complete_robot()
    serRobot.write(b'G0 X0.00 Y216.90 Z0.00 E0.00 F0.00\r')
    wait_complete_robot()
    serRobot.write(b'G0 X0.00 Y216.90 Z0.00 E200.00 F0.00\r')
    wait_complete_robot()
    serRobot.write(b'G0 X0.00 Y216.90 Z-93.00 E200.00 F0.00\r')
    wait_complete_robot()
    serRobot.write(b'M7\r')
    wait_complete_robot()
    serRobot.write(b'M206\r')
    wait_complete_robot()
    serRobot.write(b'G0 X0.00 Y216.90 Z0.00 E200.00 F0.00\r')
    wait_complete_robot()
    serRobot.write(b'G0 X0.00 Y216.90 Z-93.00 E200.00 F0.00\r')
    wait_complete_robot()
    serRobot.write(b'M6\r')
    wait_complete_robot()
    serRobot.write(b'M207\r')
    wait_complete_robot()
    serRobot.write(b'G0 X0.00 Y216.90 Z0.00 E200.00 F0.00\r')
    wait_complete_robot()
    serRobot.write(b'G0 X0.00 Y216.90 Z0.00 E0.00 F0.00\r')
    wait_complete_robot()
    serRobot.write(b'G0 X0.00 Y216.90 Z-93.00 E0.00 F0.00\r')
    wait_complete_robot()
    serRobot.write(b'M7\r')
    wait_complete_robot()
    serRobot.write(b'M206\r')
    wait_complete_robot()
    serRobot.write(b'G0 X0.00 Y216.90 Z0.00 E0.00 F0.00\r')
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
      

