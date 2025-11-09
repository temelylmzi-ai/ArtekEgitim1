names = ["Ali", "Hakan", "Veli", "Talha"]
years = [1990, 1985, 2000, 1995]

names.append("Cenk")
print(names)
names.insert(0, "Mert")
print(names)
names.remove("Hakan")
print(names)
print(names.index("Talha"))
print("Ali" in names)
names.reverse()
print(names)
years.reverse()
print(years)
names.sort()
print(names)
years.sort()
print(years)

str = "Chevrolet,Dacia,Renault,Fiat"
car_list = str.split(",")
print(car_list)

print(min(years))
print(max(years))
print(years.count(1998))
years.clear()
print(years)

carBrands = []
brand1 = input("Marka girin: ")
carBrands.append(brand1)
brand2 = input("Marka girin: ")
carBrands.append(brand2)
brand3 = input("Marka girin: ")
carBrands.append(brand3)
print(carBrands)