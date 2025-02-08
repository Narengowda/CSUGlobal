"""
What is a class:
-----------------
A class is like a blueprint for creating objects, but instance is a specific object created from that class.
For Eg, "Car" could be a class means this is a blueprint to build a car, while the actual car would be an instance of
the car class, you can create as many instance you would like to. Each instances will have its own context and they are
not inter connected. In python you can use id(instance) to see the identification of instance. you can use isinstance(object/instance, className) to check if the instance.


How to Hide Python Attribute:
----------------------------
To hide python attribute inside Python class, we can use name mangling by adding a double underscore(Dunderscore)
to the attribute's name you would like to hide, like __attr_to_hide__.
Here are some code examples demonstrating the usage of classes in Python:
"""


# Python code for class and instance:
# -----------------------------------
class Car:
    def __init__(self, name, door):
        self.name = name
        self.doors = door

car_one = Car("SUV", 4)
print(f"Name: {car_one.name}, doors: {car_one.doors}")


# Python code for hiding:
# -----------------------------------

class MyClass:
    def __init__(self, value):
        self.__hidden_attribute = value

    def get_hidden_attribute(self):
        return self.__hidden_attribute

    def set_hidden_attribute(self, new_value):
        self.__hidden_attribute = new_value

# What you can do
obj = MyClass(10)
print(obj.get_hidden_attribute())
obj.set_hidden_attribute(20)
print(obj.get_hidden_attribute())

# What you cant do
obj = MyClass(100)
print(obj.__hidden_attribute)