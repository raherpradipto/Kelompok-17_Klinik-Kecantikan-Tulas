
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

def consultation():
    global price_concul
    global injamkonsul
    global media
    global indokter
    global durasi
    print("Berikut Daftar Jam Konsultasi :")
    jamkonsul = "1. 09.00 \n2. 11.00 \n3. 13.00"
    print(jamkonsul)
    injamkonsul = (input("Pilih Jam Konsultasi Yang Anda Inginkan :"))
    print("Berikut Daftar Dokter :")
    dokter = "1. Dr. Tazkiya Mutia Yogasani \n2. Dr. Sekar Salsabila Santosa \n3. Dr. Rahmat Herpradipto"
    print(dokter)
    indokter = (input("Pilih Dokter Yang Anda Inginkan :"))
    print("Berikut Daftar Media Konsultasi :")
    media = "1. Whatsapp \n2. Zoom Meeting {Rp 50.000,00}\n3. Google Meeting {Rp 50.000,00}\n4. Datang Langsung {Rp 50.000,00}"
    print(media)
    inmedia = (input("Pilih Media Yang Anda Inginkan :"))
    tagihan()

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
        tagihan()
    elif pilskincare == "2":
        tagihan()
    elif pilskincare == "3":
        tagihan()
    else:
        print("Invalid code \nSilahkan Masukkan Sesuai Pilihan Yang Ada!")
        skincare()

