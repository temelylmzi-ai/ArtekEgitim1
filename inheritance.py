class Person():
    
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        print("Person Created")
    
    def who_am_i(self):
        print("I am a person.")

    def eat(self):
        print("I am eating.")

class Student(Person):

    def __init__(self,fname,lname,number):
        self.number = number
        Person.__init__(self,fname,lname)
        print("Student Created")
    
    def who_am_i(self): # override
        print("I am a student.")

    def sayHello(self):
        print("Hello i am a student.")

class Teacher(Person):
    def __init__(self,fname,lname,branch):
        Person.__init__(self,fname,lname)
        self.branch = branch

    def who_am_i(self):
        print(f"I am a {self.branch} teacher")

##########################################################

p1 = Person("Ali","Yilmaz")
s1 = Student("Cinar","Turan",123456)
t1 = Teacher("Sena","Yilmaz","Matematik")

print(f"{p1.fname} {p1.lname}")
print(f"{s1.fname} {s1.lname} {s1.number}")
print(f"{t1.fname} {t1.lname} {t1.branch}")

p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()
s1.sayHello()
t1.who_am_i()
t1.eat()
