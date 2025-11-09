# my_list = [1, 2, 3, 4, 5]
# print(my_list)

# my_list1 = ["bir", 2, True, 4.5]
# print(my_list1)

# print(my_list + my_list1)

# print(len(my_list))

# s = "Hello There, How are you?".split()
# print(s[3])

# lists = [my_list , my_list1]
# print(lists)
# print(lists[1][0])

carsBrands = ["BMW", "Mercedes", "Opel", "Mazda"]
print(len(carsBrands))

print(carsBrands[0], carsBrands[-1])

carsBrands[3] = "Toyota"
print(carsBrands)

isFound = "Mercedes" in carsBrands
print(isFound)

print(carsBrands[0:3])

carsBrands[2], carsBrands[3] = "Toyota", "Renault"
print(carsBrands)

carsBrands.append("Audi"),carsBrands.append("Nissan")
print(carsBrands)

print(carsBrands[-2])

del carsBrands[-1]
print(carsBrands)

print(carsBrands[::-1])

studentA = ["Talha", "Yilmaz", 2003, [70, 60, 70]]
studentB = ["Sena", "Kahraman Yilmaz", 2003, [80, 80, 70]]
studentC = ["Temel", "Yilmaz", 1998, [80, 70, 90]]

students = [studentA, studentB, studentC]
print(students)
print(students[1][3][1])

print(f"{students[1][0]} {students[1][1]} {2025 - students[1][2]} yasindadir ve not ortalamasi {(students[1][3][0] + students[1][3][1] + students[1][3][2]) / 3} dir.")

