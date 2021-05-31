
def treatment():
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
    print("Berikut adalah pilihan Fruit Facial \nSilahkan pilih yang anda inginkan")
    pilfruitfacial = input("1. Strawberry Exfoliating Facial \n2. Blueberry Atioxidan Facial \n3. Apple Purifying Facial \n\t:")
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
    print("Berikut adalah pilihan Anti Acne Facial \nSilahkan pilih yang anda inginkan")
    pilantiacne = input("1. Bio Acne Light Teraphy \n2. Bio Inflame Acne Teraphy \n3. Microteraphy Acne Control \n\t:")
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
    print("Berikut adalah pilihan Moisturizing Facial \nSilahkan pilih yang anda inginkan")
    pilmoist = input("1. Collagen Facial \n2. Paraffin Facial \n3. Honey Facial \n\t:")
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
    print("Berikut adalah pilihan Hair Treatment \nSilahkan pilih yang anda inginkan")
    pilhairtreatment = input("1. Medical Hair Treatment \n2. Medical Hair Mask \n3. Waxing \n\t:")
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
    print("Berikut adalah pilihan Body Treatment \nSilahkan pilih yang anda inginkan")
    pilbodytreatment = input("1. Body Slimming \n2. Body Treatment \n3. Body Firming")
    if pilbodytreatment == "1":
        print("Silahkan pilih jenis berikut: ")
        bodyslimming()
    elif pilbodytreatment == "2":
        print("Silahkan pilih jenis berikut: ")
        treatmentbody()
    elif pilbodytreatment == "3":
        print("Silahkan pilih jenis berikut: ")
        bodytreatment()
    else:
        print("Invalid code \nSilahkan Masukkan Sesuai Pilihan Yang Ada!")
        bodytreatment()

def bodyslimming():
    print("Berikut adalah pilihan Body Slimming \nSilahkan pilih yang anda inginkan")
    pilbodyslim = input("1. Meso Body Perut \n2. Meso Body Paha \n3. Meso Body Lengan \n\t:")
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
    print("Berikut adalah pilihan Perawatan Tubuh \nSilahkan pilih yang anda inginkan")
    pilbodytreat = input("1. Refreshing Body Spa \n2. Antioxidan Spa \n3. Brightening Spa \n\t:")
    if pilbodytreat == "1":
        inputcustjam()
    elif pilbodytreat == "2":
        inputcustjam()
    elif pilbodytreat == "3":
        inputcustjam()
    else:
        print("Invalid code \nSilahkan Masukkan Sesuai Pilihan Yang Ada!")
        treatmentbody()

def consultation():
    print("Berikut Daftar Jam Konsultasi :")
    jamkonsul = "1. 09.00 \n2. 11.00 \n3. 13.00"
    print(jamkonsul)
    injamkonsul = (input("Pilih Jam Konsultasi Yang Anda Inginkan :"))
    print("Berikut Daftar Dokter :")
    dokter = "1. Dr. Tazkiya Mutia Yogasani \n2. Dr. Sekar Salsabila Santosa \n3. Dr. Rahmat Herpradipto"
    print(dokter)
    indokter = (input("Pilih Dokter Yang Anda Inginkan :"))
    print("Berikut Daftar Media Konsultasi :")
    media = "1. Whatsapp \n2. Zoom Meeting \n3. Google Meeting \n4. Datang Langsung"
    print(media)
    inmedia = (input("Pilih Media Yang Anda Inginkan :"))
    tagihan()

def buymedicine():
    print("Berikut adalah beberapa medicine yang kami sediakan \nSilahkan pilih apa yang anda inginkan")
    pilmedicine = input("1. Skincare \n2. Haircare \n\t:")
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
    print("Berikut adalah pilihan Skincare \nSilahkan pilih yang anda inginkan")
    pilskincare = input("1. Serum \n2. Mask \n3. Toner \n\t:")
    if pilskincare == "1":
        tagihan()
    elif pilskincare == "2":
        tagihan()
    elif pilskincare == "3":
        tagihan()
    else:
        print("Invalid code \nSilahkan Masukkan Sesuai Pilihan Yang Ada!")
        skincare()

def haircare():
    print("Berikut adalah pilihan Haircare \nSilahkan pilih yang anda inginkan")
    pilhaircare = input("1. Shampo \n2. Conditioner \n\t:")
    if pilhaircare == "1":
        tagihan()
    elif pilhaircare == "2":
        tagihan()
    else:
        print("Invalid code \nSilahkan Masukkan Sesuai Pilihan Yang Ada!")
        haircare()

def cancel():
    no_pesanan = input("Silahkan input nomor pesanan anda \t:")
    print("Anda akan menerima refund sebesar 70% dari yang anda bayarkan sebelumnya")
    make_sure  = input("Apakah anda yakin ingin membatalkan pesanan? \n1. YES \n2. NO \t:")
    if make_sure == "1":
        print("Pesanan anda telah dibatalkan \nAnda akan menerima refund sesuai dengan media pembayaran yang anda gunakan sebelumnya paling lambat 2 x 24 jam")
    else:
        print("Terima Kasih Telah Memilih Produk Kami")

def inputcustjam():
    print(input("Input Jumlah Customer \n>"))
    print("Pilih Jam yang Anda Inginkan untuk Treatment : \n1. 08.00 \n2. 10.00 \n3. 13.00")
    print(input(">"))
    sekaliguskonsul = (input("Apakah Anda Ingin Sekaligus Konsultasi ? \n1. YA \n2. TIDAK \n>"))
    print(sekaliguskonsul)
    if sekaliguskonsul == 1 :
        consultation()
    else:
        tagihan()

def tagihan():
    print("......")
    breakpoint()
