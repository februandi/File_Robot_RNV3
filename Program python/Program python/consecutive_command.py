import serial
import time

#PORT DECLARATIONS
port = 'COM10' #SEE PORT NAME IN ARDUINO IDE: TOOLS>PORT:
baud = 115200 #BY DEFAULT 115200
timeout = None #LEAVE AS IS
ser = serial.Serial(port,baud,timeout=timeout)
time.sleep(1)

#LIST OF COMMANDS TO BE EXECUTED BY ROBOT ARM, CHANGE ACCORDINGLY
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

#ROBOT HOMES ITSELF
ser.write(b'G28\r')
print("homing in progress")
time.sleep(10)
print(ser.readline())
print(ser.readline())
print(ser.readline())
print(ser.readline())

def wait_complete():
    waitstatus = 1
    while True:
        a = ser.readline()
        print(a)  # Mencetak respons yang diterima
        if "ok" in a.decode("utf-8"):
            waitstatus = 0
            break
      

#ROBOT BEGINS WHEN USER INPUTS "y"
begin = input('type y to begin: ')

while True:
    if begin == 'y':
        break

for bCmd in bCmdList:
    ser.write(bCmd)
    print(bCmd)
    wait_complete()
