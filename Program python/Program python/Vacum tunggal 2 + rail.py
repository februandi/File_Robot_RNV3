import serial
import time
import keyboard

# DEKLARASI PORT
port = 'COM15' # Lihat nama port dalam Arduino IDE: Tools > Port:
baud = 115200 # Default 115200
timeout = None # Biarkan seperti ini
ser = serial.Serial(port,baud,timeout=timeout)
time.sleep(1)

# DAFTAR PERINTAH YANG AKAN DIEKSEKUSI OLEH ROBOT, UBAH SESUAI KEBUTUHAN
cmdList = [


"M7",
"G0 Z-76", # turun A1 (tamabah)
"M1", #ambil
"G0 Z0", # naik
"G0 X-50", # kiri
"G0 Z-98", # turun B1 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi
"G0 X0", # ke kordinat lagi

"M7",
"G0 Z-77", # turun A2 (tamabah)
"M1", #ambil
"G0 Z0", # naik
"G0 X-50", # kiri
"G0 Z-97", # turun B2 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi
"G0 X0", # ke kordinat lagi

"M7",
"G0 Z-78", # turun A3 (tamabah)
"M1", #ambil
"G0 Z0", # naik
"G0 X-50", # kiri
"G0 Z-96", # turun B2 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi
"G0 X0", # ke kordinat lagi

"M7",
"G0 Z-79", # turun A4 (tamabah)
"M1", #ambil
"G0 Z0", # naik
"G0 X-50", # kiri
"G0 Z-95", # turun B4 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi
"G0 X0", # ke kordinat lagi

"M7",
"G0 Z-80", # turun A5 (tamabah)
"M1", #ambil
"G0 Z0", # naik
"G0 X-50", # kiri
"G0 Z-94", # turun B5 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi
"G0 X0", # ke kordinat lagi

"M7",
"G0 Z-81", # turun A6 (tamabah)
"M1", #ambil
"G0 Z0", # naik
"G0 X-50", # kiri
"G0 Z-93", # turun B4 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi
"G0 X0", # ke kordinat lagi

"M7",
"G0 Z-82", # turun A7 (tamabah)
"M1", #ambil
"G0 Z0", # naik
"G0 X-50", # kiri
"G0 Z-92", # turun B7 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi
"G0 X0", # ke kordinat lagi

"M7",
"G0 Z-83", # turun A8 (tamabah)
"M1", #ambil
"G0 Z0", # naik
"G0 X-50", # kiri
"G0 Z-91", # turun B8 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi
"G0 X0", # ke kordinat lagi

"M7",
"G0 Z-84", # turun A9 (tamabah)
"M1", #ambil
"G0 Z0", # naik
"G0 X-50", # kiri
"G0 Z-90", # turun B9 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi
"G0 X0", # ke kordinat lagi

"M7",
"G0 Z-85", # turun A10 (tamabah)
"M1", #ambil
"G0 Z0", # naik
"G0 X-50", # kiri
"G0 Z-89", # turun B10 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi
"G0 X0", # ke kordinat lagi

"M7",
"G0 Z-86", # turun A11 (tamabah)
"M1", #ambil
"G0 Z0", # naik
"G0 X-50", # kiri
"G0 Z-88", # turun B11 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi
"G0 X0", # ke kordinat lagi

"M7",
"G0 Z-87", # turun A12 (tamabah)
"M1", #ambil
"G0 Z0", # naik
"G0 X-50", # kiri
"G0 Z-87", # turun B12 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi
"G0 X0", # ke kordinat lagi

"M7",
"G0 Z-88", # turun A13 (tamabah)
"M1", #ambil
"G0 Z0", # naik
"G0 X-50", # kiri
"G0 Z-86", # turun B13 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi
"G0 X0", # ke kordinat lagi

"M7",
"G0 Z-89", # turun A14 (tamabah)
"M1", #ambil
"G0 Z0", # naik
"G0 X-50", # kiri
"G0 Z-85", # turun B14 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi
"G0 X0", # ke kordinat lagi

"M7",
"G0 Z-90", # turun A15 (tamabah)
"M1", #ambil
"G0 Z0", # naik
"G0 X-50", # kiri
"G0 Z-84", # turun B15 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi
"G0 X0", # ke kordinat lagi

"M7",
"G0 Z-91", # turun A16 (tamabah)
"M1", #ambil
"G0 Z0", # naik
"G0 X-50", # kiri
"G0 Z-83", # turun B16 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi
"G0 X0", # ke kordinat lagi

"M7",
"G0 Z-92", # turun A17 (tamabah)
"M1", #ambil
"G0 Z0", # naik
"G0 X-50", # kiri
"G0 Z-82", # turun B17 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi
"G0 X0", # ke kordinat lagi

"M7",
"G0 Z-93", # turun A18 (tamabah)
"M1", #ambil
"G0 Z0", # naik
"G0 X-50", # kiri
"G0 Z-81", # turun B18 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi
"G0 X0", # ke kordinat lagi

"M7",
"G0 Z-94", # turun A19 (tamabah)
"M1", #ambil
"G0 Z0", # naik
"G0 X-50", # kiri
"G0 Z-80", # turun B19 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi
"G0 X0", # ke kordinat lagi

"M7",
"G0 Z-95", # turun A20 (tamabah)
"M1", #ambil
"G0 Z0", # naik
"G0 X-50", # kiri
"G0 Z-79", # turun B20 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi
"G0 X0", # ke kordinat lagi

"M7",
"G0 Z-96", # turun A21 (tamabah)
"M1", #ambil
"G0 Z0", # naik
"G0 X-50", # kiri
"G0 Z-78", # turun B21 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi
"G0 X0", # ke kordinat lagi

"M7",
"G0 Z-97", # turun A22 (tamabah)
"M1", #ambil
"G0 Z0", # naik
"G0 X-50", # kiri
"G0 Z-77", # turun B22 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi
"G0 X0", # ke kordinat lagi

"M7",
"G0 Z-98", # turun A23 (tamabah)
"M1", #ambil
"G0 Z0", # naik
"G0 X-50", # kiri
"G0 Z-76", # turun B23 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi
"G0 X0", # ke kordinat lagi
#-----------------------------------

"M7",
"G0 X-50", # kiri
"G0 Z-76", # turun B23 (tambah)
"M1", #ambil
"G0 Z0", # naik
"G0 X0", # kanan
"G0 Z-98", # turun A23 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi

"M7",
"G0 X-50", # kiri
"G0 Z-77", # turun B22 (tambah)
"M1", #ambil
"G0 Z0", # naik
"G0 X0", # kanan
"G0 Z-97", # turun A22 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi

"M7",
"G0 X-50", # kiri
"G0 Z-78", # turun B21 (tambah)
"M1", #ambil
"G0 Z0", # naik
"G0 X0", # kanan
"G0 Z-96", # turun A21 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi

"M7",
"G0 X-50", # kiri
"G0 Z-79", # turun B20 (tambah)
"M1", #ambil
"G0 Z0", # naik
"G0 X0", # kanan
"G0 Z-95", # turun A20 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi

"M7",
"G0 X-50", # kiri
"G0 Z-80", # turun B19 (tambah)
"M1", #ambil
"G0 Z0", # naik
"G0 X0", # kanan
"G0 Z-94", # turun A19 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi

"M7",
"G0 X-50", # kiri
"G0 Z-81", # turun B18 (tambah)
"M1", #ambil
"G0 Z0", # naik
"G0 X0", # kanan
"G0 Z-93", # turun A18 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi

"M7",
"G0 X-50", # kiri
"G0 Z-82", # turun B17 (tambah)
"M1", #ambil
"G0 Z0", # naik
"G0 X0", # kanan
"G0 Z-92", # turun A17 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi

"M7",
"G0 X-50", # kiri
"G0 Z-83", # turun B16 (tambah)
"M1", #ambil
"G0 Z0", # naik
"G0 X0", # kanan
"G0 Z-91", # turun A16 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi

"M7",
"G0 X-50", # kiri
"G0 Z-84", # turun B15 (tambah)
"M1", #ambil
"G0 Z0", # naik
"G0 X0", # kanan
"G0 Z-90", # turun A15 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi

"M7",
"G0 X-50", # kiri
"G0 Z-85", # turun B14 (tambah)
"M1", #ambil
"G0 Z0", # naik
"G0 X0", # kanan
"G0 Z-89", # turun A14 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi

"M7",
"G0 X-50", # kiri
"G0 Z-86", # turun B13 (tambah)
"M1", #ambil
"G0 Z0", # naik
"G0 X0", # kanan
"G0 Z-88", # turun A13 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi

"M7",
"G0 X-50", # kiri
"G0 Z-87", # turun B12 (tambah)
"M1", #ambil
"G0 Z0", # naik
"G0 X0", # kanan
"G0 Z-87", # turun A12 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi

"M7",
"G0 X-50", # kiri
"G0 Z-88", # turun B11 (tambah)
"M1", #ambil
"G0 Z0", # naik
"G0 X0", # kanan
"G0 Z-86", # turun A11 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi

"M7",
"G0 X-50", # kiri
"G0 Z-89", # turun B10 (tambah)
"M1", #ambil
"G0 Z0", # naik
"G0 X0", # kanan
"G0 Z-85", # turun A10 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi

"M7",
"G0 X-50", # kiri
"G0 Z-90", # turun B9 (tambah)
"M1", #ambil
"G0 Z0", # naik
"G0 X0", # kanan
"G0 Z-84", # turun A9 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi

"M7",
"G0 X-50", # kiri
"G0 Z-91", # turun B8 (tambah)
"M1", #ambil
"G0 Z0", # naik
"G0 X0", # kanan
"G0 Z-83", # turun A8 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi

"M7",
"G0 X-50", # kiri
"G0 Z-92", # turun B7 (tambah)
"M1", #ambil
"G0 Z0", # naik
"G0 X0", # kanan
"G0 Z-82", # turun A7 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi

"M7",
"G0 X-50", # kiri
"G0 Z-93", # turun B6 (tambah)
"M1", #ambil
"G0 Z0", # naik
"G0 X0", # kanan
"G0 Z-81", # turun A6 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi

"M7",
"G0 X-50", # kiri
"G0 Z-94", # turun B5 (tambah)
"M1", #ambil
"G0 Z0", # naik
"G0 X0", # kanan
"G0 Z-80", # turun A5 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi

"M7",
"G0 X-50", # kiri
"G0 Z-95", # turun B4 (tambah)
"M1", #ambil
"G0 Z0", # naik
"G0 X0", # kanan
"G0 Z-79", # turun A4 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi

"M7",
"G0 X-50", # kiri
"G0 Z-96", # turun B3 (tambah)
"M1", #ambil
"G0 Z0", # naik
"G0 X0", # kanan
"G0 Z-78", # turun A3 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi

"M7",
"G0 X-50", # kiri
"G0 Z-97", # turun B2 (tambah)
"M1", #ambil
"G0 Z0", # naik
"G0 X0", # kanan
"G0 Z-77", # turun A2 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi

"M7",
"G0 X-50", # kiri
"G0 Z-98", # turun B1 (tambah)
"M1", #ambil
"G0 Z0", # naik
"G0 X0", # kanan
"G0 Z-76", # turun A1 (kurang)
"M2",
"G4 S0.4",
"M6",
"G0 Z0", # naik lagi



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
