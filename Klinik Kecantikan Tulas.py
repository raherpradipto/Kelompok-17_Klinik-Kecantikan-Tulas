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
        print("Silahkan pilih jenis berikut: ")
        bodyslimming()
    elif pilbodytreatment == "2":
        print("Silahkan pilih jenis berikut: ")
        treatmentbody()
    elif pilbodytreatment == "3":
        print("Silahkan pilih jenis berikut: ")
        inputcustjam()
    else:
        print("Invalid code \nSilahkan Masukkan Sesuai Pilihan Yang Ada!")
        bodytreatment()

def bodyslimming():
    global price_bs
    global pilbodyslim
    print("Berikut adalah pilihan Body Slimming \nSilahkan pilih yang anda inginkan")
    pilbodyslim = input("1. Meso Body Perut {Rp 360.000,00}\n2. Meso Body Paha {Rp 360.000,00}\n3. Meso Body Lengan {Rp 360.000,00}\n\t:")
    price_bs = 360000
    if pilbodyslim == "1":
        inputcustjam()
    elif pilbodyslim == "2":
        inputcustjam()
    elif pilbodyslim == "3":
        inputcustjam()
    else:
        print("Invalid code \nSilahkan Masukkan Sesuai Pilihan Yang Ada!")
        bodyslimming()

def treatmentbody():
    global price_tb
    print("Berikut adalah pilihan Perawatan Tubuh \nSilahkan pilih yang anda inginkan")
    pilbodytreat = input("1. Refreshing Body Spa {Rp 330.000,00}\n2. Antioxidan Spa {Rp 330.000,00}\n3. Brightening Spa {Rp 330.000,00}\n\t:")
    price_tb = 330000
    if pilbodytreat == "1":
        inputcustjam()
    elif pilbodytreat == "2":
        inputcustjam()
    elif pilbodytreat == "3":
        inputcustjam()
    else:
        print("Invalid code \nSilahkan Masukkan Sesuai Pilihan Yang Ada!")
        treatmentbody()

def inputcustjam():
    global jml_custom
    global jam_treatment
    global sekaliguskonsul
    jml_custom = int(input("Input Jumlah Customer \n>"))
    print("Pilih Jam yang Anda Inginkan untuk Treatment : \n1. 08.00 \n2. 10.00 \n3. 13.00")
    jam_treatment = input(">")
    sekaliguskonsul = (input("Apakah Anda Ingin Sekaligus Konsultasi ? \n1. YA \n2. TIDAK \n>"))
    print(sekaliguskonsul)
    if sekaliguskonsul == "1" :
        consultation(sekaliguskonsul)
    elif sekaliguskonsul == "2" :
        tagihan(sekaliguskonsul)
    else:
        print("error detected ! pilih option yang telah diberikan !")
        inputcustjam()

def consultation(tambah):
    global harga_consul
    global injamkonsul
    global media
    global indokter
    global durasi
    print("Berikut Daftar Jam Konsultasi :")
    jamkonsul = "1. 09.00 \n2. 11.00 \n3. 13.00"
    print(jamkonsul)
    injamkonsul = (input("Pilih Jam Konsultasi Yang Anda Inginkan :"))
    durasi = int(input("Tentukan Berapa lama konsultasi anda (dalam jam)\t:"))
    print("Berikut Daftar Dokter :")
    dokter = "1. Dr. Tazkiya Mutia Yogasani \n2. Dr. Sekar Salsabila Santosa \n3. Dr. Rahmat Herpradipto"
    print(dokter)
    indokter = (input("Pilih Dokter Yang Anda Inginkan :"))
    print("Berikut Daftar Media Konsultasi :")
    media = "1. Whatsapp {Rp 50.000,00} \n2. Zoom Meeting {Rp 50.000,00}\n3. Google Meeting {Rp 50.000,00}\n4. Datang Langsung {Rp 50.000,00}"
    print(media)
    inmedia = (input("Pilih Media Yang Anda Inginkan :"))
    harga_consul = 50000
    if tambah == '1':
        tagihan('1')
    else :
        tagihan('3')

