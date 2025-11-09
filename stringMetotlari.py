greeting = "Hello There. My name is Talha Yilmaz"

greeting_upper = greeting.upper()
print(greeting_upper)

greeting_lower = greeting.lower()
print(greeting_lower)

greeting_title = greeting.title()
print(greeting_title)

greeting_capitalize = greeting.capitalize()
print(greeting_capitalize)

greeting_strip = greeting.strip()
print(greeting_strip)

greeting_split = greeting.split('e')
print(greeting_split)
print(greeting_split[3])

greeting_join = 'e'.join(greeting_split)
print(greeting_join)

greeting_replace = greeting.replace("Talha Yilmaz", "John Doe")
print(greeting_replace)

greeting_find = greeting.find("Talha")
print(greeting_find)