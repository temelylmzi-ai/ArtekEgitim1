### SORU 1
nameSurname = input("Adinizi ve soyadinizi giriniz: ")
yas = int(input("Yasinizi giriniz: "))
egitimDurumu = input("Egitim durumunuzu giriniz: ")

if(yas >= 18 and ((egitimDurumu == "Lise" or "lise") or (egitimDurumu == "Universite" or "universite"))):
    print(f"{nameSurname} bey/hanimefendi ehliyet alabilirsiniz.")
else:
    print(f"{nameSurname} bey/hanimefendi ehliyet icin gerekli sartlari saglamiyosunuz.")

### SORU 2
yazili1 = float(input("1. yazili notunuzu giriniz: "))
yazili2 = float(input("2. yazili notunuzu giriniz: "))
sozlu = float(input("Sozlu notunuz giriniz: "))
ort = (yazili1 + yazili2 + sozlu) / 3
print("Ortalamaniz: ",ort)

if(0<=ort<25):
    print("Notunuz: 0")
elif(24<ort<45):
    print("Notunuz: 1")
elif(44<ort<55):
    print("Notunuz: 2")
elif(54<ort<70):
    print("Notunuz: 3")
elif(69<ort<85):
    print("Notunuz: 4")
elif(84<ort<=100):
    print("Notunuz: 5")
else:
    print("Gecersiz Not !!!")

### SORU 3
import datetime
tarih = input("Aracinizin trafige cikis tarihini giriniz (yil/ay/gün): ")
tarih = tarih.split("/")

trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
#trafigeCikis = datetime.datetime(2024,8,9) --> KULLANICIDAN ALMAK DAHA IYI
simdi = datetime.datetime.now()
days =simdi - trafigeCikis
print(days.days)
days = days.days

if(0 < days <= 365):
    print("1. Bakim Yili.")
elif(365 < days <= 365*2):
    print("2. Bakim Yili.")
elif(365*2 < days <= 365*3):
    print("3. Bakim Yili.")
else: 
    print("Hatali zaman girisi.")