def buymedicine():
    global price_medicine
    global pilmedicine
    print("Berikut adalah beberapa medicine yang kami sediakan \nSilahkan pilih apa yang anda inginkan")
    pilmedicine = input("1. Skincare \n2. Haircare \n\t:")
    price_medicine = 50000
    if pilmedicine == "1":
        print("Silahkan pilih jenis berikut: ")
        skincare()
    elif pilmedicine == "2":
        print("Silahkan pilih jenis berikut: ")
        haircare()
    else:
        print("Invalid code \nSilahkan Input sesuai pilihan yang tersedia!")
        buymedicine()

def skincare():
    global jml_skincare
    print("Berikut adalah pilihan Skincare \nSilahkan pilih yang anda inginkan")
    pilskincare = input("1. Serum {Rp 50.000,00}\n2. Mask {Rp 50.000,00}\n3. Toner {Rp 50.000,00}\n\t:")
    if pilskincare == "1":
        jml_skincare = int(input("Masukkan Jumlah produk yang anda inginkan\t:"))
        tagihan('2')
    elif pilskincare == "2":
        jml_skincare = int(input("Masukkan Jumlah produk yang anda inginkan\t:"))
        tagihan('2')
    elif pilskincare == "3":
        jml_skincare = int(input("Masukkan Jumlah produk yang anda inginkan\t:"))
        tagihan('2')
    else:
        print("Invalid code \nSilahkan Masukkan Sesuai Pilihan Yang Ada!")
        skincare()

def haircare():
    global jml_haircare
    print("Berikut adalah pilihan Haircare \nSilahkan pilih yang anda inginkan")
    pilhaircare = input("1. Shampo {Rp 50.000,00}\n2. Conditioner {Rp 50.000,00}\n\t:")
    if pilhaircare == "1":
        jml_haircare = int(input("Masukkan Jumlah produk yang anda inginkan\t:"))
        tagihan()
    elif pilhaircare == "2":
        jml_haircare = int(input("Masukkan Jumlah produk yang anda inginkan\t:"))
        tagihan()
    else:
        print("Invalid code \nSilahkan Masukkan Sesuai Pilihan Yang Ada!")
        haircare()

def cancel():
    no_pesanan = input("Silahkan input nomor pesanan anda \t:")
    cekpesanan(no_pesanan)
    print("Anda akan menerima refund sebesar 70% dari yang anda bayarkan sebelumnya")
    make_sure  = input("Apakah anda yakin ingin membatalkan pesanan? \n1. YES \n2. NO \t:")
    if make_sure == "1":
        print("Pesanan anda telah dibatalkan \nAnda akan menerima refund sesuai dengan media pembayaran yang anda gunakan sebelumnya paling lambat 2 x 24 jam")
    else:
        print("Terima Kasih Telah Memilih Produk Kami")
    exit()


saat_ini = dtm.now()
sekarang = '{}'.format(dtm.strftime(saat_ini,'%d%Y%M'))
struk = ('''

=================================================

                STRUK

===================================================



Nomor pesanan anda \t : {}'''.format(dtm.strftime(saat_ini,'%d%Y%M'))
)

penutup = ("""
Pemesanan dilakukan pada {}""".format(dtm.strftime(saat_ini,'%d-%m-%Y %H:%M')))
tambahan = ("""

					TERIMA KASIH 
===================================================					
""")


