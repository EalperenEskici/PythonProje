import time

icecekler = ['1-Kahve','2-Çay','3-Ice-Latte','4-Su']
fiyatListe = [10,5,20,3]
miktar = 0
def paraYukleme(miktar):
    paraMiktar = int(input("Kartınıza ne kadar para yüklemek istersiniz--->>>     "))
    miktar += paraMiktar
    return miktar

def bakiyeGöster(bakiye):
    print("{} kadar paranız mevcut. İyi harcamalar  ^^   ".format(bakiye))

while True:
    print("""   
          Kafemize Hoşgeldiniz.
          1-Karta para yükleme
          2-İçecekler seçeneklerini görme
          3-Bakiye Göster
          4-Çıkış             
                    """)
    secim = input("Hangi işlemi yapmak istersiniz--->>>    ")
    if secim == '1':
        miktar = paraYukleme(miktar)
        print("Kartınıza {} kadar para yüklenmiştir. İyi harcamalar  ^^  ".format(miktar))
        input("Devam etmek için enter'a basınız... ")
    elif secim == '2':
        for i in icecekler:
            print(i , end= ' ' )

        kahveSecim = input("\nHangi içeceği istersiniz--->>> ")
        if kahveSecim == '1':
            kahveSecim = fiyatListe[0]
            if kahveSecim > miktar:
                print("Bakiyeniz Yetersiz lütfen para yükleyip tekrar deneyiniz !!! ")
            elif kahveSecim <= miktar:
                print("Kahveniz hazırlanıyor lütfen bekleyiniz  ^^  ")
                miktar -= fiyatListe[0]
                time.sleep(1.5)
                print("Kahveniz hazırdır. Afiyet olsun   ^.^   ")
        elif kahveSecim == '2':
            kahveSecim = fiyatListe[1]
            if kahveSecim > miktar:
                print("Bakiyeniz Yetersiz lütfen para yükleyip tekrar deneyiniz !!! ")
            elif kahveSecim <=miktar :
                print("{}ınız hazırlanıyor lütfen bekleyiniz  ^^  ".format(icecekler[1]))
                miktar -= fiyatListe[1]
                time.sleep(1.5)
                print("Çayınız hazırdır. Afiyet olsun  ^.^  ")
        elif kahveSecim == '3':
            kahveSecim = fiyatListe[2]
            if kahveSecim > miktar:
                print("Bakiyeniz Yetersiz lütfen para yükleyip tekrar deneyiniz !!! ")
            elif kahveSecim <=miktar :
                print("{}ınız hazırlanıyor lütfen bekleyiniz  ^^  ".format(icecekler[2]))
                miktar -= fiyatListe[2]
                time.sleep(1.5)
                print("Ice-Latte'niz hazırdır. Afiyet olsun  ^.^  ")
        elif kahveSecim == '4':
            kahveSecim = fiyatListe[3]
            if kahveSecim > miktar:
                print("Bakiyeniz Yetersiz lütfen para yükleyip tekrar deneyiniz !!! ")
            elif kahveSecim <=miktar :
                print("{}ınız hazırlanıyor lütfen bekleyiniz  ^^  ".format(icecekler[3]))
                miktar -= fiyatListe[3]
                time.sleep(1.5)
                print("Su hazırdır. Afiyet olsun  ^.^  ")
        else:
            print("Menümüzde olmayan seçeneği seçtiniz. Lütfen tekrar deneyiniz.")

        input("\nDevam etmek için enter'a basınız... ")


    elif secim == '3':
        bakiyeGöster(miktar)
        input("Devam etmek için enter'a basınız... ")

    elif secim == '4':
        print("Tekrar bekleriz. İyi günler  \n<*<*<*<**>*>*>*> ")
        break

    else:
        print("Yanlış işlem girdiniz Lütfen tekrar deneyiniz...")

