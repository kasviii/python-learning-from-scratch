##shortnotes
class Person: #blueprint
    def __init__(self, name, age):#attributes= data belonging to an object
        self.name = name
        self.age = age
    def greet(self):#methods=things an object can do
        print(f"Hi, I'm {self.name}!")
        
        
person1 = Person("Clara", 21)##object=actual thing made from blueprint
print(person1.name) 
print(person1.age) 
person1.greet()
#therefore object has attributes like clara and 21 and can do methods like greet


##INHERITANCE##
class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print("I am eating")
    def sleep(self):
        print("in nature")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)#super() lets you use parents version
        self.breed = breed
    def bark(self):
        print("woof!")
    def sleep(self):
        print("on bed")#can override parents method

dog1 = Dog("Buddy", "Labrador")
dog1.eat()#inherited from animal
dog1.bark()#dogs own method
dog1.sleep()
ani = Animal("tom")
ani.sleep()
print(dog1.name+" "+dog1.breed)
print(ani.name)

##POLYMORPHSIM##
#-> different objects can use the same method name but behave differently
class Dog:
    def speak(self):
        print("Woof!")


class Cat:
    def speak(self):
        print("Meow!")


class Cow:
    def speak(self):
        print("Moo!")

dog = Dog()
cat = Cat()
cow = Cow()

dog.speak()
cat.speak()
cow.speak()
##here speak() did the same thing everytime

def make_sound(animal):
    animal.speak()

d = Dog()
c = Cat()

make_sound(d)
make_sound(c)

##ENCAPSULATION
#-> keeping an object's data and the code that controls that data together, while controlling how the data is accessed or changed.
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance

account = BankAccount(1000)

account.deposit(500)
#account._balance = -999999 so underscore doesnt prevent chance, its just convention, that says this is private
print(account.get_balance())

##ABSTRACTION->hide complicated stuff and explose only what user needs
class CoffeeMachine:

    def make_coffee(self):
        self.heat_water()
        self.grind_beans()
        self.add_water()
        print("Coffee ready!")

    def heat_water(self):
        print("Heating water...")

    def grind_beans(self):
        print("Grinding beans...")

    def add_water(self):
        print("Adding water...")

machine = CoffeeMachine()

machine.make_coffee()