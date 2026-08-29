class Dog:#blueprint for an object, what it will have, how it will behave
    def __init__(self, name, breed, owner):#special method that takes attributes and gets called on automatically w/o explicit code
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("woof, woof")

class Owner:
    def __init__(self, number,name, address):
        self.name = name
        self.number = number
        self.address = address

owner1 = Owner("999","dan","dash121")#owner1 is an object which is an instance of a class
dog1 = Dog("harry", "husky", owner1)#we instantiated owner1 object in dog1 object
dog1.bark()
print(dog1.name)
print(dog1.owner.name)


#####-----example 2----######;
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        a=input("")
        if a=="hi":#f in print is a formatted string literal, it tells to put correct value in {}
            print(f"hello, i am {self.name} i am {self.age} years old")
        else:
            print("i dont care")

person1 = person("clara", 21)
person1.greet()

####----example 3-----#####
class User:
    def __init__(self, username, gmail, password):
        self.username = username
        self.gmail = gmail
        self.password = password

    def say_hi(self, user):
        print(f"sending message to {user.username}: hi {user.username}, its {self.username}")

user1 = User("dantheman", "dan@abc.com", "123")
user2 = User("tinniewinnie", "win@xyz.com","abc")

user1.say_hi(user2)
print(user1.gmail)
user1.gmail = "dannn"
print(user1.gmail)#so basically we were able to change the value, we dont want that
#so to prevent this mutation we make the data private and user getters and setters

class student:
    def __init__(self, regno, name, classroom):
        self._name = name#can still be changed and accessed but its liek coding etiquette/convention like dont touch this directly to modify
        self.__regno = regno# the attribute can now not be accessed as we did name mangling
        self.classroom = classroom
    def clean_name(self):
        return self._name.lower().strip()
student1 = student(223,"Naya","sunflower")
print(student1._name)
student1._name = "raya"
print(student1.clean_name())
print(student1.__regno)##will give an error







