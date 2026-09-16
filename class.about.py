'''
(1) What is class
(2) ordinary vs static properties
(3) special/magic methods methods
'''

print("=======What is Class?=======")
# Class -> bluepring for an object creation (Object yaratish uchun shablon)
# structure -> state constructor method


class Person():
    # state
    message = "static state property"
    # constructure

    def __init__(self, name, age):
        self.name = name
        self.age = age
    # method

    def introduce(self):
        print(f'{self.name} says "How do you do?"')

    def say_age(self):
        print(f'{self.name} says I am {self.age}')

    @classmethod
    def explain(cls):
        print("Static method property executed!")


person1 = Person("Justin", 25)
person2 = Person("Martin", 35)

# ordinary state
print("Person1 name: ", person1.name)
print("Person2 name: ", person2.name)

# ordinary method
person1.introduce()
person1.say_age()
person2.introduce()
person2.say_age()  # Oddiy property -> obejct orqali chaqiriladi


print("=======Ordinary vs Static properties=======")
# Static state
new_message = Person.message  # Static -> classni ozi bilan birga keladigan property
print(new_message)

# Static method
Person.explain()


print("=======   special/magic methods methods   ========")
# __init__   __new__   __str__   __call__   __getitem__   __eq__   __len__


class Car():
    # state property
    description = "This class makes cars"
    # constructor

    def __new__(cls, *args):
        print("*__new__*")
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year

    def __str__(self):
        return f"The car {self.name} was produced in {self.year} year!"

    def __call__(self):
        print("Object called as function!")
        return True

    # method
    def start_engine(self):
        print(f"The {self.name} started engine")

    def stop_engine(self):
        print(f"The {self.name} stopped engine")


my_car = Car("Ferrari", 2025)
my_car.start_engine()
my_car.stop_engine()

print("----------")
your_car = Car("Toyota", 2026)  # __new__ ishga tushadi

print(your_car)
your_car()
response = your_car()  # CALL
print(response)
