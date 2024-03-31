person = {"name": "Robert", "age": 30}

# Operators
print("'name' in person", "name" in person)  # true
print("'nationality' in person", "nationality" not in person)  # true
print('person == {"name": "Robert"}', person == {"name": "Robert"})  # false
print(
    'person == {"name": "Robert", "age": 30}', person == {"name": "Robert", "age": 30}
)  # true
print('person != {"name": "Robert"}', person != {"name": "Robert"})  # true
print(
    'person is {"name": "Robert", "age": 30}', person is {"name": "Robert", "age": 30}
)  # false

person2 = person
print("person == person2", person == person2)  # true
print("person is person2", person is person2)  # true

print(
    person | {"nationality": "Colombia"}
)  # {'name': 'Robert', 'age': 30, 'nationality': 'Colombia'}

print("person['name'] =", person["name"])
person["age"] = 33
person["weight"] = 78.3
del person["weight"]  # Remove key and Value

print([person["test"]])
