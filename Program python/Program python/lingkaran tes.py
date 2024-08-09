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



"G0 X108.5629 Y154.2746",
"G0 X106.9673 Y154.8443",
"G0 X105.8994 Y158.2169",
"G0 X107.8492 Y161.0179",
"G0 X113.3336 Y161.8334",
"G0 X117.5506 Y158.372",
"G0 X118.1719 Y150.7704",
"G0 X113.1409 Y145.1429",
"G0 X103.4178 Y144.6964",
"G0 X96.3839 Y151.3165",
"G0 X96.1035 Y163.1634",
"G0 X104.3214 Y171.6012",
"G0 X118.2937 Y171.7202",
"G0 X128.1339 Y161.8998",
"G0 X128.0942 Y145.8013",
"G0 X116.6686 Y134.5595",
"G0 X98.4433 Y134.7562",
"G0 X85.8006 Y147.7887",
"G0 X86.1529 Y168.1414",
"G0 X100.7937 Y182.1845",
"G0 X123.2741 Y181.6773",
"G0 X138.7173 Y165.4276",
"G0 X138.0558 Y140.8192",
"G0 X120.1964 Y123.9762",



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