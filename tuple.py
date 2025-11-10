list = [1 , "Ahmet" , 87.5]
tuple = ("Talha" , "bir" , 2 , 37.8 , 2)
names = ("Ilker" , 8 , "K") + tuple

print(type(list))
print(type(tuple))

print(len(list))
print(len(tuple))

list[0] = 2 #liste üzerinde indexe özel islemler yapabiliriz ancak tuple'da yapamayiz. sadece elemanlara ulasabiliriz.
print(list) 

print(tuple.count(2))

print(names)

