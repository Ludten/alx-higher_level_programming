# Python - Almost a circle
> Each file in this repository holds code that illustrates everything I've learnt
> specific to the Python programming language

## Description of what each file shows:
* base.py: The first class `Base`

* rectangle.py: The class `Rectangle` that inherits from `Base`

* Update the class `Rectangle` by adding validation of all setter methods and instantiation (`id` excluded)

* Update the class `Rectangle` by adding the public method `def area(self):` that returns the area value of the `Rectangle` instance.

* Update the class `Rectangle` by adding the public method `def display(self):` that prints in stdout the Rectangle instance with the character `#` - you don’t need to handle `x` and `y` here.

* Update the `class` Rectangle by overriding the `__str__` method so that it returns `[Rectangle] (<id>) <x>/<y> - <width>/<height>`

* Update the class `Rectangle` by improving the public method `def display(self):` to print in stdout the Rectangle instance with the character `#` by taking care of `x` and `y`

* Update the class `Rectangle` by adding the public method `def update(self, *args):` that assigns an argument to each attribute:

	- 1st argument should be the `id` attribute
	- 2nd argument should be the `width` attribute
	- 3rd argument should be the `height` attribute
	- 4th argument should be the `x` attribute
	- 5th argument should be the `y` attribute

* Update the class `Rectangle` by updating the public method `def update(self, *args):` by changing the prototype to `update(self, *args, **kwargs)` that assigns a key/value argument to attributes

* square.py: The class `Square` that inherits from `Rectangle`

* Update the class `Square` by adding the public getter and setter `size`

* Update the class `Square` by adding the public method `def update(self, *args, **kwargs)` that assigns attributes

* Update the class `Rectangle` by adding the public method `def to_dictionary(self):` that returns the dictionary representation of a `Rectangle`

* Update the class `Square` by adding the public method `def to_dictionary(self):` that returns the dictionary representation of a `Square`

* Update the class `Base` by adding the static method `def to_json_string(list_dictionaries):` that returns the JSON string representation of `list_dictionaries`

* Update the class `Base` by adding the class method `def save_to_file(cls, list_objs):` that writes the JSON string representation of `list_objs` to a file

* Update the class `Base` by adding the static method `def from_json_string(json_string):` that returns the list of the JSON string representation `json_string`

* Update the class `Base` by adding the class method `def create(cls, **dictionary):` that returns an instance with all attributes already set

* Update the class `Base` by adding the class method `def load_from_file(cls):` that returns a list of instances

* Update the class `Base` by adding the class methods `def save_to_file_csv(cls, list_objs):` and `def load_from_file_csv(cls):` that serializes and deserializes in CSV:

* Update the class `Base` by adding the static method `def draw(list_rectangles, list_squares):` that opens a window and draws all the `Rectangles` and `Squares`
