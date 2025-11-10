fruits = {"orange" , "apple"} #kümeler indekslenemez.

for x in fruits:
    print(x)

fruits.add("cherry")
print(fruits)
fruits.update(["mango" , "grape"])
print(fruits)
fruits.remove("orange")
print(fruits)
fruits.discard("apple")
print(fruits)
fruits.pop() # Rastgele siler.
print(fruits)
fruits.clear()
print(fruits)

