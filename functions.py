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
