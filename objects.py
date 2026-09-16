'''
(1) What is an object? 
(2) Iterable objects and & RANGE 
(3) DICTIONARY
(4) Error handling system
'''

import array  # package or module
import math   # package
from math import ceil, asin   # Math package dan Ceil method ni chaqirish


print("=======What is an object?=======")
# An object has state and methods
# Everything is an object in Python

print(type("Hello World"))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# a = 97.7 --> a dan path qilsak bo'ladi
# PARADIGM -> OOP (Objectlarga asoslangan dasturlash), Functional(Chiziqli Programming - Variable va Functions)
# OOP 4 ta concepts ga ega:
# (1)	Abstraction; (2) Encapsulation; (3) Polimorphism; (4) Inheritance

result1 = math.ceil(97.7)  # CALL --> 98; 97.1->98
print("result1: ", result1)
result2 = ceil(99.7)
result3 = asin(0.56)
print("result2: ", result2)
print("ASIN OF 0.56", result3)


print("=======Error handling system=======")

car_dict = dict(name="Toyota", year=2026, electric=True)

try:
    print("PASSED HERE")
    result0 = car_dict["year"]
    a = car_dict.speed  # AttributeError: 'dict' object has no attribute 'speed'
    # result = car_dict["origin"]
    print("result: ", result0)
    # print("result: ", result)
# except (KeyError, AttributeError) as err:
    # print("Error", err)
except Exception as err:
    print("Error", err)
# except KeyError as err:
#     print("No origin state property found: ", err)
# except AttributeError as err:
#     print("No speed state property found: ", err)
else:  # try xatosiz bo'lsa
    print("Executed successfully without errors")
finally:
    print("Final closing logic")
