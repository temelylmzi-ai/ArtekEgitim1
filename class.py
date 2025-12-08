class Person:

    address = "no information" # class object attribute
    
    def __init__(self,name,year): # constructor
        self.name = name # instance attribute
        self.year = year

    def calculateAge(self): # instance object method
        return 2025 - self.year 

p1 = Person("Talha",2003)
p2 = Person("Sena",1999)
p1.address = "Kocaeli"
p2.address = "Istanbul"

print(f"name: {p1.name} , birth year: {p1.year} , age: {p1.calculateAge()} , address: {p1.address}")
print(f"name: {p2.name} , birth year: {p2.year} , age: {p2.calculateAge()} , address: {p2.address}")

        