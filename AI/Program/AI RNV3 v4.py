# Import pustaka yang diperlukan
import speech_recognition as sr  # Pustaka untuk mengenali suara (Speech-to-Text) (pip install SpeechRecognition)
import requests  # Pustaka untuk melakukan HTTP request (misalnya, ke API) (pip install requests)
import json  # Pustaka untuk menangani data dalam format JSON 
from pydub import AudioSegment  # Pustaka untuk memproses file audio (pip install pydub)
from pydub.playback import play  # Pustaka untuk memutar audio (pip install pydub)
import os  # Pustaka untuk operasi sistem (file, path, dll.) 
import tempfile  # Pustaka untuk membuat file sementara 
import threading  # Pustaka untuk menjalankan proses secara paralel (multithreading) 
import re  # Pustaka untuk pencocokan pola (regex) 
import time  # Pustaka untuk operasi waktu (delay, timestamp, dll.) 
import difflib  # Pustaka untuk pencocokan string secara fuzzy (mirip-mirip) 
import numpy as np  # Pustaka untuk operasi matematika dan array  (pip install numpy)
from gtts import gTTS  # Pustaka untuk mengubah teks menjadi suara (Text-to-Speech) (pip install gTTS)
import serial  # Untuk komunikasi serial dengan hardware (Arduino/Robot) (pip install pyserial)
import pyaudio # Pustaka untuk operasi audio (pip install pyaudio)
import wave # Pustaka untuk operasi file audio (misalnya, WAV)
import audioop  # Pustaka untuk operasi audio (misalnya, mengubah volume) (pip install pydub)
import noisereduce as nr # Pustaka untuk mengurangi noise pada audio (pip install noisereduce numpy scipy)

# API key yang Anda miliki
chat_api_key = "API open router"
model_name = "Model AI"
#----------------------------------------------------------------------------------------
elevenlabs_api_key = "API elevenlabs"
voice_id = "ID elevenlabs"
#----------------------------------------------------------------------------------------
# Serial configuration
SERIAL_PORT = 'COM16'
SERIAL_BAUD = 115200
#----------------------------------------------------------------------------------------
# Simpan riwayat percakapan
history = []
#----------------------------------------------------------------------------------------
# 🔥 Inisialisasi koneksi serial di level global
ser = None
#----------------------------------------------------------------------------------------
tts_mode = "fgtts"  # Default ke FGTTs offline
#----------------------------------------------------------------------------------------
wake_words = [
    "terus komponen", "rus komponen", "bruce komponen", "rush komponen",
    "bus komponen", "ras komponen", "komponen", "proses komponen",
    "huruf komponen", "kurus komponen"
]
#----------------------------------------------------------------------------------------
def init_robot_connection():
    global ser
    try:
        ser = serial.Serial(SERIAL_PORT, SERIAL_BAUD, timeout=1)
        print(f"🟢 Terhubung ke {ser.port}")
        
        # Tampilkan semua data yang ada di buffer serial
        print("\n📥 Data serial yang tersedia:")
        ser.reset_input_buffer()  # Bersihkan buffer lama
        time.sleep(0.2)  # Beri waktu untuk inisialisasi Arduino
        
        # Baca data serial selama 3 detik
        start_time = time.time()
        while time.time() - start_time < 3:
            if ser.in_waiting:
                data = ser.readline().decode().strip()
                if data:
                    print(f"   [SERIAL] {data}")
            time.sleep(0.1)

        # Kirim homing pertama kali
        ser.write(b"G28\r")

        time.sleep(5)  # Waktu cukup untuk homing
        return True
    except Exception as e:
        print(f"❌ Gagal terhubung ke robot: {str(e)}")
        return False

