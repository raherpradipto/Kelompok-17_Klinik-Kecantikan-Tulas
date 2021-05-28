# Kelompok-17_Klinik-Kecantikan-Tulas
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
