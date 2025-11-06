name = "Talha"
surname = "Yilmaz"
age = 22

print(f"My name is {name} {surname} and I am {age} years old.") #f-string kullanımı

print("My name is {} {} and I am {} years old.".format(name, surname, age)) #format metodu kullanımı

greeting = ("My name is " + name + " " + surname + " and I am " + str(age) + " years old.") #string birlestirme yaptıgımız icin age bilgisini stringe cevirdik
print(greeting)

print(greeting[0])      #ilk karakter
print(greeting[11:19])  #substring
print(greeting[-1])     #son karakter
print(greeting[2:46:2]) #2 karakter atlayarak yazdırma
print(len(greeting))    #karakter sayısı

result = 500 / 478
print(f"Result: {result:.2f}") #ondalık sayıyı 2 basamakla sınırlama