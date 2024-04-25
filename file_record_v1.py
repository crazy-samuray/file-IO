






dosya_yolu = "kayitlar.txt"



while True:
    print("""
          1.Yeni Kayıt Ekle          
          2.Kayıtları Göster
          3.Çıkış
""")
    
    secim = input("Yapmak istediğiniz işlemin numarasını giriniz:")

    if secim =="1":
        print("kayıt eklenecek")

    elif secim =="2":
        print("kayıtlar read yapılıp print edilecek")

    elif secim =="3":
        print("programdan çıkılıyor")
        break
    else:
        print("Geçersiz seçim! Lütfen Tekrar deneniyiz")