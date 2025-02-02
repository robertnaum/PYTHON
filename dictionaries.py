person = {
    "name": "Alice",
    "age" : 30,
    "city": "New York"
}

print (person)
print (person["name"])
person["age"] = 31
print (person["age"])

person["email"] = "alice@example.com"
print (person)

del person["age"]
print (person)

print(person.keys())
print(person.values())
print(person.items())

for key in person:
    print(key)
for value in person.values():
    print(value)
for item in person.items():
    print(item)

print(person.get("age","Not Found"))

email = person.pop("email")
print (email)
print(person)