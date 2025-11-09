# String Islemleri
website = "https://www.example.com"
course = "Python Kursu: Bastan Sona Python Programlama Rehberi 2025"

print(len(course))
print(website[8:11])
print(website[20:23])
print(course[0:15])
print(course[-15:])
print(course[::-1])

# String Formatlama
name , surname , age , job = "Bora" , "Yilmaz" , 30 , "Muzisyen"

print("Benim adim {} {}, yasim {} ve meslegim {}.".format(name, surname, age, job))
print(f"Benim adim {name} {surname}, yasim {age} ve meslegim {job}.")

# String Metotlari
greeting = "Hello, world!"
greeting = greeting[:7] + 'W' + greeting[8:]
print(greeting)

print("abc" * 3)