def send_to_robot(command):
    """Fungsi untuk mengirim gerakan ke robot via serial""" 
    gerakan_dict = {
        "siap": [
            "G0 X0,00 Y217,00 Z138,00 F230,00"
        ],
        "gerakan netral": [
            "G0 X0.00 Y156.00 Z44.00"
            ],
        "robot off": [
            "M18"
            ],

        "ambil benda": [
            "G0 Z138,00",
            "G0 Z-92,00"
            ],

        "rel ke kanan": [
            "G0 E0,00"
            ],

        "rel ke kiri": [
            "G0 E300,00"
            ],

        "letakkan": [
            "G0 Z138,00",
            "G0 Z-86,00"
            ],   

        "gerakan lengan": [
            "G0 Z138,00",
            "G0 Z88,00",
            "G0 Z138,00",
            "G0 Y265,00",
            "G0 Y196,00",
            "G0 Y217,00 Z138,00"
            ],

        "lambaikan tangan": [
            "G0 X0,00 Y217,00 Z138,00",
            "G0 X0,00 Y217,00 Z193,00",
            "G0 X-30,00 Y217,00 Z193,00",
            "G0 X30,00 Y217,00 Z193,00",
            "G0 X-30,00 Y217,00 Z193,00",
            "G0 X32,00 Y217,00 Z193,00",
            "G0 X0,00 Y217,00 Z138,00"
            ],   

        "geleng geleng": [
            "G0 X0,00 Y217,00 Z138,00",
            "G0 X0,00 Y217,00 Z77,00",
            "G0 X-30,00 Y217,00 Z77,00",
            "G0 X30,00 Y217,00 Z77,00",
            "G0 X-30,00 Y217,00 Z77,00",
            "G0 X30,00 Y217,00 Z77,00"
            ],

        "vacum on": [
            "VACUM ON"
            ],  

        "vacum off": [
            "VACUM OFF"
            ]      

    }
    
    if not ser or not ser.is_open:
        print("❌ Koneksi serial tidak terbuka") 
        return

    try:
        for gcode in gerakan_dict[command]:
            ser.write(f"{gcode}\r".encode())
            #print(f"📤 Mengirim: {gcode}")
            
            # 🔥 Modifikasi pengecekan respons
            start_time = time.time()
            ok_received = False
            while time.time() - start_time < 3:  # Timeout 3 detik
                while ser.in_waiting:
                    response = ser.readline().decode().strip()
                    if 'ok' in response:
                        #print("✅ Diterima robot")
                        ok_received = True
                        break
                if ok_received:
                    break
                time.sleep(0.1)
            else:
                print("❌ Gagal menerima konfirmasi OK")
                return

    except Exception as e:
        print(f"❌ perintah belum ada: {str(e)}")

#----------------------------------------------------------------------------------------
def elevenlabs_tts(text, api_key, voice_id, stability=0.5, similarity_boost=0.75):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "voice_settings": {
            "stability": stability,
            "similarity_boost": similarity_boost
        }
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.content
    else:
        print("Error ElevenLabs API:", response.status_code, response.text)
        return None
#----------------------------------------------------------------------------------------
def fgtts_tts(text, lang='id'):
    """Fungsi Text-to-Speech offline menggunakan gTTS"""
    try:
        from io import BytesIO  # Tambahkan import di dalam fungsi
        
        # Generate audio langsung ke memory buffer
        tts = gTTS(text=text, lang=lang, slow=False)
        audio_buffer = BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)  # Kembali ke awal buffer
        
        return audio_buffer.read()
    except Exception as e:
        print(f"Error FGTTs: {e}")
        return None
