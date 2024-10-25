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

def reset_servo():
    serRobot.write(b'M3\r')
    wait_complete_robot()
    serRobot.write(b'M5\r')
    wait_complete_robot()
    serRobot.write(b'M3\r')
    wait_complete_robot()
    pass
#-------------------------robot tes gripper servo (pakai rell)-----------------------------
def Play_robot():
    serRobot.write(b'G0 X0.00 Y216.90 Z138.00 E280.00 F0.00\r') 
    wait_complete_robot()
    serRobot.write(b'G0 X0.00 Y216.90 Z-99.00 E280.00 F0.00\r') 
    wait_complete_robot()
    serRobot.write(b'M5\r') 
    wait_complete_robot()
    serRobot.write(b'G0 X0.00 Y216.90 Z130.00 E280.00 F0.00\r') 
    wait_complete_robot()
    serRobot.write(b'G0 X100.00 Y216.90 Z130.00 E100.00 F0.00\r') 
    wait_complete_robot()
    serRobot.write(b'G0 X-120.00 Y216.90 Z130.00 E100.00 F0.00\r') 
    wait_complete_robot()
    serRobot.write(b'G0 X0.00 Y216.90 Z130.00 E100.00 F0.00\r') 
    wait_complete_robot()
    serRobot.write(b'G0 X0.00 Y216.90 Z-100.00 E0.00 F0.00\r') 
    wait_complete_robot()
    serRobot.write(b'M3\r') 
    wait_complete_robot()
    serRobot.write(b'G0 X0.00 Y216.90 Z0.00 E0.00 F0.00\r') 
    wait_complete_robot()
    serRobot.write(b'G0 X0.00 Y216.90 Z-100.00 E0.00 F0.00\r') 
    wait_complete_robot()
    serRobot.write(b'M5\r') 
    wait_complete_robot()
    serRobot.write(b'G0 X0.00 Y216.90 Z100.00 E0.00 F0.00\r') 
    wait_complete_robot()
    serRobot.write(b'G0 X0.00 Y216.90 Z100.00 E280.00 F0.00\r') 
    wait_complete_robot()
    serRobot.write(b'G0 X0.00 Y216.90 Z0.00 E280.00 F0.00\r') 
    wait_complete_robot()
    serRobot.write(b'G0 X0.00 Y216.90 Z-99.00 E280.00 F0.00\r') 
    wait_complete_robot()
    serRobot.write(b'M3\r') 
    wait_complete_robot()
    pass

#tambahkan instruksi lain di sini

#--------------------------------------------------------------------------------------------
reset_servo()
calibrate() # saat program pertama run calibrasi di panggil

while True:
    # Membaca data dari port serial
    data = serRobot.readline().decode('utf-8').strip()
    print("Menuggu sensor")
    # jika sensor S1 OFF
    if "S1 OFF" in data: # menunggu S1 OFF
        print("OK")
        
        Play_robot() # Jika S1 OFF program Play_robot di panggil

    time.sleep(0.5)# tunggu sebentar sebelum membaca data lagi 
      

