import random

sayi = random.randint(1,100)
sayac = 0
puan = 0
hakSayisi = int(input("Lutfen hak sayisini giriniz: "))
can = hakSayisi

while hakSayisi > 0:
    sayac +=1
    hakSayisi -= 1
    tahmin = int(input("Lutfen 1 ile 100 arasinda sayi tahmininizi giriniz: ")) 
    if hakSayisi == 0:
        if sayi == tahmin:
            print(f"Sayi son tahminde bildiniz. Puaniniz = {100 - ((100/can)*(hakSayisi+1))}")
            break
        else:
            print(f"Hakkiniz bitti. Tutulan sayi = {sayi}. Puaniniz = 0")
        break     
    if sayi < tahmin:
        print("Asagi")
        print(f"{hakSayisi} hakkiniz kaldi")
    elif sayi > tahmin:
        print("Yukari")
        print(f"{hakSayisi} hakkiniz kaldi")
    else:
        print(f"Sayiyi {sayac}. tahminde buldunuz. Toplam puaniniz = {(100/can)*(hakSayisi+1)}")
        break


