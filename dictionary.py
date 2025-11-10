# key - value

# sehirler = ["Kocaeli" , "Istanbul"]
# plakalar= [41 , 34]

# print(plakalar[sehirler.index("Istanbul")])
# print(plakalar[sehirler.index("Kocaeli")])

# plakalar = {
#     "Kocaeli" : 41 ,
#     "Istanbul": 34 
#             }

# print(plakalar)
# print(plakalar["Kocaeli"])

# plakalar["Ankara"] = 6
# plakalar["Kocaeli"] = "new value"

# print(plakalar)

users = {
    "sadikturan" : {
        "roles" : ["user"],
        'age' : 36 ,
        'email' : "sdgksjdg@gmail.com",
        'city' : "nevsehir"
        },
    "talhayilmaz" : {
        "roles" : ["admin" , "user"],
        'age' : 22,
        'email' : "skdjgşls@icloud.com",
        'city' : "erzurum"
    }
}

print(users['talhayilmaz']["age"])
print(users["talhayilmaz"]["roles"][1])




