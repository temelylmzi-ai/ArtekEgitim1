students = {}

number = input("Ogrenci no: ")
name = input("Ogrenci adi: ")
surname = input("Ogrenci soyadi: ")
phone = input("Ogrenci tel no:")

# students[number] = {
#         "ad" : name,
#         "soyad" : surname,
#         "telefon" : phone
# }

##########  YA DA  ###########

students.update({
    number: {
        "ad": name,
        "soyad" : surname,
        "telefon" : phone
    }
})

number = input("Ogrenci no: ")
name = input("Ogrenci adi: ")
surname = input("Ogrenci soyadi: ")
phone = input("Ogrenci tel no:")

students.update({
    number: {
        "ad": name,
        "soyad" : surname,
        "telefon" : phone
    }
})

print(f"\n{students}\n")

stdNo = input("Istediginiz ogrencinin bilgileri icin ogrenci no giriniz: ")
student = students[stdNo]
print(f"\nAradiginiz {stdNo} nolu ogrencinin adi {student["ad"]} , soyadi {student["soyad"]} ve telefon numarasi {student["telefon"]}")

