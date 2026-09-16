'''
(1) What is class
(2) ordinary vs static properties
(3) special methods
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