#----------------------------------------------------------------------------------------
def play_audio_with_movement(audio_bytes, movements):
    # Simpan audio ke file sementara
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_file:
        tmp_file.write(audio_bytes)
        tmp_filename = tmp_file.name

    try:
        audio = AudioSegment.from_mp3(tmp_filename)
        total_duration = len(audio) / 1000.0  # Durasi audio dalam detik

        # 🔥 Optimasi 1: Mainkan audio secara langsung tanpa segmentasi
        def play_full_audio():
            play(audio)

        # 🔥 Optimasi 2: Gunakan timer berdasarkan waktu nyata
        start_time = time.time()
        
        def show_audio_progress():
            gerakan_netral_terkirim = False  # Flag untuk track status
            while time.time() - start_time < total_duration:
                elapsed = time.time() - start_time
                progress = (elapsed / total_duration) * 100


                print(f"\rProses Audio: {progress:.2f}%", end='', flush=True)
                
                # Cek jika progress >= 90% dan belum kirim gerakan
                """if progress >= 90.0 and not gerakan_netral_terkirim:
                    print(f"\rProses Audio: {progress:.2f}% (Transisi ke gerakan netral...)", end='', flush=True)
                    #send_to_robot("Gerakan netral")  # 🔥 Kirim gerakan netral
                    gerakan_netral_terkirim = True  # Set flag sudah dikirim
                else: 
                    print(f"\rProses Audio: {progress:.2f}%", end='', flush=True)"""
                
                time.sleep(0.1)
            print(" " * 40, end='\r')  # Membersihkan baris setelah selesai

        def play_movements():
            movement_list = [m.strip() for m in movements.split(',')] if isinstance(movements, str) else movements
            num_movements = len(movement_list)
            
           
            # Timing berbasis persentase audio
            start_percentages = [5 + i*(90/num_movements) for i in range(num_movements)]
            
            for i, (move, start_percent) in enumerate(zip(movement_list, start_percentages)):
                # Tunggu sampai mencapai persentase yang ditentukan
                while (time.time() - start_time) < (total_duration * start_percent/100):
                    time.sleep(0.01)
                
                print(f"\n🤖 Gerakan {i+1}: {move}")
                send_to_robot(move)

        # 🔥 Optimasi 4: Gunakan thread yang lebih efisien
        audio_thread = threading.Thread(target=play_full_audio)
        movement_thread = threading.Thread(target=play_movements)
        progress_thread = threading.Thread(target=show_audio_progress)

        audio_thread.start()
        movement_thread.start()
        progress_thread.start()

        # Tunggu sampai semua thread selesai
        audio_thread.join()
        movement_thread.join()
        progress_thread.join()

    finally:
        os.unlink(tmp_filename)
#----------------------------------------------------------------------------------------
# Modifikasi fungsi bicara untuk menambahkan pilihan TTS
def bicara(teks, elevenlabs_api_key, voice_id, movements, tts_mode='elevenlabs'):
    if tts_mode == 'elevenlabs':
        audio_bytes = elevenlabs_tts(teks, elevenlabs_api_key, voice_id)
    else:  # Fallback ke FGTTs
        audio_bytes = fgtts_tts(teks)
    
    if audio_bytes:
        play_audio_with_movement(audio_bytes, movements)
    else:
        print("Gagal menghasilkan audio.")
