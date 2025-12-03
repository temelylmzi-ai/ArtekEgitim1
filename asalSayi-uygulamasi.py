sayi = int(input("Bir sayi giriniz: "))
asalMi = True

if(sayi == 1):
    asalMi = False

for i in range(2,sayi):
    if(sayi % i == 0):
        asalMi = False

if(asalMi):
    print(f"{sayi} sayisi asal sayidir.")
else:
    print(f"{sayi} sayisi asal degildir.")