sayi1 = float(input("Birinci sayiyi girin: "))
sayi2 = float(input("Ikinci sayiyi girin: "))

if sayi1 > sayi2:
    print(f"{sayi1} sayisi {sayi2} sayisindan buyuktur.")
elif sayi1 < sayi2:
    print(f"{sayi1} sayisi {sayi2} sayisindan kucuktur.")
else:
    print("Iki sayi birbirine esittir.")

vize1 = float(input("Birinci vize notunu girin: "))
vize2 = float(input("Ikinci vize notunu girin: "))
final = float(input("Final notunu girin: "))

ortalama = (vize1 * 0.3) + (vize2 * 0.3) + (final * 0.4)

if ortalama >= 50 and final >= 50:
    print("Tebrikler, dersi gectiniz!")
else:
    print("Maalesef, dersi gecemediniz.")

sayi = float(input("Bir sayi girin: "))
if sayi > 0:
    print("Pozitif sayi")
elif sayi < 0:
    print("Negatif sayi")

_sayi = float(input("Bir sayi girin: "))
if _sayi %2 == 0:
    print("Cift sayi")
else:
    print("Tek sayi")

email = "email@talhayilmaz.com"
password = "12345"

girilen_email = input("Email girin: ")
girilen_password = input("Parola girin: ")

if girilen_email == email and girilen_password == password:
    print("Giris basarili")
else:
    print("Giris basarisiz")
