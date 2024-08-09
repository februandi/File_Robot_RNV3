import serial
import time
import keyboard

# DEKLARASI PORT
port = 'COM11' # Lihat nama port dalam Arduino IDE: Tools > Port:
baud = 115200 # Default 115200
timeout = None # Biarkan seperti ini
ser = serial.Serial(port,baud,timeout=timeout)
time.sleep(1)

# DAFTAR PERINTAH YANG AKAN DIEKSEKUSI OLEH ROBOT, UBAH SESUAI KEBUTUHAN
cmdList = [


"G0 Y150  Z0 F200",
"G0 Y230  Z130 F200",
"G0 Y150 Z100 F200",
"G0 Y150 Z130 F50",

"G0 Y140 Z190 F200",
"G0 Y200 Z190 F200",
"G0 Y140 Z190 F200",

"G0 Y160 Z0 F200",
"G0 Y200 Z0 F200",
"G0 Y160 Z0 F200",

"G0 Y140 Z190 F200",
"G0 Y200 Z190 F200",
"G0 Y140 Z190 F200",

"G0 Y160 Z0 F200",
"G0 Y200 Z0 F200",
"G0 Y160 Z0 F200",

"G0 Y140 Z190 F200",
"G0 Y200 Z190 F200",
"G0 Y140 Z190 F200",

"G0 Y160 Z0 F200",
"G0 Y200 Z0 F200",
"G0 Y160 Z0 F200",

"G0 Y140 Z190 F200",
"G0 Y200 Z190 F200",
"G0 Y140 Z190 F200",

"G0 Y160 Z0 F200",
"G0 Y200 Z0 F200",
"G0 Y160 Z0 F200",

"G0 X0 Y195 Z130 F200",

"G0 X-100 Y195 Z0 F200",
"G0 X0 Y195 Z130 F200",

"G0 X100 Y195 Z0 F200",
"G0 X0 Y195 Z130 F200",

"G0 X-100 Y195 Z0 F200",
"G0 X0 Y195 Z130 F200",

"G0 X100 Y195 Z0 F200",
"G0 X0 Y195 Z130 F200",

"G0 X-100 Y195 Z0 F200",
"G0 X0 Y195 Z130 F200",

"G0 X100 Y195 Z0 F200",
"G0 X0 Y195 Z130 F200",

"G0 X-100 Y195 Z0 F200", 
"G0 X0 Y195 Z130 F200",

"G0 X100 Y195 Z0 F200",
"G0 X0 Y195 Z130 F200",

"G0 X-100 Y195 Z0 F200", 
"G0 X0 Y195 Z130 F200",

"G0 X100 Y195 Z0 F200",
"G0 X0 Y195 Z130 F200",

"G0 X-100 Y195 Z0 F200", 
"G0 X0 Y195 Z130 F200",

"G0 X100 Y195 Z0 F200",
"G0 X0 Y195 Z130 F200",

"G0 X-100 Y195 Z0 F200", 
"G0 X0 Y195 Z130 F200",

"G0 X100 Y195 Z0 F200",
"G0 X0 Y195 Z130 F200",

"G0 X-100 Y195 Z0 F200", 
"G0 X0 Y195 Z130 F200",

"G0 X100 Y195 Z0 F200",
"G0 X0 Y195 Z130 F200",




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
