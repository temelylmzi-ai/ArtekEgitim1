"""
x = input("1. sayiyi giriniz: ") # input fonksiyonu ile girilen degerler string tipindedir.
y = input("2. sayiyi giriniz: ") # input fonksiyonu ile girilen degerler string tipindedir.

print(type(x))  # string
print(type(y))  # string

toplam = int(x) + int(y)

print("Toplam: ", toplam)
"""


"""

# Veri Tipi Dönüşümleri

x= 5                # integer
y = 3.2             # float  
name = "Ahmet"      # string
isStudent = True    # boolean

print(type(x))         
print(type(y))
print(type(name))
print(type(isStudent))

x = float(x)      # integer to float
y = int(y)        # float to integer

print(x)
print(type(x))
print(y)
print(type(y))

result = str(x) + name  # float to string
print(result)
print(type(result))

isStudent = str(isStudent)  # boolean to string
print(isStudent)
print(type(isStudent))

isStudent = int(True)  # boolean to integer
print(isStudent)
print(type(isStudent))
"""

print("Dairenin alanini ve cevresini hesaplama programi\n")

yaricap = float(input("Dairenin yaricapini giriniz: "))
pi = 3.14

alan = pi * (yaricap ** 2)
cevre = 2 * pi * yaricap

print("Dairenin alani: ", alan)
print("Dairenin cevresi: ", cevre)