
# f = open("dosya_adi", "kip")
# kip = w = yazma kipi(write)
# kip = r = okuma kipi(read)
# kip = a = hepsi (all)
#*****************************
# file = open(dosya_adi)
# file.read(), file.write()

kayit_dosyasi = open("kayit_dosyasi.txt", "w") 
kayit_dosyasi.write("Ayaz : 120.000 EURO")
kayit_dosyasi.write("\nAybars : 130.000 EURO")

kayit_dosyasi.close()