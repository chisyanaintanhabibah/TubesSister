#Melakukan import library
import paho.mqtt.client as mqtt #implementasi protokol mqtt
import time #manajemen waktu
import os #operasi sistem
from IPython.display import clear_output #membersihkan output
from tabulate import tabulate #merapihkan table

#Function untuk menampilkan menu dalam tabel
def menu():
    print(tabulate({'No': ['1','2','3','4'],
                    'Menu Laundry': ['Subscribe Laundry Bojong','Subscribe Laundry Soang','Perbandingan','Keluar']},
                    headers='keys',
                    tablefmt='grid'))

#Function subscribe laundry bojong membuat koneksi ke broker mqtt dan akan menampilkan data laundrybojong
def laundryBojong(): 
    arrBojong = []
    def on_connect(client, userdata, flags, rc): #menampilkan pesan bahwa client terhubung atau gagal
        if rc == 0:
            print("Client is connected to Laundry Bojong")
        else:
            print("Connected Failed")
    def on_message(client, userdata, message): # # Mendekode pesan yang diterima dan memisahkan datanya
        data = str(message.payload.decode('utf-8')).split('|')
        arrBojong.append(data)  # Menambahkan data ke dalam list arrBanding
        clear_output(wait=True) #Membersihkan layar dan menampilkan tabel dengan data terkini
        os.system('cls')
        index = range(1, len(arrBojong)+1)
        print("Tagihan Laundry Bojong")
        print(tabulate(arrBojong, headers=['Nama', 'Tanggal Input', 'Jenis Layanan', 'Jenis Paket Waktu', 'Berat', 'Pengembalian Cucian', 
        'Total Harga'], tablefmt='pretty', showindex=index))
    broker_address = 'test.mosquitto.org' #broker mqtt
    # Membuat objek klien MQTT
    client = mqtt.Client('laundrybojong', clean_session=True)
    client.on_connect = on_connect
    client.on_message = on_message
    # Melakukan koneksi ke broker MQTT dan mulai loop
    client.connect(broker_address, port=1883)
    client.loop_start()
    # Melakukan subscribe ke topik 'laundry' dengan Quality of Service
    client.subscribe('laundry', qos=1)
    while True:
        time.sleep(1) #Memberi jeda selama 1 detik
    client.loop_stop()

def laundrySoang(): #Fungsi subscribe laundry soang
    arrSoang = []
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Client is connected to Laundry Soang")
        else:
            print("Connected Failed")
    def on_message(client, userdata, message):
        data = str(message.payload.decode('utf-8')).split('|')
        arrSoang.append(data)
        os.system('cls')
        clear_output(wait=True)
        index = range(len(arrSoang))
        print("Tagihan Laundry Soang")
        print(tabulate(arrSoang, headers=['Nama', 'Tanggal Input', 'Jenis Layanan', 'Jenis Paket Waktu', 'Berat', 'Pengembalian Cucian', 
        'Total Harga'], tablefmt='pretty', showindex=index))
    broker_address = 'test.mosquitto.org'
    client = mqtt.Client('laundrysoang', clean_session=True)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker_address, port=1883)
    client.loop_start()
    client.subscribe('laundry', qos=1)
    while True:
        time.sleep(1)
    client.loop_stop()

def perbandingan(): #Function untuk membandingkan informasi dari kedua laundry
    arrBanding = []
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Client is connected to Perbandingan Laundry")
        else:
            print("Connected Failed")
    def on_message(client, userdata, message):
        data = str(message.payload.decode('utf-8')).split('|')
        arrBanding.append(data)
        clear_output(wait=True)
        os.system('cls')
        index = range(len(arrBanding))
        print("Tagihan Data laundry Perbandingan")
        print(tabulate(arrBanding, headers=['Nama', 'Tanggal Input', 'Jenis Layanan', 'Jenis Paket Waktu', 'Berat', 'Pengembalian Cucian', 'Total Harga'], 
            tablefmt='pretty', showindex=index))
    broker_address = 'test.mosquitto.org'
    client = mqtt.Client('BandingWaktu', clean_session=True)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker_address, port=1883)
    client.loop_start()
    client.subscribe('laundry', qos=1)
    while True:
        time.sleep(1)
    client.loop_stop()

#Looping untuk melakukan pemilihan menu
os.system('cls')
menu()
status = True
while status:
    inputan = int(input('Masukan pilihan anda : '))
    if inputan == 1:
        laundryBojong()
    elif inputan == 2:
        laundrySoang()
    elif inputan == 3:
        perbandingan()
    elif inputan == 4:
        status = False
        print("Anda keluar dari program")
        exit()        
    else:
        print("Yang Anda masukan salah silahkan coba lagi")
        time.sleep(2)
        os.system('cls')
        menu()
        