# Library
import paho.mqtt.client as mqtt
import datetime
import time
import os
from tabulate import tabulate

# Function untuk publish data
def publishBojong(nama, berat, jenis_paket, jenisPaketWaktu):
    broker_address = 'test.mosquitto.org'
    client = mqtt.Client('Bojong', clean_session=False)
    client.connect(broker_address, port=1883)
    
    client.loop_start()
    print('Publish data to subscriber.')

    beratLaundry = float(berat)
    beratKg = str(berat) + ' Kg'
    if jenis_paket == 'Standar':
        if(jenisPaketWaktu == 'Ekonomis'):
            int_harga = int(beratLaundry * 5000)
            str_harga = str(int_harga)
        elif(jenisPaketWaktu == 'Reguler'):
            int_harga = int(beratLaundry * 5000 + 1000)
            str_harga = str(beratLaundry * 5000) + ' + 1000 = ' + str((int_harga))
        elif(jenisPaketWaktu == 'Express'):
            int_harga = int(beratLaundry * 5000 + 2000)
            str_harga = str(beratLaundry * 5000) + ' + 2000 = ' + str((int_harga))

    elif jenis_paket == 'Dry':
        if(jenisPaketWaktu == 'Ekonomis'):
            int_harga = int(beratLaundry * 7000)
            str_harga = str(int_harga)
        elif(jenisPaketWaktu == 'Reguler'):
            int_harga = int(beratLaundry * 7000 + 1000)
            str_harga = str(beratLaundry * 7000) + ' + 1000 = ' + str((int_harga))
        elif(jenisPaketWaktu == 'Express'):
            int_harga = int(beratLaundry * 7000 + 2000)
            str_harga = str(beratLaundry * 7000) + ' + 2000 = ' + str((int_harga))

    elif jenis_paket == 'Premium':
        if(jenisPaketWaktu == 'Ekonomis'):
            int_harga = int(beratLaundry * 9000)
            str_harga = str(int_harga)
        elif(jenisPaketWaktu == 'Reguler'):
            int_harga = int(beratLaundry * 9000 + 1000)
            str_harga = str(beratLaundry * 9000) + ' + 1000 = ' + str((int_harga))
        elif(jenisPaketWaktu == 'Express'):
            int_harga = int(beratLaundry * 9000 + 2000)
            str_harga = str(beratLaundry * 9000) + ' + 2000 = ' + str((int_harga))
    
    waktu = datetime.datetime.now()
    waktuPengajuan = waktu.strftime("%d/%m/%Y %H:%M:%S")

    if jenisPaketWaktu == 'Ekonomis':
        plus_hours = waktu + \
            datetime.timedelta(days=3)
        Pengembalian_Cucian = str(plus_hours.strftime("%d/%m/%Y %H:%M:%S"))
    elif jenisPaketWaktu == 'Reguler':
        plus_hours = waktu + \
            datetime.timedelta(days=2)
        Pengembalian_Cucian = str(plus_hours.strftime("%d/%m/%Y %H:%M:%S"))
    elif jenisPaketWaktu == 'Express':
        plus_hours = waktu + \
            datetime.timedelta(days=1)
        Pengembalian_Cucian = str(plus_hours.strftime("%d/%m/%Y %H:%M:%S"))

    # Mempublish data ke client
    client.publish('laundry', ''+nama+'|'+waktuPengajuan+'|'+jenis_paket+'|'
    +jenisPaketWaktu +'|'+beratKg+'|'+Pengembalian_Cucian+'|'+str_harga+'', qos=1, retain=False)

    client.loop_stop()