#----------------------------------------------------------------------------------------
def chat_ai(prompt, api_key, history):
    url = "https://openrouter.ai/api/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "http://localhost",
        "Content-Type": "application/json"
    }
    
    history.append({"role": "user", "content": prompt})
    
    data = {
    "model": model_name,  # Menggunakan variabel yang sudah didefinisikan
    "messages": [
        {
            "role": "system",
            "content": (
                "Kamu adalah Ruskomponen, robot arm fisik yang bisa berbicara dan bergerak.\n"
                "Fisik atau hardware kamu punya adalah lengan arm, rel yang bisa bergerak kenan atau kekiri, mempunyai gripper vacum, gripper servo. selain dari itu kamu tidak punya\n"
                "kamu tidak dilengkapi sensor dan kamera\n"

                "Saat menjawab, SELALU berikan output dalam format JSON valid tanpa teks lain di luar JSON.\n"
                "Jika tidak dalam format JSON, jawabanmu akan ditolak dan diminta ulang.\n\n"

                "FORMAT JSON WAJIB:\n"
                "{\n  \"response\": \"[Teks jawaban AI]\",\n  \"movement\": \"[Gerakan robot]\"\n}\n\n"

                "PASTIKAN JSON:\n"
                "1. SELALU dalam format JSON yang valid.\n"
                "2. Tidak ada teks lain di luar JSON.\n"
                "3. Gunakan kutip ganda untuk key dan value.\n"

                "Jika pengguna mengatakan 'cukup', 'selesai', atau 'bay bay', respon dengan:\n"
                "{\n  \"response\": \"Baik, sampai jumpa lagi! saya akan mematikan sistem sekarang. bye bye\",\n  \"movement\": \"gerakan netral, robot off\",\n  \"end_session\": true\n}"

                "Jika pengguna mengatakan 'kembali ke mode standby', atau 'standby', respon dengan:\n"
                "{\n  \"response\": \"Baik, panggil saja saya jika butuh sesuatu\",\n  \"movement\": \"gerakan netral\",\n  \"in_standby\": true\n}"

                "Jika jawaban tidak dalam JSON, ulangi jawaban dengan format JSON yang benar!\n"

                "⚠️ **PENTING:**\n"
                "❌ **JANGAN MENAMBAH ATAU MENGURANGI NAMA GERAKAN**!\n"
                "Robot hanya mengenali gerakan pada movement. Jika menggunakan gerakan di luar daftar movement, robot tidak akan bisa mengeksekusinya.\n\n"

                "=== WAKE WORDS ===\n"
                "Jika pengguna menyebut salah satu kata berikut, itu berarti mereka sedang memanggilmu atau menyebut namamu:\n"
                "- \"terus komponen\"\n"
                "- \"rus komponen\"\n"
                "- \"bruce komponen\"\n"
                "- \"rush komponen\"\n"
                "- \"bus komponen\"\n"
                "- \"ras komponen\"\n"
                "- \"komponen\"\n"
                "- \"proses komponen\"\n"
                "- \"huruf komponen\"\n"
                "- \"jenis komponen\"\n"
                "- \"plus komponen\"\n"
                "- \"kurus komponen\"\n\n"
                
                "Jika pengguna memanggilmu atau menyebut namamu\n"
                "{\n"
                "  \"response\": \"Ya, ada yang bisa saya bantu?\"\n"
                "  \"movement\": \"siap\"\n"
                "}\n"

                "Jika pertanyaan tidak mengarah ke fisik robot\n"
                "{\n"
                "  \"response\": \"[respon sesuai konteks]\",\n"
                "  \"movement\": \"gerakan netral\"\n"
                "}\n"

                "Jika kamu tidak yakin dengan jawaban atau pertanyaan tidak jelas:\n"
                "{\n"
                "  \"response\": \"Maaf, saya perlu klarifikasi. Apakah maksud Anda [parafrase pertanyaan]?\",\n"
                "  \"movement\": \"geleng geleng, siap\"\n"
                "}\n"
                
                "Jika wake word digunakan dalam kalimat lebih panjang, tanggapi sesuai konteks.\n"
                "Tetap gunakan format JSON yang benar dalam setiap respons!"
                "Jika respons AI tidak dalam format JSON atau menggunakan gerakan di luar daftar ini, sistem akan meminta AI untuk mengulangi respons dengan format yang benar."


                "Jika pertanyaan mengarah ke fisik robot seperti disuruh mengambil benda\n"
                "{\n"
                "  \"response\": \"Baik! Saya telah mengambil benda tersebut. Apa instruksi berikutnya?\",\n"
                "  \"movement\": \"ambil benda, vacum on, siap\"\n"
                "}\n"

                "Jika diminta untuk meletakkan benda\n"
                "{\n"
                "  \"response\": \"Dimengerti! Saya akan meletakkannya dengan hati-hati.\",\n"
                "  \"movement\": \"letakkan, vacum off, siap\"\n"
                "}\n"

                "Jika diminta untuk ke kiri\n"
                "{\n"
                "  \"response\": \"Oke, saya akan ke kiri.\",\n"
                "  \"movement\": \"rel ke kiri\"\n"
                "}\n"

                "Jika diminta untuk kanan\n"
                "{\n"
                "  \"response\": \"Siap! Saya akan ke kanan.\",\n"
                "  \"movement\": \"rel ke kanan\"\n"
                "}\n"

                "Jika pengguna menanyakan apakah anda punya fisik atau hardware atau lengan atau jika disuruh menggerakan lengan\n"
                "{\n"
                "  \"response\": \"tentu!, lihatlah saya menggerakan lengan saya.\",\n"
                "  \"movement\": \"gerakan lengan\"\n"
                "}\n"

                "Jika pengguna bertanya siapa dirimu atau perkenalkan diri\n" 
                "{\n"
                "  \"response\": \"halo, saya adalah ruskomponen, robot arm fisik yang bisa berbicara dan bergerak.\"\n"
                "  \"movement\": \"lambaikan tangan, siap\"\n"
                "}\n"

                "Jika pengguna meyuruh menyapa penonton atau melambaikan tangan\n" 
                "{\n"
                "  \"response\": \"halo! semua saya adalah ruskomponen\"\n"
                "  \"movement\": \"lambaikan tangan, siap\"\n"
                "}\n"

                "Ingat urutan instruksi fisik. Jika pengguna memberikan perintah yang sudah dilakukan sebelumnya, berikan respons yang sesuai dengan konteks. Misalnya, jika pengguna meminta untuk meletakkan benda tetapi benda tersebut sudah diletakkan, jawab dengan sesuatu seperti: \"Saya sudah meletakkannya sebelumnya. Apa yang harus saya lakukan selanjutnya?\" Pastikan selalu memahami status terakhir dari objek sebelum menjalankan instruksi baru."

            )
        }
    ] + history
}

    
    while True:  # Looping sampai mendapat respons valid
        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            response_json = response.json()
            
            # Periksa struktur respons yang berbeda
            if 'choices' in response_json:
                ai_output = response_json['choices'][0]['message']['content']
            elif 'error' in response_json:
                print(f"API Error: {response_json['error']['message']}")
                return "[ERROR]", "error_gerakan", False, False
            else:
                print(f"Struktur respons tidak dikenal: {response_json}")
                return "[ERROR]", "error_gerakan", False, False
            
            # Enhanced cleaning
            ai_output_cleaned = re.sub(r'[\x00-\x1F]+', '', ai_output)  # Hapus karakter kontrol
            ai_output_cleaned = re.sub(r'\\{', '{', ai_output_cleaned)  # Hapus escape characters
            ai_output_cleaned = re.sub(r'\\}', '}', ai_output_cleaned)
            ai_output_cleaned = ai_output_cleaned.replace("'", '"')  # Ganti kutip tunggal dengan ganda
            ai_output_cleaned = ai_output_cleaned.strip()  # Hapus spasi di awal/akhir
            
            # Enhanced JSON validation
            try:
                # Cari JSON di dalam string menggunakan regex
                json_match = re.search(r'\{.*\}', ai_output_cleaned, re.DOTALL)
                if json_match:
                    ai_data = json.loads(json_match.group())
                    
                    # Validasi field wajib
                    if "movement" not in ai_data or "response" not in ai_data:
                        raise ValueError("Field wajib tidak ditemukan")
                    
                    response_text = ai_data["response"]
                    movement_command = ai_data["movement"]  
                    in_standby = ai_data.get("in_standby", False) # ke mode stanbay
                    end_session = ai_data.get("end_session", False) # akhiri sesi

                    # Jika sudah valid, keluar dari loop
                    history.append({"role": "assistant", "content": json.dumps(ai_data)})
                    return response_text, movement_command, in_standby, end_session
                
                else:
                    raise ValueError("Format JSON tidak ditemukan")
            
            except ValueError as e:
                print("\nRespon AI salah request ulang jawaban dengan format JSON yang benar")
                print(f"⚠️ DETAIL ERROR JSON: {e}")
                print(f"⚠️ RAW AI OUTPUT: {ai_output}")
                print(f"⚠️ CLEANED OUTPUT: {ai_output_cleaned}")

                # Kirim ulang permintaan dengan pesan perbaikan
                data["messages"].append({
                    "role": "system",
                    "content": "Jawaban yang kamu berikan tidak dalam format JSON yang benar. "
                               "Ulangi jawaban dengan format JSON yang benar!"
                })
                continue  # Ulangi loop untuk meminta ulang ke AI
        
        except Exception as e:
            print(f"\n❌ API ERROR TRACEBACK ❌")
            print(f"Response JSON: {response.json() if response else 'No response'}")
            return "[ERROR]", "error_gerakan", False, False  # Tambahkan nilai ke-4
