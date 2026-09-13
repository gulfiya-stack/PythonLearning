# print("="*10)
'''
(a)	In Java --> Variable is a name of a storage location, malumot manzilining nomlanishi
(b)	In Python --> named references --> storage locationga qaratilgan tushuncha
'''
print("==========number============")

count = 100
count_type = type(count)
print("count", count)
print("count type", count_type)

# Superstring in node js, in Python -> (f"{count_type}")
print(f"The count is {count} and its type is {count_type}")

# Count object ekanin ko'rish - methods larni chaqirish

# attribute/property - state; sonning surat qismini beradi count/1.
# Kvadratlar -->  method, kalit(wrench) lar esa --> state


# method; bit_count() integer sonning binary ko‘rinishida nechta 1 borligini sanaydi: 1100100 - > 3
result1 = count.bit_count()  # method
result2 = count.numerator    # state
print(result1)
print(result2)

print("==========string============")

# METHODS: upper() lower() title() find() replace()

course = "AI Python Fullstack"
result3 = type(course)
print(f"Result 1: {result3}")

result3 = course.title()
print(f"Result 2: {result3}")

result3 = course.upper()
print(f"Result 3: {result3}")

result3 = course.replace("Fullstack", "MasterClass")
print(f"Result 4: {result3}")

result3 = course.replace("Fullstack", "MasterClass")
print(f"Result 4: {result3}")

print(result3)  # o'zgarmaydi chunki courseni o'zgartirmadik