def publishSoang(nama, berat, jenis_paket, jenisPaketWaktu):
    broker_address = 'test.mosquitto.org'
    client = mqtt.Client('Soang', clean_session=False)
    client.connect(broker_address, port=1883)
    
    client.loop_start()
    print('Publish data to subscriber.')

    beratLaundrySoang = float(berat)
    beratKg = str(berat) + ' Kg'
    if jenis_paket == 'Standar':
        if(jenisPaketWaktu == 'Ekonomis'):
            int_harga = int(beratLaundrySoang * 6000)
            str_hargaSoang = str(int_harga)
        elif(jenisPaketWaktu == 'Reguler'):
            int_harga = int(beratLaundrySoang * 6000 + 1000)
            str_hargaSoang = str(beratLaundrySoang * 6000) + ' + 1000 = ' + str((int_harga))
        elif(jenisPaketWaktu == 'Express'):
            int_harga = int(beratLaundrySoang * 6000 + 2000)
            str_hargaSoang = str(beratLaundrySoang * 6000) + ' + 2000 = ' + str((int_harga))

    elif jenis_paket == 'Dry':
        if(jenisPaketWaktu == 'Ekonomis'):
            int_harga = int(beratLaundrySoang * 8000)
            str_hargaSoang = str(int_harga)
        elif(jenisPaketWaktu == 'Reguler'):
            int_harga = int(beratLaundrySoang * 8000 + 1000)
            str_hargaSoang = str(beratLaundrySoang * 8000) + ' + 1000 = ' + str((int_harga))
        elif(jenisPaketWaktu == 'Express'):
            int_harga = int(beratLaundrySoang * 8000 + 2000)
            str_hargaSoang = str(beratLaundrySoang * 8000) + ' + 2000 = ' + str((int_harga))

    elif jenis_paket == 'Premium':
        if(jenisPaketWaktu == 'Ekonomis'):
            int_harga = int(beratLaundrySoang * 9000)
            str_hargaSoang = str(int_harga)
        elif(jenisPaketWaktu == 'Reguler'):
            int_harga = int(beratLaundrySoang * 9000 + 1000)
            str_hargaSoang = str(beratLaundrySoang * 9000) + ' + 1000 = ' + str((int_harga))
        elif(jenisPaketWaktu == 'Express'):
            int_harga = int(beratLaundrySoang * 9000 + 2000)
            str_hargaSoang = str(beratLaundrySoang * 9000) + ' + 2000 = ' + str((int_harga))
    
    waktu = datetime.datetime.now()
    waktuPengajuanSoang = waktu.strftime("%d/%m/%Y %H:%M:%S")

    if jenisPaketWaktu == 'Ekonomis':
        plus_hours = waktu + \
            datetime.timedelta(days=3)
        Pengembalian_CucianSoang = str(plus_hours.strftime("%d/%m/%Y %H:%M:%S"))
    elif jenisPaketWaktu == 'Reguler':
        plus_hours = waktu + \
            datetime.timedelta(days=2)
        Pengembalian_CucianSoang = str(plus_hours.strftime("%d/%m/%Y %H:%M:%S"))
    elif jenisPaketWaktu == 'Express':
        plus_hours = waktu + \
            datetime.timedelta(days=1)
        Pengembalian_CucianSoang = str(plus_hours.strftime("%d/%m/%Y %H:%M:%S"))

    # Mempublish data ke client
    client.publish('laundry', ''+nama+'|'+waktuPengajuanSoang+'|'+jenis_paket+'|'+jenisPaketWaktu 
    +'|'+beratKg+'|'+Pengembalian_CucianSoang+'|'+str_hargaSoang+'', qos=1, retain=False)

    client.loop_stop()

