# #and
# x = 6
# result = (x > 2) and (x < 10) # iki kosulun da dogru olmasi gerekir.
# print(result)  # True

# #or
# y = 4
# result = (y > 2) or (y < 3) # kosullardan birinin dogru olmasi yeterli.
# print(result)  # True

# #not
# z = 5
# result = not(z > 3) # kosulun dogru olmasi durumunda sonucu yanlis yapar.
# print(result)  # False

# # Kombinasyon
# a = 11
# result = (a > 5) and not(a < 10) # ilk kosul dogru, ikinci kosul yanlis, sonuc yanlis.
# print(result)  # False

# input1 = int(input("Bir sayi giriniz: "))
# result = ((5 < input1 ) and (input1 < 10)) and (input1 % 2 == 0)
# print(result)


### UYGULAMA ###

#1
girilen_sayi = int(input("Bir sayi giriniz: "))
sonuc = (girilen_sayi > 0) and (girilen_sayi < 100)
print(sonuc)

sonuc1 = girilen_sayi > 0 and girilen_sayi % 2 == 0
print(sonuc1)

#2
vize1 = float(input("Birinci vize notunu giriniz: "))
vize2 = float(input("Ikinci vize notunu giriniz: "))   
final = float(input("Final notunu giriniz: "))

ortalama = (vize1 * 0.3) + (vize2 * 0.3) + (final * 0.4)

sonuc3 = (ortalama >= 50) and (final >= 40)
print("Sinifi gecti mi (final şartli) ? ", sonuc3)

sonuc4 = (ortalama >= 50) or (final >= 70)
print("Sinifi gecti mi ? ", sonuc4)

#3
ad = input("Adinizi giriniz: ")
kilo = float(input("Kilonuzu giriniz (kg): "))
boy = float(input("Boyunuzu giriniz (m): "))
bmi = kilo / (boy ** 2)

print(f"\n{ad} kisisinin vucut kitle indeksi (BMI) : {bmi:.2f}")
sonuc5 = bmi < 18.5
print("Zayif mi? ", sonuc5)
sonuc6 = (bmi >= 18.5) and (bmi <= 24.9)
print("Normal kilolu mu? ", sonuc6)
sonuc7 = (bmi >= 25) and (bmi <= 29.9)
print("Fazla kilolu mu? ", sonuc7)
sonuc8 = bmi >= 30
print("Obez mi? ", sonuc8)
