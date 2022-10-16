print("Vize Notunuzu Giriniz")
vize = int(input())
print("Final Notunuzu Giriniz")
final = int(input())
if(final < 50):
    print("Final notu barajı geçemediği için kalmış bulunmaktasınız.")

sonuc = (vize*40)/100 + (final*60)/100
if(sonuc < 50):
    print("Kaldınız", sonuc)
else:
    print("Geçtiniz", sonuc)