def perbandingan(nama, berat, jenis_paket, jenisPaketWaktu):
    broker_address = 'test.mosquitto.org'
    client = mqtt.Client('bandingwaktu', clean_session=False)
    client.connect(broker_address, port=1883)
    
    client.loop_start()
    print('Publish data to subscriber.')

    beratLaundry = float(berat)

    if jenis_paket == 'Standar':
        if(jenisPaketWaktu == 'Ekonomis'):
            int_harga = int(beratLaundry * 5000)
            str_harga = str(int_harga)
        elif(jenisPaketWaktu == 'Reguler'):
            int_harga = int(beratLaundry * 5000 + 1000)
            str_harga = str(beratLaundry * 5000) + ' + 1000 = ' + str((int_harga))
        elif(jenisPaketWaktu == 'Express'):
            int_harga = int(beratLaundry * 5000 + 2000)
            str_harga = str(beratLaundry * 5000) + ' + 2000 = ' + str((int_harga))

    elif jenis_paket == 'Dry':
        if(jenisPaketWaktu == 'Ekonomis'):
            int_harga = int(beratLaundry * 7000)
            str_harga = str(int_harga)
        elif(jenisPaketWaktu == 'Reguler'):
            int_harga = int(beratLaundry * 7000 + 1000)
            str_harga = str(beratLaundry * 7000) + ' + 1000 = ' + str((int_harga))
        elif(jenisPaketWaktu == 'Express'):
            int_harga = int(beratLaundry * 7000 + 2000)
            str_harga = str(beratLaundry * 7000) + ' + 2000 = ' + str((int_harga))

    elif jenis_paket == 'Premium':
        if(jenisPaketWaktu == 'Ekonomis'):
            int_harga = int(beratLaundry * 9000)
            str_harga = str(int_harga)
        elif(jenisPaketWaktu == 'Reguler'):
            int_harga = int(beratLaundry * 9000 + 1000)
            str_harga = str(beratLaundry * 9000) + ' + 1000 = ' + str((int_harga))
        elif(jenisPaketWaktu == 'Express'):
            int_harga = int(beratLaundry * 9000 + 2000)
            str_harga = str(beratLaundry * 9000) + ' + 2000 = ' + str((int_harga))
    
    waktu = datetime.datetime.now()
    waktuPengajuan = waktu.strftime("%d/%m/%Y %H:%M:%S")

    if jenisPaketWaktu == 'Ekonomis':
        plus_hours = waktu + \
            datetime.timedelta(days=3)
        Pengembalian_Cucian = str(plus_hours.strftime("%d/%m/%Y %H:%M:%S"))
    elif jenisPaketWaktu == 'Reguler':
        plus_hours = waktu + \
            datetime.timedelta(days=2)
        Pengembalian_Cucian = str(plus_hours.strftime("%d/%m/%Y %H:%M:%S"))
    elif jenisPaketWaktu == 'Express':
        plus_hours = waktu + \
            datetime.timedelta(days=1)
        Pengembalian_Cucian = str(plus_hours.strftime("%d/%m/%Y %H:%M:%S"))
    
    
    #LAUNDRY SOANG
    beratLaundry = float(berat)
    beratKg = str(berat) + ' Kg'
    if jenis_paket == 'Standar':
        if(jenisPaketWaktu == 'Ekonomis'):
            int_harga = int(beratLaundry * 6000)
            str_hargaSoang = str(int_harga)
        elif(jenisPaketWaktu == 'Reguler'):
            int_harga = int(beratLaundry * 6000 + 1000)
            str_hargaSoang = str(beratLaundry * 6000) + ' + 1000 = ' + str((int_harga))
        elif(jenisPaketWaktu == 'Express'):
            int_harga = int(beratLaundry * 6000 + 2000)
            str_hargaSoang = str(beratLaundry * 6000) + ' + 2000 = ' + str((int_harga))

    elif jenis_paket == 'Dry':
        if(jenisPaketWaktu == 'Ekonomis'):
            int_harga = int(beratLaundry * 8000)
            str_hargaSoang = str(int_harga)
        elif(jenisPaketWaktu == 'Reguler'):
            int_harga = int(beratLaundry * 8000 + 1000)
            str_hargaSoang = str(beratLaundry * 8000) + ' + 1000 = ' + str((int_harga))
        elif(jenisPaketWaktu == 'Express'):
            int_harga = int(beratLaundry * 8000 + 2000)
            str_hargaSoang = str(beratLaundry * 8000) + ' + 2000 = ' + str((int_harga))

    elif jenis_paket == 'Premium':
        if(jenisPaketWaktu == 'Ekonomis'):
            int_harga = int(beratLaundry * 9000)
            str_hargaSoang = str(int_harga)
        elif(jenisPaketWaktu == 'Reguler'):
            int_harga = int(beratLaundry * 9000 + 1000)
            str_hargaSoang = str(beratLaundry * 9000) + ' + 1000 = ' + str((int_harga))
        elif(jenisPaketWaktu == 'Express'):
            int_harga = int(beratLaundry * 9000 + 2000)
            str_hargaSoang = str(beratLaundry * 9000) + ' + 2000 = ' + str((int_harga))
    
    waktu = datetime.datetime.now()
    waktuPengajuan = waktu.strftime("%d/%m/%Y %H:%M:%S")

    if jenisPaketWaktu == 'Ekonomis':
        plus_hours = waktu + \
            datetime.timedelta(days=3)
        Pengembalian_CucianSoang = str(plus_hours.strftime("%d/%m/%Y %H:%M:%S"))
    elif jenisPaketWaktu == 'Reguler':
        plus_hours = waktu + \
            datetime.timedelta(days=2)
        Pengembalian_CucianSoang = str(plus_hours.strftime("%d/%m/%Y %H:%M:%S"))
    elif jenisPaketWaktu == 'Express':
        plus_hours = waktu + \
            datetime.timedelta(days=1)
        Pengembalian_CucianSoang = str(plus_hours.strftime("%d/%m/%Y %H:%M:%S"))

    client.publish('laundry', ''+'Laundry Bojong'+'|'+nama+'|'+waktuPengajuan+'|'+jenis_paket+'|'+jenisPaketWaktu 
    +'|'+beratKg+'|'+Pengembalian_Cucian+'|'+str_harga+'', qos=1, retain=False)
    client.publish('laundry', ''+'Laundry Soang'+'|'+nama+'|'+waktuPengajuan+'|'+jenis_paket+'|'+jenisPaketWaktu 
    +'|'+beratKg+'|'+Pengembalian_CucianSoang+'|'+str_hargaSoang+'', qos=1, retain=False)
    client.loop_stop()


