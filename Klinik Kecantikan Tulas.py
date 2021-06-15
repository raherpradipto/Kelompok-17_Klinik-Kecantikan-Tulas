from datetime import datetime as dtm
import json


def create_json(file_name):
    with open(file_name, 'w') as json_file:
        json.dump([], json_file)


def read_json(file_name):
    with open(file_name, 'r') as json_file:
        database = json.load(json_file)
    return database

def write_json(file_name, database, username, password, nomember):
    account = {
        'username': username,
        'password': password,
        'nomor member': nomember
    }

    database.append(account)

    with open(file_name, 'w') as json_file:
        json.dump(database, json_file)


def awal_regis(username,password,no_member):
    if __name__ == '__main__':
        FILE_NAME = 'database user.json'

        try:
            database = read_json(FILE_NAME)
        except:
            create_json(FILE_NAME)
            database = read_json(FILE_NAME)

        USERNAME = username
        PASSWORD = password
        NOMEMBER = no_member

        write_json(FILE_NAME, database, USERNAME, PASSWORD, NOMEMBER)


def regispesanan(no_pesanan):
    if __name__ == '__main__':
        FILE_NAME = 'nomor pesanan.json'

        try:
            database = read_json(FILE_NAME)
        except:
            create_json(FILE_NAME)
            database = read_json(FILE_NAME)

        NO_PESANAN = no_pesanan

        write_pesanan(FILE_NAME, database, NO_PESANAN)


def write_pesanan(file_name, database, no_pesanan):
    account = {
        'nomor pesanan' : no_pesanan
    }

    database.append(account)

    with open(file_name, 'w') as json_file:
        json.dump(database, json_file)


def cekpesanan(no_pesanan):
    def checkpesanan(database, nomorpesanan):

        data = {
            'nomor pesanan' : nomorpesanan
        }

        if data in database:
        	pass
        else:
            print('Nomor pesanan tidak ditemukan')
            print('Masukkan nomor pesanan yang benar')
            cancel()
    if __name__ == '__main__':
        FILE_NAME = 'nomor pesanan.json'


        try:
            database = read_json(FILE_NAME)
        except:
            create_json(FILE_NAME)
            database = read_json(FILE_NAME)

        NOMORPESANAN = no_pesanan

        checkpesanan(database, NOMORPESANAN)


def treatment():
    global intreatment
    print("Berikut Jenis Treatment :")
    jenistreatment = "1. Face Treatment \n2. Hair Treatment \n3. Body Treatment"
    print(jenistreatment)
    intreatment = (input("Pilih Jenis Treatment Yang Anda Inginkan :"))
    if intreatment == "1" :
        facetreatment()
    elif intreatment == "2":
        hairtreatment()
    elif intreatment == "3":
        bodytreatment()
    else:
        print("Invaid code \nSilahkan input sesuai pilihan")
        mulai()


def facetreatment():
    global pilfacetreatment
    print("Berikut adalah pilihan Face Treatment \nSilahkan pilih yang anda inginkan")
    pilfacetreatment = input("1. Fruit Facial \n2. Anti Acne Facial \n3. Moisturizing Facial \n\t:")
    if pilfacetreatment == "1":
        print("Silahkan pilih jenis berikut: ")
        fruitfacial()
    elif pilfacetreatment == "2":
        print("Silahkan pilih jenis berikut: ")
        antiacnefacial()
    elif pilfacetreatment == "3":
        print("Silahkan pilih jenis berikut: ")
        moisturizingfacial()
    else:
        print("Invalid code \nSilahkan Masukkan Sesuai Pilihan Yang Ada!")
        facetreatment()

def fruitfacial():
    global price_ff
    print("Berikut adalah pilihan Fruit Facial \nSilahkan pilih yang anda inginkan")
    pilfruitfacial = input("1. Strawberry Exfoliating Facial {Rp 90.000,00} \n2. Blueberry Atioxidan Facial {Rp 90.000,00} \n3. Apple Purifying Facial {Rp 90.000,00} \n\t:")
    price_ff = 90000
    if pilfruitfacial == "1":
        inputcustjam()
    elif pilfruitfacial == "2":
        inputcustjam()
    elif pilfruitfacial == "3":
        inputcustjam()
    else:
        print("Invalid code \nSilahkan Masukkan Sesuai Pilihan Yang Ada!")
        fruitfacial()

def antiacnefacial():
    global price_af
    print("Berikut adalah pilihan Anti Acne Facial \nSilahkan pilih yang anda inginkan")
    pilantiacne = input("1. Bio Acne Light Teraphy {Rp 230.000,00}\n2. Bio Inflame Acne Teraphy {Rp 230.000,00}\n3. Microteraphy Acne Control {Rp 230.000,00}\n\t:")
    price_af = 230000
    if pilantiacne == "1":
        inputcustjam()
    elif pilantiacne == "2":
        inputcustjam()
    elif pilantiacne == "3":
        inputcustjam()
    else:
        print("Invalid code \nSilahkan Masukkan Sesuai Pilihan Yang Ada!")
        antiacnefacial()

def moisturizingfacial():
    global price_mf
    print("Berikut adalah pilihan Moisturizing Facial \nSilahkan pilih yang anda inginkan")
    pilmoist = input("1. Collagen Facial {Rp 135.000,00}\n2. Paraffin Facial {Rp 135.000,00}\n3. Honey Facial {Rp 135.000,00}\n\t:")
    price_mf = 135000
    if pilmoist == "1":
        inputcustjam()
    elif pilmoist == "2":
        inputcustjam()
    elif pilmoist == "3":
        inputcustjam()
    else:
        print("Invalid code \nSilahkan Masukkan Sesuai Pilihan Yang Ada!")
        moisturizingfacial()

def hairtreatment():
    global price_ht
    global pilhairtreatment
    print("Berikut adalah pilihan Hair Treatment \nSilahkan pilih yang anda inginkan")
    pilhairtreatment = input("1. Medical Hair Treatment {Rp 70.000,00}\n2. Medical Hair Mask {Rp 70.000,00}\n3. Waxing {Rp 70.000,00}\n\t:")
    price_ht = 70000
    if pilhairtreatment == "1":
        inputcustjam()
    elif pilhairtreatment == "2":
        inputcustjam()
    elif pilhairtreatment == "3":
        inputcustjam()
    else:
        print("Invalid code \nSilahkan Masukkan Sesuai Pilihan Yang Ada!")
        hairtreatment()

def bodytreatment():
    global pilbodytreatment
    global price_bf
    print("Berikut adalah pilihan Body Treatment \nSilahkan pilih yang anda inginkan")
    pilbodytreatment = input("1. Body Slimming \n2. Body Treatment \n3. Body Firming {Rp 360.000,00}")
    price_bf = 360000
    if pilbodytreatment == "1":
