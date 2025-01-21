"""
Lists and dictionaries are very important Data stuctures in Python.
Lists are ordered and you can modify/mutate them, while dictionaries are for storing key-value pairs.
In List data is accessed by index, in dict data is accessed by key
"""

# ------Py List demo Code:-------
fruits = ["apple", "Banana", "cherry"]
fruits.append("guava") # adds a friuit to list
fruits.insert(1, "blue berry") # insert to the right of list
fruits[2] = "blackberry" #Assigns blackberry to the second index
fruits.remove("apple") # remove apple from list
fruits.pop(1) #Remove first item
print(fruits)

# ----- Py Dict demo code -------
#iniitiate a dict with key value
person = {
    "name": "Naren",
    "age": 35,
    "city": "DC"
}

person["email"] = "naren@mail.com"  # Creates a new key value pair
person["age"] = 31 # updates the value of key "age"
del person["city"] # removes the key value pair with key city

print(person) # Print entire dict
print(person.get('age')) # access value of key age, if not found return none
print(person['key_doesnt_exist']) # Throws error if key doesnt exist