def menu():
    status = True
    while status:
        print('+-------------------------------+')
        print("|      Publish TimetoWash       |")
        print(tabulate({'No': ['1','2','3','4'],
                        'Menu Laundry': ['Publish Laundry Bojong','Publish Laundry Soang','Perbandingan','Keluar']},
                        headers='keys',
                        tablefmt='grid'))
        
        pilihan = input("Masukan pilihan anda : ")
        
        if pilihan == "1":
            nama, berat, jenis_paket, jenisPaketWaktu = menuLaundry()
            publishBojong(nama, berat, jenis_paket, jenisPaketWaktu)

        elif pilihan == "2":
            nama, berat, jenis_paket, jenisPaketWaktu = menuLaundrySoang()
            publishSoang(nama, berat, jenis_paket, jenisPaketWaktu)

        elif pilihan == "3":
            nama, berat, jenis_paket, jenisPaketWaktu = menuLaundry()
            perbandingan(nama, berat, jenis_paket, jenisPaketWaktu)
        elif pilihan == "4":
            print("Anda keluar dari program")
            status = False
        else:
            print("Yang Anda masukan salah silahkan coba lagi")
            time.sleep(2)
            os.system('cls')
            menu()

def menuLaundry():
    status = True
    l = []
    while status:
        os.system('cls')
        print("+-----------------------------------------------------------------------+")
        print("|                        Pilihan Menu Laundry                           |")
        print(tabulate({'Paket Layanan': ['Paket Standar : Rp 5000,-/kg','Paket Dry    : Rp 7000,-/kg','Paket Premium: Rp 9000,-/kg'],
                        'Paket Waktu': ['Ekonomis (3 Hari Pengerjaan)','Reguler (2 Hari Pengerjaan) + Rp 1000,-','Express (1 Hari Pengerjaan) + Rp 2000,-']},
                        headers='keys',
                        tablefmt='grid'))

        nama = input('Nama Pelanggan: ')
        berat = input('Berat: ')
        Jenis_paket = input('Jenis Paket (Standar), (Dry), (Premium): ')
        jenisPaketWaktu = input('Jenis Paket Waktu (Ekonomis), (Reguler), (Express): ')
        
        if Jenis_paket == 'Standar':
            if jenisPaketWaktu == 'Ekonomis':
                l = [nama, berat, 'Standar', 'Ekonomis']
            elif jenisPaketWaktu == 'Reguler':
                l = [nama, berat, 'Standar', 'Reguler']
            elif jenisPaketWaktu == 'Express':
                l = [nama, berat, 'Standar', 'Express']
        elif Jenis_paket == 'Dry':
            if jenisPaketWaktu == 'Ekonomis':
                l = [nama, berat, 'Dry', 'Ekonomis']
            elif jenisPaketWaktu == 'Reguler':
                l = [nama, berat, 'Dry', 'Reguler']
            elif jenisPaketWaktu == 'Express':
                l = [nama, berat, 'Dry', 'Express']
        elif Jenis_paket == 'Premium':
            if jenisPaketWaktu == 'Ekonomis':
                l = [nama, berat, 'Premium', 'Ekonomis']
            elif jenisPaketWaktu == 'Reguler':
                l = [nama, berat, 'Premium', 'Reguler']
            elif jenisPaketWaktu == 'Express':
                l = [nama, berat, 'Premium', 'Express']
        else:
            print("Yang Anda masukan salah silahkan coba lagi")
            status = True
            time.sleep(2)
            os.system('cls')
            menu()
        return l

