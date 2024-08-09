import serial
import time
import keyboard

# DEKLARASI PORT
port = 'COM10' # Lihat nama port dalam Arduino IDE: Tools > Port:
baud = 115200 # Default 115200
timeout = None # Biarkan seperti ini
ser = serial.Serial(port,baud,timeout=timeout)
time.sleep(1)

#LIST OF COMMANDS TO BE EXECUTED BY ROBOT ARM, CHANGE ACCORDINGLY
cmdList = [

"M3",           #buka gripper
"G4 S0.2",      #tunggu 0.2s
"G0 z0",      #turun speed normal ke 0
"G4 S0.2",      #tunggu 0.2s
"G0 z-50 F170",      #turun speed cepat ke -50
"G4 S0.2",      #tunggu 0.2s
"G0 z-70 F30",      #turun speed pelan ke -70
"M5",           #ambil
"G4 S0.2",      #tunggu 0.2s
"G0 z0",        #naik
"G0 x70 F170", 
"G4 S0.2",      #tunggu 0.2s
"G0 z-50 F170",      #turun speed cepat ke -50
"G4 S0.2",      #tunggu 0.2s
"G0 z-70 F30",      #turun speed pelan ke -70
"M3",           #buka gripper
"G0 z0",
"G4 S0.2",      #tunggu 0.2s
"G0 x0 F170",
"G4 S0.2",      #tunggu 0.2s
"G0 x70 F170",
"G4 S0.2",      #tunggu 0.2s
"G0 z-50 F170",      #turun speed cepat ke -50
"G4 S0.2",      #tunggu 0.2s
"G0 z-70 F30",      #turun speed pelan ke -70
"M5",           #ambil
"G4 S0.2",      #tunggu 0.2s
"G0 z0",
"G4 S0.2",      #tunggu 0.2s
"G0 x0",
"G4 S0.2",      #tunggu 0.2s
"G0 z-50 F170",      #turun speed cepat ke -50
"G4 S0.2",      #tunggu 0.2s
"G0 z-70 F30",      #turun speed pelan ke -70
"G4 S0.2",      #tunggu 0.2s
"M3",           #buka gripper
"G4 S0.2",      #tunggu 0.2s
"G0 z0",

]

bCmdList = []
for cmd in cmdList:
    cmd_temp = cmd + '\r'
    bCmdList.append(cmd_temp.encode('utf-8'))

# ROBOT MELAKUKAN HOME
ser.write(b'G28\r')
print("")
print("Home sedang dalam proses")
print("")
time.sleep(5)
print(ser.readline())
print(ser.readline())
print(ser.readline())
print(ser.readline())

def tunggu_selesai():
    waitstatus = 1
    while True:
        a = ser.readline()
        print(a)  # Mencetak respons yang diterima
        if "ok" in a.decode("utf-8"):
            waitstatus = 0
            break

print("")
mulai = input('Tekan y untuk mulai: ')
print("")
while True:
    if mulai == 'y':
        print("")
        print("Robots Start Working")
        print("")
        print("tahan q untuk berhenti")
        break

while True:
    for cmd in bCmdList:
        ser.write(cmd)
        #print(cmd)
        tunggu_selesai()
        if keyboard.is_pressed('q'): #tahan q sampai robot posisi ok
            ser.write(b'G0 X0 Y140 Z31\r')
            print("")
            print("Robot Stop")
            print("")
            time.sleep(1) # Menunggu 1 detik
            print("Stepper akan off dalam 5 detik")
            print("")
            time.sleep(5) # Menunggu 5 detik
            ser.write(b'M18\r')
            tunggu_selesai()
            ser.close()
            exit()