def tagihan(sekaligus):
    print("Pesanan Anda Telah Diterima \nMohon Konfirmasi kembali pesanan dan tagihan anda")
    def tagihantunggal():
        if menu == "1":
            if intreatment == "1":
                if pilfacetreatment == "1":
                	print("Pesanan anda berupa treatment Fruit Facial seharga Rp ",price_ff, "untuk",jml_custom,"orang \nDengan Total Tagihan = \tRp ", jml_custom * price_ff)
                	pes = 'Pesanan anda berupa Fruit Facial '
                	total = jml_custom * price_ff
                elif pilfacetreatment == "2":
                    print("Pesanan anda berupa treatment Anti Acne Facial seharga Rp ",price_af, "untuk",jml_custom,"orang \nDengan total Tagihan = \tRp ", jml_custom * price_af)
                    pes = 'Pesanan anda berupa Anti Acne Facial '
                    total = jml_custom * price_af
                else:
                    print("Pesanan anda berupa treatment Moisturizing Facial seharga Rp ", price_mf, "untuk",jml_custom,"orang \nDengan total Tagihan = \tRp ", jml_custom * price_mf)
                    pes = 'Pesanan anda berupa Moisturizing Facial '
                    total = jml_custom * price_mf
            elif intreatment == "2":
                if pilhairtreatment == "1":
                    print("Pesanan anda berupa Medical Hair Treatment seharga Rp ", price_ht, "untuk", jml_custom, "orang \nDengan total Tagihan = \tRp ",jml_custom * price_ht)
                    pes = 'Pesanan anda berupa Medical Hair Treatment '
                    total = jml_custom * price_ht
                elif  pilhairtreatment == "2":
                    print("Pesanan anda berupa Medical Hair Mask seharga Rp ", price_ht, "untuk", jml_custom, "orang \nDengan total Tagihan = \tRp ",jml_custom * price_ht)
                    pes = 'Pesanan anda berupa Medical Hair Mask '
                    total = jml_custom * price_ht
                else:
                    print("Pesanan anda berupa Waxing seharga Rp ", price_ht, "untuk", jml_custom, "orang \nDengan total Tagihan = \tRp ",jml_custom * price_ht)
                    pes = 'Pesanan anda berupa Waxing '
                    total = jml_custom * price_ht
            else:
                if pilbodytreatment == "1":
                    print("Pesanan anda berpa Body Slimming Treatment seharga Rp ", price_bs, "untuk", jml_custom, "orang \nDengan total Tagihan = \tRp ",jml_custom * price_bs)
                    pes = 'Pesanan anda berupa Body Slimming Treatment '
                    total = jml_custom * price_bs
                elif pilbodytreatment == "2":
                    print("Pesanan anda berpa Body Treatment seharga Rp ", price_tb, "untuk", jml_custom, "orang \nDengan total Tagihan = \tRp ",jml_custom * price_tb)
                    pes = 'Pesanan anda berupa Body Treatment '
                    total = jml_custom * price_tb
                else:
                    print("Pesanan anda berpa Body Firming seharga Rp ", price_bf, "untuk", jml_custom, "orang \nDengan total Tagihan = \tRp ",jml_custom * price_bf)
                    pes = 'Pesanan anda berupa Body Firming '
                    total = jml_custom * price_bf
        elif menu == "2":
            if injamkonsul == "1":
                if indokter == "1":
                    if media == "1" or "2" or "3":
                        print("Anda memesan Konsultasi secara Online bersama Dr. Tazkiya pada jam 09:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * harga_consul)
                        pes = 'Pesanan anda berupa Konsultasi secara Online bersama Dr. Tazkiya pada jam 09:00, '
                        total = durasi * harga_consul
                    else:
                        print("Anda memesan Konsultasi secara Langsung bersama Dr. Tazkiya pada jam 09:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * harga_consul)
                        pes = 'Pesanan anda berupa Konsultasi secara Langsung bersama Dr. Tazkiya pada jam 09:00, '
                        total = durasi * harga_consul
                elif indokter == "2":
                    if media == "1" or "2" or "3":
                        print("Anda memesan Konsultasi secara Online bersama Dr. Sekar pada jam 09:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * harga_consul)
                        pes = 'Pesanan anda berupa Konsultasi secara Online bersama Dr. Sekar pada jam 09:00, '
                        total = durasi * harga_consul
                    else:
                        print("Anda memesan Konsultasi secara Langsung bersama Dr. Sekar pada jam 09:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * harga_consul)
                        pes = 'Pesanan anda berupa Konsultasi secara Langsung bersama Dr. Sekar pada jam 09:00, '
                        total = durasi * harga_consul
                else:
                    if media == "1" or "2" or "3":
                        print("Anda memesan Konsultasi secara Online bersama Dr. Rahmat pada jam 09:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * harga_consul)
                        pes = 'Pesanan anda berupa Konsultasi secara Online bersama Dr. Rahmat pada jam 09:00, '
                        total = durasi * harga_consul
                    else:
                        print("Anda memesan Konsultasi secara Langsung bersama Dr. Rahmat pada jam 09:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * harga_consul)
                        pes = 'Pesanan anda berupa Konsultasi secara Langsung bersama Dr. Rahmat pada jam 09:00, '
                        total = durasi * harga_consul
            elif injamkonsul == "2":
                if indokter == "1":
                    if media == "1" or "2" or "3":
                        print("Anda memesan Konsultasi secara Online bersama Dr. Tazkiya pada jam 11:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * harga_consul)
                        pes = 'Pesanan anda berupa Konsultasi secara Online bersama Dr. Tazkiya pada jam 11:00, '
                        total = durasi * harga_consul
                    else:
                        print("Anda memesan Konsultasi secara Langsung bersama Dr. Tazkiya pada jam 11:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * harga_consul)
                        pes = 'Pesanan anda berupa Konsultasi secara Langsung bersama Dr. Tazkiya pada jam 11:00, '
                        total = durasi * harga_consul
                elif indokter == "2":
                    if media == "1" or "2" or "3":
                        print("Anda memesan Konsultasi secara Online bersama Dr. Sekar pada jam 11:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * harga_consul)
                        pes = 'Pesanan anda berupa Konsultasi secara Online bersama Dr. Sekar pada jam 11:00, '
                        total = durasi * harga_consul
                    else:
                        print("Anda memesan Konsultasi secara Langsung bersama Dr. Sekar pada jam 11:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * harga_consul)
                        pes = 'Pesanan anda berupa Konsultasi secara Langsung bersama Dr. Sekar pada jam 11:00, '
                        total = durasi * harga_consul
                else:
                    if media == "1" or "2" or "3":
                        print("Anda memesan Konsultasi secara Online bersama Dr. Rahmat pada jam 11:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * harga_consul)
                        pes = 'Pesanan anda berupa Konsultasi secara Online bersama Dr. Rahmat pada jam 11:00, '
                        total = durasi * harga_consul
                    else:
                        print("Anda memesan Konsultasi secara Langsung bersama Dr. Rahmat pada jam 11:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * harga_consul)
                        pes = 'Pesanan anda berupa Konsultasi secara Langsung bersama Dr. Rahmat pada jam 11:00, '
                        total = durasi * harga_consul
            else:
                if indokter == "1":
                    if media == "1" or "2" or "3":
                        print("Anda memesan Konsultasi secara Online bersama Dr. Tazkiya pada jam 13:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * harga_consul)
                        pes = 'Pesanan anda berupa Konsultasi secara Online bersama Dr. Tazkiya pada jam 13:00, '
                        total = durasi * harga_consul
                    else:
                        print("Anda memesan Konsultasi secara Langsung bersama Dr. Tazkiya pada jam 13:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * harga_consul)
                        pes = 'Pesanan anda berupa Konsultasi secara Langsung bersama Dr. Tazkiya pada jam 13:00, '
                        total = durasi * harga_consul
                elif indokter == "2":
                    if media == "1" or "2" or "3":
                        print("Anda memesan Konsultasi secara Online bersama Dr. Sekar pada jam 13:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * harga_consul)
                        pes = 'Pesanan anda berupa Konsultasi secara Online bersama Dr. Sekar pada jam 13:00, '
                        total = durasi * harga_consul
                    else:
                        print("Anda memesan Konsultasi secara Langsung bersama Dr. Sekar pada jam 13:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * harga_consul)
                        pes = 'Pesanan anda berupa Konsultasi secara Langsung bersama Dr. Sekar pada jam 13:00, '
                        total = durasi * harga_consul
                else:
                   if media == "1" or "2" or "3":
                       print("Anda memesan Konsultasi secara Online bersama Dr. Rahmat pada jam 13:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * harga_consul)
                       pes = 'Pesanan anda berupa Konsultasi secara Online bersama Dr. Rahmat pada jam 13:00, '
                       total = durasi * harga_consul
                   else:
                       print("Anda memesan Konsultasi secara Langsung bersama Dr. Rahmat pada jam 13:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * harga_consul)
                       pes = 'Pesanan anda berupa Konsultasi secara Langsung bersama Dr. Rahmat pada jam 13:00, '
                       total = durasi * harga_consul
        elif menu == "3":
            if pilmedicine == "1":
                print("Anda memesan produk Skincare sebanyak ",jml_skincare," buah, seharga Rp ",price_medicine," \nDengan total Tagihan = Rp ",jml_skincare * price_medicine)
                pes = 'Pesanan anda berupa produk Skincare '
                total = jml_skincare * price_medicine
            else:
                print("Anda memesan produk Haircare sebanyak ",jml_haircare," buah, seharga Rp ",price_medicine," \nDengan total Tagihan = Rp ",jml_haircare * price_medicine)
                pes = 'Pesanan anda berupa produk Haircare '
                total = jml_haircare * price_medicine
        else:
            pass
        filename = open ('struk.txt', 'w')
        filename.write(struk)
        filename.write('\n' + penutup)
        if menu == "1":
            print('\n\n\n{}'.format(pes),'dengan jumlah customer (orang)', jml_custom,'\ndengan total tagihan :', total, file = filename)
        elif menu == "2" :
            print('\n\n\n{}'.format(pes), 'dengan durasi (jam) = ', durasi, '\ndengan total tagihan :', total, file=filename)
        else:
            if pilmedicine == "1" :
                print('\n\n\n{}'.format(pes), 'sebanyak', jml_skincare, 'buah \ndengan total tagihan :', total, file=filename)
            else:
                print('\n\n\n{}'.format(pes), 'sebanyak', jml_haircare, 'buah \ndengan total tagihan :', total, file=filename)
        filename.close()
        regispesanan(sekarang)
        payment()

    def tagihan_ganda():
        if intreatment == "1":
            if pilfacetreatment == "1":
                print("Pesanan anda berupa treatment Fruit Facial seharga Rp ", price_ff, "untuk", jml_custom,
                      "orang \ndengan harga = \tRp ", jml_custom * price_ff)
                print("Dengan tambahan pemesanan konsultasi selama ", durasi ,'jam, dengan harga = Rp ', durasi * harga_consul)
                print("Sehingga total tagihan anda sebesar = Rp ", (jml_custom * price_ff) + (durasi * harga_consul))
                pesproduk = "Pesanan anda berupa treatment Fruit Facial "
                harproduk = jml_custom * price_ff
                pesconsul = "Dengan tambahan pemesanan konsultasi "
                harconsul = durasi * harga_consul
                pestotal = "Total tagihan anda sebesar = Rp "
                hartotal = harconsul + harproduk
            elif pilfacetreatment == "2":
                print("Pesanan anda berupa treatment Anti Acne Facial seharga Rp ", price_af, "untuk", jml_custom,
                      "orang \nDengan total Tagihan = \tRp ", jml_custom * price_af)
                print("Dengan tambahan pemesanan konsultasi selama ", durasi, 'jam, dengan harga = Rp ',
                      durasi * harga_consul)
                print("Sehingga total tagihan anda sebesar = Rp ", (jml_custom * price_af) + (durasi * harga_consul))
                pesproduk = "Pesanan anda berupa treatment Anti Acne Facial "
                harproduk = jml_custom * price_af
                pesconsul = "Dengan tambahan pemesanan konsultasi "
                harconsul = durasi * harga_consul
                pestotal = "Total tagihan anda sebesar = Rp "
                hartotal = harconsul + harproduk
            else:
                print("Pesanan anda berupa treatment Moisturizing Facial seharga Rp ", price_mf, "untuk", jml_custom,
                      "orang \nDengan total Tagihan = \tRp ", jml_custom * price_mf)
                print("Dengan tambahan pemesanan konsultasi selama ", durasi, 'jam, dengan harga = Rp ',
                      durasi * harga_consul)
                print("Sehingga total tagihan anda sebesar = Rp ", (jml_custom * price_mf) + (durasi * harga_consul))
                pesproduk = "Pesanan anda berupa treatment Moisturizing Facial "
                harproduk = jml_custom * price_mf
                pesconsul = "Dengan tambahan pemesanan konsultasi "
                harconsul = durasi * harga_consul
                pestotal = "Total tagihan anda sebesar = Rp "
                hartotal = harconsul + harproduk
        elif intreatment == "2":
            if pilhairtreatment == "1":
                print("Pesanan anda berupa Medical Hair Treatment seharga Rp ", price_ht, "untuk", jml_custom,
                      "orang \nDengan total Tagihan = \tRp ", jml_custom * price_ht)
                print("Dengan tambahan pemesanan konsultasi selama ", durasi, 'jam, dengan harga = Rp ',
                      durasi * harga_consul)
                print("Sehingga total tagihan anda sebesar = Rp ", (jml_custom * price_ht) + (durasi * harga_consul))
                pesproduk = "Pesanan anda berupa Medical Hair Treatment untuk "
                harproduk = jml_custom * price_ht
                pesconsul = "Dengan tambahan pemesanan konsultasi "
                harconsul = durasi * harga_consul
                pestotal = "Total tagihan anda sebesar = Rp "
                hartotal = harconsul + harproduk
            elif pilhairtreatment == "2":
                print("Pesanan anda berupa Medical Hair Mask seharga Rp ", price_ht, "untuk", jml_custom,
                      "orang \nDengan total Tagihan = \tRp ", jml_custom * price_ht)
                print("Dengan tambahan pemesanan konsultasi selama ", durasi, 'jam, dengan harga = Rp ',
                      durasi * harga_consul)
                print("Sehingga total tagihan anda sebesar = Rp ", (jml_custom * price_ht) + (durasi * harga_consul))
                pesproduk = "Pesanan anda berupa Medical Hair Mask "
                harproduk = jml_custom * price_ht
                pesconsul = "Dengan tambahan pemesanan konsultasi "
                harconsul = durasi * harga_consul
                pestotal = "Total tagihan anda sebesar = Rp "
                hartotal = harconsul + harproduk
            else:
                print("Pesanan anda berupa Waxing seharga Rp ", price_ht, "untuk", jml_custom,
                      "orang \nDengan total Tagihan = \tRp ", jml_custom * price_ht)
                print("Dengan tambahan pemesanan konsultasi selama ", durasi, 'jam, dengan harga = Rp ',
                      durasi * harga_consul)
                print("Sehingga total tagihan anda sebesar = Rp ", (jml_custom * price_ht) + (durasi * harga_consul))
                pesproduk = "Pesanan anda berupa Waxing untuk "
                harproduk = jml_custom * price_ht
                pesconsul = "Dengan tambahan pemesanan konsultasi "
                harconsul = durasi * harga_consul
                pestotal = "Total tagihan anda sebesar = Rp "
                hartotal = harconsul + harproduk
        else:
            if pilbodytreatment == "1":
                print("Pesanan anda berpa Body Slimming Treatment seharga Rp ", price_bs, "untuk", jml_custom,  