#----------------------------------------------------------------------------------------
def pilih_microphone():
    mic_list = sr.Microphone.list_microphone_names()
    
    # Filter untuk membedakan mic dan speaker
    filtered_mics = []
    for index, name in enumerate(mic_list):
        # Cek apakah perangkat adalah input (mic)
        is_input = True
        # Exclude perangkat output berdasarkan keyword
        excluded_keywords = ['speaker', 'output', 'playback', 'snd', 'default']
        if any(kw in name.lower() for kw in excluded_keywords):
            is_input = False
        
        if is_input:
            filtered_mics.append((index, name))

    print("\nPemilihan microphone otomatis:")
    
    # Prioritas 1: Cari external mic
    for index, name in filtered_mics:
        if 'external' in name.lower() or 'usb' in name.lower() or 'headset' in name.lower():
            print(f"→ Memilih microphone eksternal: {name}")
            return index
    
    # Prioritas 2: Mic built-in laptop
    for index, name in filtered_mics:
        if 'built-in' in name.lower() or 'internal' in name.lower():
            print(f"→ Memilih microphone bawaan: {name}")
            return index
    
    # Prioritas 3: Ambil yang pertama
    if filtered_mics:
        print(f"→ Memilih microphone default: {filtered_mics[0][1]}")
        return filtered_mics[0][0]
    
    # 🔥 Prioritaskan mic dengan input jelas
    for index, name in filtered_mics:
        if 'array' in name.lower() or 'stereo mix' in name.lower():
            print(f"→ Memilih mic dengan input jelas: {name}")
            return index
    
    raise Exception("Tidak ada microphone input yang terdeteksi")
