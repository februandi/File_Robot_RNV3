import serial
import time
import keyboard

# DEKLARASI PORT
port = 'COM4' # Lihat nama port dalam Arduino IDE: Tools > Port:
baud = 115200 # Default 115200
timeout = None # Biarkan seperti ini
ser = serial.Serial(port,baud,timeout=timeout)
time.sleep(1)

# DAFTAR PERINTAH YANG AKAN DIEKSEKUSI OLEH ROBOT, UBAH SESUAI KEBUTUHAN
cmdList = [

"G0 X0 Y216.90 Z-83 E0 F0", # Point: 1
"G0 X0 Y216.90 Z-92 E0 F0", # Point: 2
"M6", # Point: 3
"M207", # Point: 4
"G4 S1", # Point: 5
"G0 X0 Y216.90 Z0 E0 F0", # Point: 6
"G0 X-100 Y216.90 Z0 E100 F0", # Point: 7
"G0 X-100 Y216.90 Z-60 E100 F0", # Point: 8
"G0 X-100 Y216.90 Z-96 E100 F10", # Point: 9
"M7", # Point: 10
"M206", # Point: 11
"G4 S1", # Point: 12
"G0 X-100 Y216.90 Z-80 E100 F10", # Point: 13
"G0 X-100 Y216.90 Z0.00 E100 F0", # Point: 14
"G0 X-100 Y216.90 Z-75 E100 F0", # Point: 15
"G0 X-100 Y216.90 Z-95 E100 F5", # Point: 16
"M6", # Point: 17
"M207", # Point: 18
"G0 X-100 Y216.90 Z0 E100 F0", # Point: 19
"G0 X0 Y216.90 Z0 E0 F0", # Point: 20
"G0 X0 Y216.90 Z-93 E0 F0", # Point: 21
"M7", # Point: 22
"M206", # Point: 23
"G0 X0 Y216.90 Z0 E0 F0", # Point: 24
"G0 X100 Y216.90 Z0 E0 F0", # Point: 25
"G0 X-100 Y216.90 Z0 E0 F0", # Point: 26
"G0 X0 Y216.90 Z0 E0 F0", # Point: 27


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
