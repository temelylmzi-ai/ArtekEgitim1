#-----> SORU 1 <-----
# def printString(s,a):
#     print((s + "\n") * a)        
# string = input("Yazdirmak istediginiz kelimeyi giriniz: ")
# adet = int(input("Kac defa yazdirmak istersiniz: "))
# printString(string,adet)

# -----> SORU 2 <-----
# def myFunc(*args):
#     print(args)
# myFunc(1, 2, 3, 45, 6, 8151, 23, 213, 51, "Sa", "As")

# -----> SORU 3 <-----
# def bolenler(sayi):
#     bolenlerListesi = []
#     for i in range(1,sayi+1):
#         if sayi % i == 0:
#          bolenlerListesi.append(i)
#     print(bolenlerListesi)
# sayi = int(input("Lutfen bir sayi giriniz: "))
# bolenler(sayi)

# -----> SORU 4 <------
# def asalSayilar(sayi1,sayi2):
#     for sayi in range(sayi1,sayi2+1):
#         if sayi > 1:
#             for i in range(2,sayi):
#                 if sayi % i == 0:
#                     break
#             else:
#                 print(sayi)
# sayi1 = int(input("Sayi 1 = "))
# sayi2 = int(input("Sayi 2 = "))
# asalSayilar(sayi1,sayi2)
