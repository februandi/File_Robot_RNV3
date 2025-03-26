import serial # pip install pyserial
import time
import sys
import keyboard  # pip install keyboard

portRobot = 'COM5'
baudRobot = 115200
timeoutRobot = None
serRobot = serial.Serial(portRobot,baudRobot,timeout=timeoutRobot)

time.sleep(1)

def wait_complete_robot():
    waitstatus = 1
    timeout_start = time.time()
    timeout_limit = 15  # Meningkatkan timeout menjadi 15 detik
    
    # Bersihkan buffer serial terlebih dahulu
    serRobot.reset_input_buffer()
    
    while waitstatus:
        if serRobot.in_waiting:
            a = serRobot.readline()
            try:
                decoded = a.decode("utf-8").strip()
                print(f"Received: {decoded}")  # Print data yang diterima dengan label
                if "ok" in decoded.lower():  # Cek lowercase untuk menangani 'OK' atau 'ok'
                    print("OK response detected")  # Debug message
                    waitstatus = 0
                    break
            except UnicodeDecodeError:
                print("Received invalid data")
                
        # Tambahkan timeout untuk mencegah program hang
        if time.time() - timeout_start > timeout_limit:
            print("Timeout waiting for 'ok' response")
            return False
            
        time.sleep(0.05)  # Kurangi jeda untuk respons lebih cepat
    
    return True

def calibrate():
    serRobot.write(b'G28\r')
    wait_complete_robot()
    pass

def send_gcode(command):
    print(f"\nSending: {command}")  # Tambah newline untuk memisahkan perintah
    
    # Clear input buffer sebelum kirim perintah baru
    serRobot.reset_input_buffer()
    
    # Kirim perintah
    serRobot.write(command.encode() + b'\r')
    
    # Tunggu hingga data terkirim sepenuhnya
    serRobot.flush()
    
    # Tunggu respons
    success = wait_complete_robot()
    
    # Retry if failed
    if not success:
        print(f"Retrying command: {command}")
        
        # Clear buffer lagi sebelum retry
        serRobot.reset_input_buffer()
        
        serRobot.write(command.encode() + b'\r')
        serRobot.flush()
        success = wait_complete_robot()
        
        if not success:
            print(f"Command failed after retry: {command}")
        
    return success

# Tambahkan fungsi untuk request status sensor
def request_sensor_status():
    serRobot.write(b'M105\r')
    # Tidak perlu wait_complete_robot() di sini untuk mencegah blocking

#-------------------------robot tes gripper vacum (tanpa rell)-----------------------------
def posisi_awal():
    send_gcode('G0 X0,00 Y217,00 Z138,00 F0,00') # posisi awal
    pass

def ambil_benda():
    send_gcode('G0 X-112,00 Y227,00 Z138,00 F0,00') 
    send_gcode('G0 X-112,00 Y227,00 Z-32,00 F0,00')
    send_gcode('G0 X-112,00 Y227,00 Z-60,00 F0,00') 
    send_gcode('VACUM ON')
    send_gcode('G0 X-112,00 Y227,00 Z-35,00 F0,00')
    send_gcode('G0 X-112,00 Y227,00 Z6,00 F0,00') # ke sensor 
    pass

def sensor_1():
    send_gcode('G0 X-45,00 Y203,00 Z6,00 F0,00') 
    send_gcode('G0 X-45,00 Y203,00 Z-55,00 F0,00') 
    send_gcode('VACUM OFF') 
    #send_gcode('G4 S0.2')   
    pass

def sensor_2():
    send_gcode('G0 X-8,00 Y203,00 Z6,00 F0,00') 
    send_gcode('G0 X-8,00 Y203,00 Z-55,00 F0,00') 
    send_gcode('VACUM OFF')  
    #send_gcode('G4 S0.2')
    pass

def sensor_3():
    send_gcode('G0 X28,00 Y227,00 Z-17,00 F0,00') 
    send_gcode('G0 X28,00 Y203,00 Z-17,00 F0,00') 
    send_gcode('G0 X28,00 Y203,00 Z-55,00 F0,00')  
    send_gcode('VACUM OFF')
    #send_gcode('G4 S0.2')
    pass

