
# Value Types --> string , number

x = 5
y = 25

x = y # Degerlerin esitlemesi yapilir. Birbirinden etkilenmezler.

y = 10

print(x,y)

# Reference Types

a = ["apple" , "banana"]
b = ["apple" , "banana"]

a = b # Verilerin tutuldugu adreslerin esitlemesi yapilir. Yapilan degisikliklerden ikisi de etkilenir.

b[0] = "grape"

print(a,b)