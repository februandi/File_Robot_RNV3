import serial
import time
import keyboard

# DEKLARASI PORT
port = 'COM10' # Lihat nama port dalam Arduino IDE: Tools > Port:
baud = 115200 # Default 115200
timeout = None # Biarkan seperti ini
ser = serial.Serial(port,baud,timeout=timeout)
time.sleep(1)

# DAFTAR PERINTAH YANG AKAN DIEKSEKUSI OLEH ROBOT, UBAH SESUAI KEBUTUHAN
cmdList = [

"g0 E177 F80",
"g0 Z0",
"g0 Z130",
"g0 Z190",
"g0 Z0",
"g0 Z-50",
"g0 Z0",
"g0 Y300",
"g0 Y150",
"g0 Y195",
"g0 X200",
"g0 X0",
"g0 X-200",
"g0 X0 Z130 E355 F80",
"g0 Z0 E177 F80",
"g0 X100 E277 F80",
"g0 X-100 E77 F80",
"g0 X100 E277 F80",
"g0 X-100 E77 F80",
"g0 X100 E277 F80",
"g0 X-100 E77 F80",

"M3",
"G4 S0.5",
"M5",
"G4 S0.5",
"M3",
"G4 S0.5",
"M5",
"G4 S0.5",
"M3",
"G4 S0.5",
"M5",
"G4 S0.5",
"M3",
"G4 S0.5",
"M5",

"g0 z0",
"g0 x190 y200",
"g0 x150 y0",
"g0 x250  y0 e100  f100",

"g0 z20 F140",
"g0 x150 y0 F140",
"g0 z0 F140",
"g0 x250  y0 e200  f100",

"g0 z20 F140",
"g0 x150 y0 F140",
"g0 z0 F140",
"g0 x250  y0 e300  f100",

"G4 S1",

"g0 x150  y0 e200  f100",
"g0 z20 F140",
"g0 x250 y0 F140",
"g0 z0 F140",
"g0 x150  y0 e100  f100",

"g0 z20 F140",
"g0 x250  y0 F140",
"g0 z0 F170",
"g0 x150  y0 e0  f100",

"g0 x190 y200",

"g0 x0 y195 Z130",

"g0 z0 F200",
"g0 X100 F200",
"g0 E150 F100",
"g0 Z-50 f50",
"g0 X0 Z150 F200",
"g0 Z0 F200",
"g0 Z130 F200",
"g0 X-140 F200",
"g0 X0 Z0 F200",
"g0 Y300 F200",
"g0 x200 y195 F200",
"g0 x0 y195 z130 e0  f100",

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