def menuLaundrySoang():
    status = True
    l = []
    while status:
        os.system('cls')
        print("+---------------------------------------------------+")
        print("|              Pilihan Menu Laundry                 |")
        print(tabulate({'Paket Layanan': ['Paket Standar : Rp 6000,-/kg','Paket Dry    : Rp 8000,-/kg','Paket Premium: Rp 9000,-/kg'],
                        'Paket Waktu': ['Ekonomis','Reguler + Rp 1000,-','Express + Rp 2000,-']},
                        headers='keys',
                        tablefmt='grid'))

        nama = input('Nama Pelanggan: ')
        berat = input('Berat: ')
        Jenis_paket = input('Jenis Paket (Standar), (Dry), (Premium): ')
        jenisPaketWaktu = input('Jenis Paket Waktu (Ekonomis), (Reguler), (Express): ')
        
        if Jenis_paket == 'Standar':
            if jenisPaketWaktu == 'Ekonomis':
                l = [nama, berat, 'Standar', 'Ekonomis']
            elif jenisPaketWaktu == 'Reguler':
                l = [nama, berat, 'Standar', 'Reguler']
            elif jenisPaketWaktu == 'Express':
                l = [nama, berat, 'Standar', 'Express']
        elif Jenis_paket == 'Dry':
            if jenisPaketWaktu == 'Ekonomis':
                l = [nama, berat, 'Dry', 'Ekonomis']
            elif jenisPaketWaktu == 'Reguler':
                l = [nama, berat, 'Dry', 'Reguler']
            elif jenisPaketWaktu == 'Express':
                l = [nama, berat, 'Dry', 'Express']
        elif Jenis_paket == 'Premium':
            if jenisPaketWaktu == 'Ekonomis':
                l = [nama, berat, 'Premium', 'Ekonomis']
            elif jenisPaketWaktu == 'Reguler':
                l = [nama, berat, 'Premium', 'Reguler']
            elif jenisPaketWaktu == 'Express':
                l = [nama, berat, 'Premium', 'Express']
        else:
            print("Yang Anda masukan salah silahkan coba lagi")
            status = True
            time.sleep(2)
            os.system('cls')
            menu()
        return l
os.system('cls')
menu()