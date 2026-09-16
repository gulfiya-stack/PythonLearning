# takrorlanish xususiyatiga ega object lar
print("=======Iterable objects & RANGE=======")
# Iterable objects ---> string dict tuple list range map filter

range_obj = range(3)  # [0;2)
print("range_obj", range_obj)

for letter in "MIT":
    print(f"The letter: {letter}")
for ele in range_obj:
    print(f"The element: {ele}")

print("======DICTIONARY======")
# DICTIONARY is a JSON object!!!
person = {"name": "Justin", "age": 25, "single": True}
person_obj = dict(name="Justin", age=25, single=True)
print("The person:", person)
print("The person_obj", person_obj)


name1 = person_obj["name"]
# name2 = person_obj['hobby'] #key error
# 1-usul
print("name1: ", name1)
# print("name2: ", name2)
# 2 - usul
# method: get()
name = person_obj.get('name')
hobby = person_obj.get("hobby")
balance = person_obj.get("balance", 0)
print(name)
print(f"the name: {name}, hobby: {hobby}")  # None
print("balance: ", balance)

# Dictionary ---> Iterable object
del person_obj["single"]
for key in person_obj:
    print(f"the key: {key} => value {person_obj[key]}")  # person_obj.get(key)
