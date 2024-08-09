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


"M7",
"G0 Z-60", # turun A1 (tamabah)
"M1", #ambil
"G0 Z130", # naik
"G0 E355 F90",

"G0 X-170 Y67", #pisis 1

"G0 Z21", #turun
"M2",
"G4 S0.4",
"M6",
"G0 Z130", #naik
"G0 X0 Y195",
"G0 E0 F70",

"M7",
"G0 Z-61", # turun A1 (tamabah)
"M1", #ambil
"G0 Z130", # naik
"G0 E355 F90",

"G0 X-175 Y96", #pisis 2

"G0 Z21", #turun
"M2",
"G4 S0.4",
"M6",
"G0 Z130", #naik
"G0 X0 Y195",
"G0 E0 F70",

"M7",
"G0 Z-62", # turun A1 (tamabah)
"M1", #ambil
"G0 Z130", # naik
"G0 E355 F90",

"G0 X-208 Y96", #pisis 3

"G0 Z21", #turun
"M2",
"G4 S0.4",
"M6",
"G0 Z130", #naik
"G0 X0 Y195",
"G0 E0 F70",

"M7",
"G0 Z-63", # turun A1 (tamabah)
"M1", #ambil
"G0 Z130", # naik
"G0 E355 F90",

"G0 X-208 Y67", #pisis 4

"G0 Z21", #turun
"M2",
"G4 S0.4",
"M6",
"G0 Z130", #naik
"G0 X0 Y195",
"G0 E0 F70",


#-----------------------------------



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
