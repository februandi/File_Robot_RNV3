import serial
import time
import keyboard

# DEKLARASI PORT
port = 'COM16' # Lihat nama port dalam Arduino IDE: Tools > Port:
baud = 115200 # Default 115200
timeout = None # Biarkan seperti ini
ser = serial.Serial(port,baud,timeout=timeout)
time.sleep(1)

# DAFTAR PERINTAH YANG AKAN DIEKSEKUSI OLEH ROBOT, UBAH SESUAI KEBUTUHAN
cmdList = [

    "G0 X0,00 Y217,00 Z138,00 E0,00 F0,00",
    "G0 X0,00 Y217,00 Z112,00 E0,00 F0,00",
    "G0 X0,00 Y249,00 Z112,00 E0,00 F0,00",
    "G0 X64,00 Y249,00 Z112,00 E0,00 F0,00",
    "G0 X-81,00 Y249,00 Z112,00 E0,00 F0,00"


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
    while True:
        a = ser.readline().decode("utf-8").strip()
        print(a)  # Mencetak respons yang diterima
        if "ok" in a.lower():  # Gunakan lower() untuk memastikan huruf kecil juga diterima
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
        if keyboard.is_pressed('q'):
            ser.write(b'G0 X0 Y140 Z31\r')
            print("\nRobot Stop\n")
            time.sleep(1)
            print("Stepper akan off dalam 5 detik\n")
            time.sleep(5)
            ser.write(b'M18\r')
            tunggu_selesai()
            ser.close()
            exit()

        ser.write(cmd)
        print(cmd)
        tunggu_selesai()

