#!/usr/bin/python3
"""
A module that add attributes to an object
"""


def add_attribute(obj, name, value):
    """
    A function that adds an attribute to an object

    Args:
        obj (object)
        name (str)
        value (any)

    Raises:
        TypeError: If the attribute cannot be added.
    """
    if hasattr(obj, "__dict__") is True:
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")


class MyClass():
    pass


mc = MyClass()
add_attribute(mc, "name", "John")
print(mc.name)

try:
    a = "My String"
    add_attribute(a, "name", "Bob")
    print(a.name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
