### ----> FOR <----
### SORU 1
numbers = [1,3,5,7,9,12,19,21]
for num in numbers:
    if(num % 3 == 0):
        print(f"{num} sayisi 3'ün katidir.")       
    else:
        print(f"{num} sayisi 3'ün kati degildir.")

### SORU 2
sum = 0
for num in numbers:
    sum += num
print("Sayilarin toplami = ",sum)

### SORU 3
for num in numbers:
    if(num % 2 != 0):
        print(f"{num} sayisinin karesi = ",num**2)

### SORU 4
sehirler = ["Kocaeli","Istanbul","Ankara","Izmir","Rize"]
for sehir in sehirler:
    charSum = len(sehir)
    if(charSum<=5):
        print(f"{sehir} {charSum} karakterlidir.")

### SORU 5 VE SORU 6
priceSum = 0
urunler = [
    {'name':'samsung S6','price':'3000'},
    {'name':'samsung S7','price':'4000'},
    {'name':'samsung S8','price':'5000'},
    {'name':'samsung S9','price':'6000'},
    {'name':'samsung S10','price':'7000'},
]

for urun in urunler:
    priceSum += int((urun['price']))
print("Urunlerin toplam fiyati = ",priceSum)

for name in urunler:
    if(int(name['price'])<=5000):
        print(name)

# ----> WHILE <----
### SORU 1
sayilar = [1,3,5,7,9,12,19,21]
i = 0 
while (i < len(sayilar)):
    print(sayilar[i])
    i += 1

### SORU 2
bas = int(input("Baslangic degeri giriniz: "))
son = int(input("Son degeri giriniz: "))
i = bas + 1
while(i<son):
    if(i%2!=0):
        print(i)
    i += 1

### SORU 3
i = 100 
while(i>=1):
    print(i)
    i -= 1

### SORU 4
numbers1 = []
i = 0

while i < 5:
    sayi = int(input("Sayi giriniz: "))
    numbers1.append(sayi)
    i+=1
print(numbers1)

### SORU 5
urunler1 = []
i = 0
adet = int(input("Kac adet urun eklemek istiyosunuz: "))
while i < adet:
    name = input("Urunun ismini giriniz: ")
    price = input("Urunun fiyatini giriniz: ")
    urunler1.append(
        {'name':name,'price':price}
    )
    i += 1
for urun in urunler1:
    print(urun['name'],urun['price'])
