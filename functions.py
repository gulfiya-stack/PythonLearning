'''
FUNCTIONS:
(1) DEFINE vs CALL
(2) Parameter vs Argument
(3) Keyword and Default Arguments
(4) Scope
'''
print("=====DEFINE vs CALL=====")
# builtin function: print(), type()
# Function - reusable block of code
# Instead of block {} in JAVA, Python uses INDENTATION!

# DEFINE - build (Parameters)


def greet(a):
    print(f"How do you do, {a}?")


def greeting(b):
    print("greeting is executed")
    return f"Hi, {b}"


# CALL -> Execute --> ustida 2 ta probel tashlandi (Arguments)
greet("Guli")
result1 = greet("Nancy")
print(result1)

result2 = greeting("Justin")
print("result:", result2)


print("=====Keyword vs Default arguments=====")

# DEFINE


def give_greet(name, age=22):
    print("give_greet is being executed")
    return f"Hello, {name}, you are {age} years old"


# CALL
give_greet("Kate", 39)  # return ko'rinmaydi, chunki return print qilmaydi

result3 = give_greet(name="Kate", age=39)
print("Result3:", result3)

result4 = give_greet("Kate")
print("Result4:", result4)


print("=====SCOPE=====")
b = 100  # 3

# DEFINE


def calculate(a, b):  # 2
    c = a * b  # 1
    print(f"the c value: {c}")


# CALL
# (1) functionning ichkaridan izlaydi
# (2) functionning () Parametrlardan izlaydi
# (3) oxirida tashqaridan izlaydi
calculate(5, 50)  # bu bu yerdagi argumentni oladi (50*5)
# calculate(5)  # majburiy parameter bilan xato; # b ni olib tashlasak 100

# See error types
print(dir(__builtins__))
