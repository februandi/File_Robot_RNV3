import serial
import time

# DEKLARASI PORT
port = 'COM10' # Lihat nama port dalam Arduino IDE: Tools > Port:
baud = 115200 # Default 115200
timeout = None # Biarkan seperti ini
ser = serial.Serial(port,baud,timeout=timeout)
time.sleep(1)

#LIST OF COMMANDS TO BE EXECUTED BY ROBOT ARM, CHANGE ACCORDINGLY
cmdList = [

]

bCmdList = []
for cmd in cmdList:
    cmd_temp = cmd + '\r'
    bCmdList.append(cmd_temp.encode('utf-8'))

#ROBOT HOMES ITSELF
#ser.write(b'M5\r')
ser.write(b'G28\r')
print("homing in progress")
time.sleep(10)
print(ser.readline())

def wait_complete():
    waitstatus = 1
    while True:
        a = ser.readline()
        if "MOVE" in a.decode("utf-8"):
            waitstatus = 0
            break

def wait_sensor():
    global cmdList
    while True:
        a = ser.readline()
        #program air panas
        if "IO1" in a.decode("utf-8"):
            cmdList = [
            "G4 S0,5", # tunggu 0.5 detik
            "M5",
            "G4 S0,5", # tunggu 0.5 detik

            "G0 X-189 Y4 F130", #ke posisi ambil
            "G4 S0,5", # tunggu 0.5 detik
            "G0 Z48 F130", #turun kecepatan high
            "G4 S0,9", # tunggu 1 detik
            "G0 Z12 F40", #Turun ambil gelas kosong
            "G4 S0,9", # tunggu 0.5 detik
            "M3", #capit geals
            "G4 S0,5", # tunggu 0.5 detik
            "G0 Z70 F40", #naik pelan
            "G4 S0,9", # tunggu 1 detik
            "G0 Z120 F130", #naik kecepatan high
            "G4 S0,5", # tunggu 0.5 detik
            "G0 X-50 Y136 F130", #Posisi di konveyor
            "G4 S0,5", # tunggu 0.5 detik
            "G0 Z50 F130", #turun kecepatan high
            "G4 S0,9", # tunggu 1 detik
            "G0 Z1 F40", # Posisi turun di konveyor
            "G4 S0,9", # tunggu 0.5 detik
            "M5",
            "G4 S0,9", # tunggu 0.5 detik
            "G0 Z50 F40", #naik pelan
            "G4 S0,9", # tunggu 1 detik
            "G0 Z120 F130", #naik kecepatan high
            "G4 S0,5", # tunggu 0.5 detik
            "G0 X0 Y174 F130", #ke posisi home
            "G4 S0,5", # tunggu 0.5 detik

            "G4 S1", # kirim status selesai
            "M1",
            "G4 S1",
            "M2", 
            ]
            break
        #program air dingin
        if "IO2" in a.decode("utf-8"):
            cmdList = [
            "G4 S0,5", # tunggu 0.5 detik
            "M5",
            "G4 S0,5", # tunggu 0.5 detik   

            "G0 X-168 Y128 F130", #ke posisi ambil
            "G4 S0,5", # tunggu 0.5 detik
            "G0 Z20 F130", #turun kecepatan high
            "G4 S0,9", # tunggu 1 detik
            "G0 Z-9 F40", #turun ambil gelas gosong
            "G4 S0,9", # tunggu 0.5 detik
            "M3",
            "G4 S0,9", # tunggu 0.5 detik
            "G0 Z50 F40", #naik pelan
            "G4 S0,9", # tunggu 1 detik
            "G0 Z120 F130", #naik kecepatan high
            "G4 S0,9", # tunggu 0.5 detik
            "G0 X-50 Y136 F130", #Posisi di konveyor
            "G4 S0,5", # tunggu 0.5 detik
            "G0 Z50 F130", # turun kecepatan high
            "G4 S0,9", # tunggu 1 detik
            "G0 Z3.8 F50", # Posisi turun di konveyor
            "G4 S0,9", # tunggu 0.5 detik
            "M5",
            "G4 S0,9", # tunggu 0.5 detik
            "G0 Z50 F50", #naik pelan
            "G4 S0,9", # tunggu 1 detik
            "G0 Z120 F130",  #naik kecepatan high
            "G4 S0,5", # tunggu 0.5 detik
            "G0 X0 Y174 F130", #ke posisi home

            "G4 S1", # kirim status selesai
            "M1",
            "G4 S1",
            "M2",       
            ]
            break
        if "IO3" in a.decode("utf-8"):
            cmdList = [
            "G0 E350 F100",
            "G4 S0,5", # tunggu 0.5 detik
            "G0 X66 Y138 F130", #posisi ambil gelas ada isi air 
            "G4 S0,9", # tunggu 0.5 detik
            "G0 Z50 F130", # Posisi turun ambil gelas
            "G4 S0,9", # tunggu 0.5 detik
            "G0 Z2 F50", # Posisi turun ambil gelas
            "G4 S0,9", # tunggu 0.5 detik
            "M3", #capit gelas
            "G4 S0,9", # tunggu 0.5 detik
            "G0 Z120 F50", #angkat ke atas
            "G4 S0,5", # tunggu 0.5 detik
            "G0 E400 F50", #geser mentok
            "G4 S0,5", # tunggu 0.5 detik
            "G0 X130 Y130 F50",
            "G4 S0,5", # tunggu 0.5 detik
            "G0 X140 Y180 F50",
            "G4 S0,5", # tunggu 0.5 detik
            "G0 Z50 F50",
            "G4 S0,5", # tunggu 0.5 detik
            "G0 G0 Z50 F50",
            "G4 S0,5", # tunggu 0.5 detik
            "G0 X140 Y230 F50",
            "G4 S0,5", # tunggu 0.5 detik
            "G0 Z4.8 F40",
            "G4 S1", # tunggu 0.5 detik
            "M5",
            "G4 S1", # tunggu 0.5 detik
            "G0 G0 Z40 F30",
            "G4 S0,5", # tunggu 0.5 detik
            "G0 X0 Y174 F130",
            "G4 S0,5", # tunggu 0.5 detik
            "G0 Z120 F130",
            "G4 S0,5", # tunggu 0.5 detik
            "G0 E0 F100",

            "G4 S1", # kirim status selesai
            "M1",
            "G4 S1",
            "M2",   
            ]
            break

#ROBOT BEGINS WHEN USER INPUTS "y"
begin = input('Tekan y untuk lanjut: ')
while True:
    if begin == 'y':
        print("Robot Ready")
        
        break

while True:
    wait_sensor()
    for cmd in cmdList:
        cmd_temp = cmd + '\r'
        cmd_temp = cmd_temp.encode('utf-8')
        ser.write(cmd_temp)
        print(cmd_temp)
        wait_complete()