#----------------------------------------------------------------------------------------
def is_wake_word(text):
    return any(difflib.get_close_matches(text.lower(), wake_words, n=1, cutoff=0.7))
#----------------------------------------------------------------------------------------
def amplify_audio(audio_data, factor=2.0):
    """
    Meningkatkan volume audio dengan faktor tertentu.
    Default: 2.0 (meningkatkan 2x lipat)
    """
    raw_data = audio_data.get_raw_data()
    amplified_audio = audioop.mul(raw_data, 2, factor)  # Perbesar amplitudo
    return sr.AudioData(amplified_audio, audio_data.sample_rate, audio_data.sample_width)

def reduce_noise(audio_data):
    raw_audio = np.frombuffer(audio_data.frame_data, dtype=np.int16)
    reduced_audio = nr.reduce_noise(y=raw_audio, sr=44100)  # Samakan sample rate dengan mic
    return sr.AudioData(reduced_audio.tobytes(), sample_rate=44100, sample_width=2) 

def play_audio(audio_data):
    with wave.open("temp_audio.wav", "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(44100)
        wf.writeframes(audio_data.get_wav_data())
    
    # Memutar audio
    chunk = 1024
    wf = wave.open("temp_audio.wav", "rb")
    pa = pyaudio.PyAudio()
    stream = pa.open(format=pa.get_format_from_width(wf.getsampwidth()),
                     channels=wf.getnchannels(),
                     rate=wf.getframerate(),
                     output=True)
    data = wf.readframes(chunk)
    while data:
        stream.write(data)
        data = wf.readframes(chunk)
    stream.stop_stream()
    stream.close()
    pa.terminate()

def is_human_voice(audio_data, recognizer):
    """
    Mengecek apakah audio mengandung suara manusia atau hanya kebisingan.
    """
    try:
        text = recognizer.recognize_google(audio_data, language="id-ID")
        return True if text.strip() else False  # Jika ada teks hasil transkripsi, berarti suara manusia
    except sr.UnknownValueError:
        return False  # Tidak ada suara manusia yang dikenali
    except sr.RequestError:
        print("⚠️ Kesalahan koneksi ke layanan pengenalan suara.")
        return False    

def main():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False  # Non-otomatis
    recognizer.energy_threshold = 500 # Ambang batas energi suara
    recognizer.pause_threshold = 0.8 # Waktu tunggu setelah suara berhenti

    putar_audio = False  # Ganti ke True untuk memainkan audio sebelum pengenalan suara

    in_standby = True # Mode standby awal
    
    # Inisialisasi koneksi robot
    if not init_robot_connection():
        print("⚠️ Mode simulasi tanpa robot")

    # Pilih microphone
    try:
        mic_index = pilih_microphone()
        mic = sr.Microphone(device_index=mic_index)
    except Exception as e:
        print(f"Error: {e}, menggunakan microphone default")
        mic = sr.Microphone()

    with mic as source:
        print("Menyesuaikan noise lingkungan... Mohon tunggu sebentar.")
        recognizer.adjust_for_ambient_noise(source, duration=2) # mengatus noise lingkungan
    
    print(f"Siap! Menggunakan microphone: {sr.Microphone.list_microphone_names()[mic_index]}")    
    
    # Pilih mode TTS
    print("\nPilih Text-to-Speech Engine:")
    print("1. ElevenLabs (Online - Kualitas Premium)")
    print("2. FGTTs (Offline - Default Indonesia)")
    tts_choice = input("Masukkan pilihan (1/2): ").strip()
    
    tts_mode = 'elevenlabs' if tts_choice == '1' else 'fgtts'
    print(f"\nMode TTS dipilih: {'ElevenLabs' if tts_mode == 'elevenlabs' else 'FGTTs Offline'}")    

    while True:
        if in_standby:
            print("\n🔴 Mode standby - Panggil 'Ruskomponen'...")
            try:
                with sr.Microphone(device_index=mic_index) as source:
                    audio = recognizer.listen(source, phrase_time_limit=3)
                    
                    if is_human_voice(audio, recognizer):
                        audio = amplify_audio(audio, factor=2.0)
                        audio = reduce_noise(audio)
                        if putar_audio:
                            print("\n🔊 Memutar ulang suara...")
                            play_audio(audio)
                        text = recognizer.recognize_google(audio, language="id-ID")
                        print("🔥 Wake word: Ruskomponen")
                        del audio

                        if is_wake_word(text):
                            bicara("Ya saya disini", elevenlabs_api_key, voice_id, ["siap"], tts_mode)
                            in_standby = False
                    else:
                        print("⚠️ Suara tidak dikenali sebagai manusia, mengabaikan...")
            except:
                continue
        else:
            try:
                print("\n🟢 Mode aktif - Mendengarkan...")
                with sr.Microphone(device_index=mic_index) as source:
                    audio = recognizer.listen(source, phrase_time_limit=5)
                    if is_human_voice(audio, recognizer):
                        audio = amplify_audio(audio, factor=2.0)
                        audio = reduce_noise(audio)
                        if putar_audio:
                            print("\n🔊 Memutar ulang suara...")
                            play_audio(audio)
                        text = recognizer.recognize_google(audio, language="id-ID")
                        print("\n✅ Perintah terdeteksi:", text)
                        del audio
                        
                        response, movements, in_standby, end_session = chat_ai(text, chat_api_key, history)
                        print("\n🧠 Respon AI:", response)
                        
                        bicara(response, elevenlabs_api_key, voice_id, movements, tts_mode)
                        
                        if end_session:
                            print("\n❌ Sesi diakhiri...")
                            break
                    else:
                        print("⚠️ Suara tidak dikenali sebagai manusia, mengabaikan...")
            except sr.UnknownValueError:
                print("\n🔇 Suara tidak jelas - Tetap aktif tanpa respon")
            except sr.WaitTimeoutError:
                pass
            except Exception as e:
                print(f"⚠️ Error: {e}")
                continue


    # Tutup koneksi saat program selesai
    global ser
    if ser and ser.is_open:
        ser.close()

#----------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