def haircare():
    global jml_haircare
    print("Berikut adalah pilihan Haircare \nSilahkan pilih yang anda inginkan")
    pilhaircare = input("1. Shampo {Rp 50.000,00}\n2. Conditioner {Rp 50.000,00}\n\t:")
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
    print("Pesanan Anda Telah Diterima \nMohon Konfirmasi kembali pesanan dan tagihan anda")
    if menu == "1":
        if intreatment == "1":
            if pilfacetreatment == "1":
                print("Pesanan anda berupa treatment Fruit Facial seharga Rp ",price_ff, "untuk",jml_custom,"orang \nDengan Total Tagihan = \tRp ", jml_custom * price_ff)
            elif pilfacetreatment == "2":
                print("Pesanan anda berupa treatment Anti Acne Facial seharga Rp ",price_af, "untuk",jml_custom,"orang \nDengan total Tagihan = \tRp ", jml_custom * price_af)
            else:
                print("Pesanan anda berupa treatment Moisturizing Facial seharga Rp ", price_mf, "untuk",jml_custom,"orang \nDengan total Tagihan = \tRp ", jml_custom * price_mf)
        elif intreatment == "2":
            if pilhairtreatment == "1":
                print("Pesanan anda berupa Medical Hair Treatment seharga Rp ", price_ht, "untuk", jml_custom, "orang \nDengan total Tagihan = \tRp ",jml_custom * price_ht)
            elif  pilhairtreatment == "2":
                print("Pesanan anda berupa Medical Hair Mask seharga Rp ", price_ht, "untuk", jml_custom, "orang \nDengan total Tagihan = \tRp ",jml_custom * price_ht)
            else:
                print("Pesanan anda berupa Waxing seharga Rp ", price_ht, "untuk", jml_custom, "orang \nDengan total Tagihan = \tRp ",jml_custom * price_ht)
        else:
            if pilbodytreatment == "1":
                print("Pesanan anda berpa Body Slimming Treatment seharga Rp ", price_bs, "untuk", jml_custom, "orang \nDengan total Tagihan = \tRp ",jml_custom * price_bs)
            elif pilbodytreatment == "2":
                print("Pesanan anda berpa Body Treatment seharga Rp ", price_tb, "untuk", jml_custom, "orang \nDengan total Tagihan = \tRp ",jml_custom * price_tb)
            else:
                print("Pesanan anda berpa Body Firming seharga Rp ", price_bf, "untuk", jml_custom, "orang \nDengan total Tagihan = \tRp ",jml_custom * price_bf)
    elif menu == "2":
        if injamkonsul == "1":
            if indokter == "1":
                if media == "1" or "2" or "3":
                    print("Anda memesan Konsultasi secara Online bersama Dr. Tazkiya pada jam 09:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * price_concul)
                else:
                    print("Anda memesan Konsultasi secara Langsung bersama Dr. Tazkiya pada jam 09:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * price_concul)
            elif indokter == "2":
                if media == "1" or "2" or "3":
                    print("Anda memesan Konsultasi secara Online bersama Dr. Sekar pada jam 09:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * price_concul)
                else:
                    print("Anda memesan Konsultasi secara Langsung bersama Dr. Sekar pada jam 09:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * price_concul)
            else:
                if media == "1" or "2" or "3":
                    print("Anda memesan Konsultasi secara Online bersama Dr. Rahmat pada jam 09:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * price_concul)
                else:
                    print("Anda memesan Konsultasi secara Langsung bersama Dr. Rahmat pada jam 09:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * price_concul)
       elif injamkonsul == "2":
            if indokter == "1":
                if media == "1" or "2" or "3":
                    print("Anda memesan Konsultasi secara Online bersama Dr. Tazkiya pada jam 11:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * price_concul)
                else:
                    print("Anda memesan Konsultasi secara Langsung bersama Dr. Tazkiya pada jam 11:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * price_concul)
            elif indokter == "2":
                if media == "1" or "2" or "3":
                    print("Anda memesan Konsultasi secara Online bersama Dr. Sekar pada jam 11:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * price_concul)
                else:
                    print("Anda memesan Konsultasi secara Langsung bersama Dr. Sekar pada jam 11:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * price_concul)
            else:
                if media == "1" or "2" or "3":
                    print("Anda memesan Konsultasi secara Online bersama Dr. Rahmat pada jam 11:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * price_concul)
                else:
                    print("Anda memesan Konsultasi secara Langsung bersama Dr. Rahmat pada jam 11:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * price_concul)
       else:
           if indokter == "1":
                if media == "1" or "2" or "3":
                    print("Anda memesan Konsultasi secara Online bersama Dr. Tazkiya pada jam 13:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * price_concul)
                else:
                    print("Anda memesan Konsultasi secara Langsung bersama Dr. Tazkiya pada jam 13:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * price_concul)
            elif indokter == "2":
                if media == "1" or "2" or "3":
                    print("Anda memesan Konsultasi secara Online bersama Dr. Sekar pada jam 13:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * price_concul)
                else:
                    print("Anda memesan Konsultasi secara Langsung bersama Dr. Sekar pada jam 13:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * price_concul)
            else:
                if media == "1" or "2" or "3":
                    print("Anda memesan Konsultasi secara Online bersama Dr. Rahmat pada jam 13:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * price_concul)
                else:
                    print("Anda memesan Konsultasi secara Langsung bersama Dr. Rahmat pada jam 13:00, selama ",durasi," jam dengan total tagihan \t=Rp ",durasi * price_concul)
    elif menu == "3":
        if pilmedicine == "1":
            print("Anda memesan produk Skincare sebanyak ",jml_skincare," buah, seharga Rp ",price_medicine," \nDengan total Tagihan = Rp ",jml_skincare * price_medicine)
        else:
            print("Anda memesan produk Haircare sebanyak ",jml_haircare," buah, seharga Rp ",price_medicine," \nDengan total Tagihan = Rp ",jml_haircare * price_medicine)
    else:
        pass
    
def payment():
    print("Berikut adalah pilihan Payment \nSilahkan pilih yang anda inginkan")
    pilpayment= input("1. Transfer Bank \n2. Ovo \n3. Dana \n\t:")
    if pilpayment == "1":
        transferbank()
    elif pilpayment == "2":
        referencenumber()
    elif pilpayment == "3":
        referencenumber()
    else:
        print("Invalid code \nSilahkan Masukkan Sesuai Pilihan Yang Ada!")
        payment()
        
def transferbank():
    print("Berikut adalah pilihan Transfer Bank \nSilahkan pilih yang anda inginkan")
    piltfbank = input("1. BRI \n2. MANDIRI \n3. BNI \n\t:")
    if piltfbank == "1":
        referencenumber()
    elif piltfbank == "2":
        referencenumber()
    elif piltfbank == "3":
        referencenumber()
    else:
        print("Invalid code \nSilahkan Masukkan Sesuai Pilihan Yang Ada!")
        transferbank()

def referencenumber():
    noreference = input("Silahkan masukkan nomor referensi anda:")
    pass

def mulai():
    print("Selamat Datang di Aplikasi Klinik Tulas \nDapatkan Apa Yang Anda Inginkan",
          "==="*12,"\nSilahkan pilih layanan yang tersedia \n1. Treatment \n2. Consultation \n3. Buy Medicine \n4. Cancel")
    menu = input("Silahkan pilih jenis produk yang anda inginkan\t:")
    if menu == "1":
        treatment()
    elif menu == "2":
        consultation()
    elif menu == "3":
        buymedicine()
    elif menu == "4":
        cancel()
    else:
        print("Invalid code")
    mulai()

def SignUp():
    username = input(str("Input Username Anda\t:"))
    password = input(str("Input Password Anda\t:"))
    cpassword = input(str("Masukkan ulang Password anda\t:"))
    if password == cpassword:
        pass
    else:
        print("Password anda tidak sesuai")
    NoWhatsApp = int(input("Input Nomor WhatsApp Anda\t:"))
    email = input(str("Input Alamat Email Anda\t:"))
    noverif = input("Silahkan Input Nomor Verifikasi Yang Sudah Dikirimkan\t:")
    print("Selamat Anda Telah Terdaftar Sebagai Member Klinik Tulas ")
    member_number = print("Berikut Nomor Member Anda : ", NoWhatsApp)
    mulai()

def Login():
    usernamelogin = input("Input Username Anda\t:")
    passwordlogin = input("Input Password Anda\t:")
    memberlogin = input("Input Nomor Member Anda\t:")
    print("Login Success")
    mulai()

def start():
    global registrasi
    print("Selamat Datang di Program Registrasi Klinik Tulas")
    print("===" * 12)
    print("Silahkan Lakukan Registrasi Dibawah Ini:")
    registrasi = input("Silahkan Pilih Langkah yang Akan Anda Lakukan \n1. Sign Up \n2. Login\t\n>")

start()

if registrasi == "1":
    SignUp()
elif registrasi == "2":
    Login()
else:
    print("Invalid Kode")
