# print("Hello World")
# print("Everything in Python is an object")
# print("Even primitive variables are objects in Python")

# Dunder __builtins__, __init__
message = "PYTHON: Everything is an object"
print(message)

result = type(message)
print(result)

'''
In Python there are built-in tools: 
(1) TYPES: int, str, float, list, dict
(2) FUNCTIONS > print(), len(), input(), type()
(3) Constants > True, False, None

'''
# Constants larni ko'rish uchun - print(__builtins__)/print(dir(__builtins__))
print(__builtins__)
print(dir(__builtins__))
