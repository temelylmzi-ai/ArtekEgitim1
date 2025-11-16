# x , y ,z = 5 , 10 , 15
# print(x , y , z)

# x += 5
# y *= 4.5
# z -= 3
# print(x , y , z)

# z %= 4 # sayiya bölümından kalanı verir.
# print(z)

# z = 12
# z /= 5
# print(z)

# y //= 5 # tam sayı bölümü verir.
# print(y)

# x **= 2 # üs alma işlemi yapar.
# print(x)

# values = 1,3,4,8,2,7,9,10
# print(values)
# print(type(values))

# a, *b, c, d = values
# print(a, b[3], c, d)


### UYGULAMA ###

x , y , z = 2 , 5 , 10
numbers = 1 , 5 , 7 , 10 , 6

# input1 = float(input("Bir sayi giriniz: ")) 
# input2 = float(input("Bir sayi giriniz: "))  

# print((input1*input2) - (x + y + z))

result1 = (y // x)
print(result1)
result2 = (x + y + z) % 3
print(result2)
result3 = y ** x
print(result3)
x , *y , z = numbers
print(x , y , z)
result4 = z ** 3 
print(result4)
result5 = sum(y)
print(result5)