website = "https://www.example.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberi 2025"

s = " Hello, World! "
s = s.strip()
print(s)

#website = website.replace("https://www.", "").replace(".com", "")
#print(website)

#website = website.lstrip("htsp:/w.")
#website = website.rstrip(".com")
#print(website)

course = course.lower()
print(course)

print(website.count("a"))

is_it = website.startswith("www")
print(is_it)

is_it = website.endswith("com")
print(is_it)

isFound = website.find(".com")
print(isFound)

#course = course.isalpha() # Ya da isdigit()
#print(course)

x = "Contents"
print(x.center(50, "*"))

#course = course.replace(" ", "-")
#print(course)

result = "Hello World".replace("World", "There")
print(result)

course = course.split(" ")
print(course)