def robot_off():
    send_gcode('G0 X0,00 Y156,00 Z44,00 F0,00') 
    send_gcode('M18') # matikan motor
    send_gcode('VACUM OFF')
    pass
#--------------------------------------------------------------------------------------------
time.sleep(0.2)
calibrate() # saat program pertama run calibrasi di panggil

try:
    print("Tekan 'q' untuk keluar dari program")
    
    # Variabel untuk tracking status sensor
    s1_last_status = False
    s2_last_status = False
    s3_last_status = False
    all_sensors_filled = False
    
    # Tambahkan variabel untuk tracking waktu request
    last_request_time = time.time()
    
    # Request status awal
    request_sensor_status()
    
    while True:
        # Cek keyboard terlebih dahulu
        if keyboard.is_pressed('q'):
            print("\nTombol q terdeteksi")
            print("Robot Stop")
            print("\nStepper akan off dalam 5 detik")
            robot_off()
            time.sleep(5)
            serRobot.close()
            print("Program selesai")
            sys.exit()

        # Kemudian baca serial
        try:
            if serRobot.in_waiting:  # Cek apakah ada data yang tersedia
                data = serRobot.readline().decode('utf-8').strip()
                if data:
                    print(f"Data received: {data}")
                    
                    # Cek format status sensor dari M105
                    if "SENSOR STATUS:" in data:
                        # Simpan status sensor (perhatikan S1:ON berarti sensor kosong)
                        s1_kosong = "S1:ON" in data
                        s2_kosong = "S2:ON" in data
                        s3_kosong = "S3:ON" in data
                        
                        # Tambahkan flag untuk mendeteksi percobaan pengisian yang gagal
                        action_taken = False
                        
                        # Cek jika semua sensor terisi (semua OFF)
                        if not s1_kosong and not s2_kosong and not s3_kosong:
                            print("Semua sensor sudah terisi")
                            if not all_sensors_filled:
                                all_sensors_filled = True
                            posisi_awal()
                            
                        # Cek jika semua sensor kosong (semua ON)
                        elif s1_kosong and s2_kosong and s3_kosong:
                            print("Semua sensor kosong")
                            all_sensors_filled = False
                            
                            # Gunakan variabel untuk menandai sensor mana yang sedang dicoba isi
                            print("Mulai mengisi sensor satu per satu...")
                            
                            # Isi sensor 1 terlebih dahulu
                            print("Sensor 1 kosong, mengisi...")
                            ambil_benda()
                            sensor_1()
                            action_taken = True
                            
                        # Jika ada sensor yang kosong (ON), isi sensor tersebut
                        else:
                            print("Mengecek dan mengisi sensor...")
                            
                            # Prioritaskan sensor dalam urutan: S1, S2, S3
                            if s1_kosong:
                                print("Sensor 1 kosong, mengisi...")
                                ambil_benda()
                                sensor_1()
                                action_taken = True
                            elif s2_kosong:
                                print("Sensor 2 kosong, mengisi...")
                                ambil_benda()
                                sensor_2()
                                action_taken = True
                            elif s3_kosong:
                                print("Sensor 3 kosong, mengisi...")
                                ambil_benda()
                                sensor_3()
                                action_taken = True
                        
                        # Update status terakhir setelah aksi dilakukan
                        s1_last_status = s1_kosong
                        s2_last_status = s2_kosong
                        s3_last_status = s3_kosong
                        
                        # Request status setelah mengisi satu sensor
                        if action_taken:
                            request_sensor_status()
                            last_request_time = time.time()  # Reset timer
                            time.sleep(0.5)  # Tunggu respons
                                
                    
        except serial.SerialException as e:
            print(f"Serial Error: {e}")
            break
            
        # Request status setiap 2 detik
        current_time = time.time()
        if current_time - last_request_time > 1.0:
            request_sensor_status()
            last_request_time = current_time
            
        time.sleep(0.1)  # Memberikan jeda kecil untuk mengurangi penggunaan CPU

except KeyboardInterrupt:
    print("\nProgram dihentikan oleh user")
except Exception as e:
    print(f"\nError: {e}")
finally:
    print("Cleaning up...")
    print("Program selesai")



