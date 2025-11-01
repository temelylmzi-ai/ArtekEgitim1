"""

#-OPERATÖRLER VE TEMEL VERİ TİPLERİ-

print("Merhaba, Python dunyasina hos geldiniz!\n")

print(2 + 3)
print((2+3)*(5-1)/3)
print(2**3)
print(10 % 3)  # Kalan bulma
print(10 / 3)
print(10 // 3) # Kalansiz bolme
print(11//3)   

x = 2*47
print(type(x))

"""

"""

#-Variable Tanimlama-

maasTalha = 5000
maasYilmaz = 4000   
vergiOrani = 0.27

netMaasTalha = maasTalha - (maasTalha * vergiOrani)
netMaasYilmaz = maasYilmaz - (maasYilmaz * vergiOrani)

print("Talha'nin net maasi: ", netMaasTalha)
print("Yilmaz'in net maasi: ", netMaasYilmaz)

num1 = 10   # integer
num2 = 3.5  # float
print(num1 ," ", num2)  
num1 = 20
print(num1)
num1 += 5  # num1 = num1 + 5
print(num1)
name = "Talha"  # string
isStudent = True  # bool

a = "5"
b = "10"
print(a + b)  # string birlestirme

# Degiskenleri tek satirda da tanimlayabiliriz.

"""