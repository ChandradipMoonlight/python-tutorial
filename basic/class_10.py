# ===================================
# Python Classes & Object-Oriented Programming - Comprehensive Concepts and Examples
# Source: Python Official Documentation & Tutorial
# ===================================

print("===== 1. Basic Class Definition =====")
# A class is a blueprint for creating objects (instances)
# Classes are defined using the 'class' keyword

class Person:
    """Simple class definition"""
    pass # pass is used to create a empty class

# Creating an object (instance) of the class
person1 = Person()
print(f"Person object: {person1}")
# Output: Person object: <__main__.Person object at 0x...>

print("\n===== 2. Constructor (__init__) =====")
# __init__ is a special method called when an object is created
# It initia
# lizes the object's attributes

class Student:
    """Student class with constructor""" # docstring is used to describe the class
    def __init__(self, name, age, roll_no): # __init__ is a special method called when an object is created
        self.name = name # self is used to refer to the instance of the class
        self.age = age 
        self.roll_no = roll_no 
        print(f"Student {name} created!") # print is used to print the message

student1 = Student("Rahul", 20, 101)
# Output: Student Rahul created!

print(f"Name: {student1.name}, Age: {student1.age}, Roll No: {student1.roll_no}")
# Output: Name: Rahul, Age: 20, Roll No: 101

print("\n===== 3. Instance Methods =====")
# Instance methods operate on instance data using 'self' parameter

class Calculator:
    """Calculator class with instance methods"""
    def __init__(self, initial_value=0):
        self.value = initial_value
    
    def add(self, num):
        """Add a number to current value"""
        self.value += num
        return self.value
    
    def subtract(self, num):
        """Subtract a number from current value"""
        self.value -= num
        return self.value
    
    def multiply(self, num):
        """Multiply current value by a number"""
        self.value *= num
        return self.value
    
    def get_value(self):
        """Get current value"""
        return self.value

calc = Calculator(10)
print(f"Initial value: {calc.get_value()}")
# Output: Initial value: 10

print(f"After adding 5: {calc.add(5)}")
# Output: After adding 5: 15

print(f"After subtracting 3: {calc.subtract(3)}")
# Output: After subtracting 3: 12

print(f"After multiplying by 2: {calc.multiply(2)}")
# Output: After multiplying by 2: 24

print("\n===== 4. Instance Attributes =====")
# Instance attributes are specific to each object

class Car:
    """Car class with instance attributes"""
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0  # Default value
    
    def drive(self, miles):
        """Increase mileage"""
        self.mileage += miles
        print(f"Driven {miles} miles. Total mileage: {self.mileage}")

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2021)

print(f"Car1: {car1.brand} {car1.model} ({car1.year})")
# Output: Car1: Toyota Camry (2020)

print(f"Car2: {car2.brand} {car2.model} ({car2.year})")
# Output: Car2: Honda Civic (2021)

car1.drive(100)
# Output: Driven 100 miles. Total mileage: 100

car2.drive(50)
# Output: Driven 50 miles. Total mileage: 50

print(f"Car1 mileage: {car1.mileage}, Car2 mileage: {car2.mileage}")
# Output: Car1 mileage: 100, Car2 mileage: 50

print("\n===== 5. Class Attributes =====")
# Class attributes are shared by all instances of the class

class Dog:
    """Dog class with class and instance attributes"""
    species = "Canis familiaris"  # Class attribute (shared by all dogs)
    count = 0  # Class attribute to count instances
    
    def __init__(self, name, breed):
        self.name = name  # Instance attribute
        self.breed = breed  # Instance attribute
        Dog.count += 1  # Increment class attribute
    
    def display_info(self):
        """Display dog information"""
        print(f"{self.name} is a {self.breed} ({Dog.species})")

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")

print(f"Dog1 species: {dog1.species}")
# Output: Dog1 species: Canis familiaris

print(f"Dog2 species: {dog2.species}")
# Output: Dog2 species: Canis familiaris

print(f"Total dogs created: {Dog.count}")
# Output: Total dogs created: 2

# Accessing class attribute via class or instance
print(f"Species via class: {Dog.species}")
print(f"Species via instance: {dog1.species}")
# Output:
# Species via class: Canis familiaris
# Species via instance: Canis familiaris

print("\n===== 6. Class Methods =====")
# Class methods operate on the class itself, not instances
# They receive 'cls' as first parameter

class Employee:
    """Employee class with class methods"""
    company = "Tech Corp"
    total_employees = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1
    
    @classmethod
    def get_company(cls):
        """Class method to get company name"""
        return cls.company
    
    @classmethod
    def get_total_employees(cls):
        """Class method to get total employee count"""
        return cls.total_employees
    
    @classmethod
    def create_from_string(cls, emp_string):
        """Alternative constructor using class method"""
        name, salary = emp_string.split("-")
        return cls(name, int(salary))
    
    def display(self):
        """Display employee information"""
        print(f"{self.name} works at {Employee.company} with salary ${self.salary}")

emp1 = Employee("Rahul", 50000)
emp2 = Employee("Priya", 60000)

print(f"Company: {Employee.get_company()}")
# Output: Company: Tech Corp

print(f"Total employees: {Employee.get_total_employees()}")
# Output: Total employees: 2

# Using alternative constructor
emp3 = Employee.create_from_string("Ankit-55000")
emp3.display()
# Output: Ankit works at Tech Corp with salary $55000

print("\n===== 7. Static Methods =====")
# Static methods don't need 'self' or 'cls'
# They are utility functions related to the class

class MathUtils:
    """Class with static methods"""
    @staticmethod
    def add(a, b):
        """Static method to add two numbers"""
        return a + b
    
    @staticmethod
    def multiply(a, b):
        """Static method to multiply two numbers"""
        return a * b
    
    @staticmethod
    def is_even(num):
        """Static method to check if number is even"""
        return num % 2 == 0

print(f"Add: {MathUtils.add(5, 3)}")
# Output: Add: 8

print(f"Multiply: {MathUtils.multiply(4, 7)}")
# Output: Multiply: 28

print(f"Is 10 even? {MathUtils.is_even(10)}")
# Output: Is 10 even? True

# Can also be called on instance
utils = MathUtils()
print(f"Add via instance: {utils.add(2, 3)}")
# Output: Add via instance: 5

# difference between static method and class method
# @staticmethod decorator is used to define a static method
# @classmethod decorator is used to define a class method
# Difference between @staticmethod and @classmethod

# - @staticmethod: 
#   - Does not take any mandatory first argument like self or cls
#   - Cannot access class or instance variables
#   - Is just a function inside a class (namespace grouping)
#   - Usually used for utility functions related logically to the class

# - @classmethod:
#   - Takes cls (the class itself) as the first argument
#   - Can access or modify class variables or call other class methods
#   - Often used for factory/alternative constructors or methods that affect the class as a whole

class Demo:
    class_var = 0

    @staticmethod
    def static_method(x, y):
        # No access to class_var or cls/self
        return x + y

    @classmethod
    def class_method(cls, value):
        # Can access or modify class_var and receive the class as 'cls'
        cls.class_var += value
        print(f"class_var is now {cls.class_var}")

# Usage examples
print(f"Static method output: {Demo.static_method(3, 7)}")  # Output: 10

Demo.class_method(5)  # Output: class_var is now 5
Demo.class_method(2)  # Output: class_var is now 7


print("\n===== 8. Inheritance =====")
# Inheritance allows a class to inherit attributes and methods from parent class


class Animal:
    """Parent class (Base class)"""
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def speak(self):
        """Base method"""
        return "Some sound"
    
    def display_info(self):
        """Display animal information"""
        print(f"{self.name} is a {self.species}")

class Dog(Animal):
    """Child class (Derived class) inheriting from Animal"""
    def __init__(self, name, breed):
        super().__init__(name, "Dog")  # Call parent constructor
        self.breed = breed
    
    def speak(self):
        """Override parent method"""
        return "Woof! Woof!"
    
    def fetch(self):
        """Dog-specific method"""
        return f"{self.name} is fetching the ball!"

class Cat(Animal):
    """Child class inheriting from Animal"""
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color
    
    def speak(self):
        """Override parent method"""
        return "Meow! Meow!"

dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

dog.display_info()
# Output: Buddy is a Dog

cat.display_info()
# Output: Whiskers is a Cat

print(f"Dog says: {dog.speak()}")
# Output: Dog says: Woof! Woof!

print(f"Cat says: {cat.speak()}")
# Output: Cat says: Meow! Meow!

print(dog.fetch())
# Output: Buddy is fetching the ball!

print("\n===== 9. Multiple Inheritance =====")
# A class can inherit from multiple parent classes

class Flyable:
    """Mixin class for flying capability"""
    def fly(self):
        return "Flying high!"

class Swimmable:
    """Mixin class for swimming capability"""
    def swim(self):
        return "Swimming deep!"

class Duck(Animal, Flyable, Swimmable):
    """Duck inherits from Animal, Flyable, and Swimmable"""
    def __init__(self, name):
        super().__init__(name, "Duck")
    
    def speak(self):
        return "Quack! Quack!"

duck = Duck("Donald")
duck.display_info()
# Output: Donald is a Duck

print(f"Duck says: {duck.speak()}")
# Output: Duck says: Quack! Quack!

print(duck.fly())
# Output: Flying high!

print(duck.swim())
# Output: Swimming deep!

print("\n===== 10. Method Overriding =====")
# Child classes can override parent class methods

class Shape:
    """Base Shape class"""
    def __init__(self, name):
        self.name = name
    
    def area(self):
        """Base area method"""
        return 0
    
    def perimeter(self):
        """Base perimeter method"""
        return 0
    
    def display(self):
        print(f"{self.name} - Area: {self.area()}, Perimeter: {self.perimeter()}")

class Rectangle(Shape):
    """Rectangle class overriding Shape methods"""
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        """Override area method"""
        return self.width * self.height
    
    def perimeter(self):
        """Override perimeter method"""
        return 2 * (self.width + self.height)

class Circle(Shape):
    """Circle class overriding Shape methods"""
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        """Override area method"""
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        """Override perimeter method (circumference)"""
        return 2 * 3.14159 * self.radius

rect = Rectangle(5, 3)
circle = Circle(4)

rect.display()
# Output: Rectangle - Area: 15, Perimeter: 16

circle.display()
# Output: Circle - Area: 50.26544, Perimeter: 25.13272

print("\n===== 11. Encapsulation (Private Attributes) =====")
# Encapsulation: hiding internal details using naming conventions
# Single underscore (_) = protected (convention, not enforced)
# Double underscore (__) = private (name mangling)

class BankAccount:
    """BankAccount class demonstrating encapsulation"""
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public attribute
        self._balance = balance  # Protected attribute (convention)
        self.__pin = "1234"  # Private attribute (name mangling)
    
    def deposit(self, amount):
        """Public method to deposit money"""
        if amount > 0:
            self._balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        """Public method to withdraw money"""
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False
    
    def get_balance(self):
        """Public method to get balance"""
        return self._balance
    
    def _validate_pin(self, pin):
        """Protected method (convention)"""
        return self.__pin == pin
    
    def change_pin(self, old_pin, new_pin):
        """Public method using private attribute"""
        if self._validate_pin(old_pin):
            self.__pin = new_pin
            return True
        return False

account = BankAccount("ACC001", 1000)
print(f"Account Number: {account.account_number}")
# Output: Account Number: ACC001

print(f"Balance: ${account.get_balance()}")
# Output: Balance: $1000

account.deposit(500)
print(f"After deposit: ${account.get_balance()}")
# Output: After deposit: $1500

account.withdraw(200)
print(f"After withdrawal: ${account.get_balance()}")
# Output: After withdrawal: $1300

# Private attribute access (not recommended, but possible with name mangling)
# print(account._BankAccount__pin)  # Would print: 1234

print("\n===== 12. Property Decorators =====")
# Property decorators allow getter, setter, and deleter methods

class Temperature:
    """Temperature class with property decorators"""
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter for celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter for celsius with validation"""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Getter for fahrenheit (computed property)"""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Setter for fahrenheit"""
        self._celsius = (value - 32) * 5/9

temp = Temperature(25)
print(f"Celsius: {temp.celsius}°C")
# Output: Celsius: 25°C

print(f"Fahrenheit: {temp.fahrenheit}°F")
# Output: Fahrenheit: 77.0°F

temp.celsius = 30
print(f"New Celsius: {temp.celsius}°C")
# Output: New Celsius: 30°C

temp.fahrenheit = 86
print(f"After setting Fahrenheit to 86: {temp.celsius}°C")
# Output: After setting Fahrenheit to 86: 30.0°C

print("\n===== 13. Special Methods (Dunder Methods) =====")
# Special methods (magic methods) provide operator overloading and special behavior

class Book:
    """Book class with special methods"""
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        """String representation for end users"""
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        """String representation for developers"""
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):
        """Return length (number of pages)"""
        return self.pages
    
    def __eq__(self, other):
        """Equality comparison"""
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False
    
    def __lt__(self, other):
        """Less than comparison (by pages)"""
        if isinstance(other, Book):
            return self.pages < other.pages
        return NotImplemented
    
    def __add__(self, other):
        """Add two books (combine pages)"""
        if isinstance(other, Book):
            return Book(f"{self.title} & {other.title}", 
                       f"{self.author} & {other.author}",
                       self.pages + other.pages)
        return NotImplemented

book1 = Book("Python Basics", "John Doe", 300)
book2 = Book("Advanced Python", "Jane Smith", 500)

print(str(book1))
# Output: 'Python Basics' by John Doe

print(repr(book1))
# Output: Book('Python Basics', 'John Doe', 300)

print(f"Book length: {len(book1)} pages")
# Output: Book length: 300 pages

print(f"Are books equal? {book1 == book2}")
# Output: Are books equal? False

print(f"Is book1 shorter? {book1 < book2}")
# Output: Is book1 shorter? True

combined = book1 + book2
print(f"Combined book: {combined}, Pages: {len(combined)}")
# Output: Combined book: 'Python Basics & Advanced Python' by John Doe & Jane Smith, Pages: 800

print("\n===== 14. Abstract Base Classes =====")
# Abstract classes cannot be instantiated and require subclasses to implement methods

from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class for shapes"""
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def area(self):
        """Abstract method - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Abstract method - must be implemented by subclasses"""
        pass
    
    def display(self):
        """Concrete method available to all subclasses"""
        print(f"{self.name}: Area = {self.area()}, Perimeter = {self.perimeter()}")

class Square(Shape):
    """Square class implementing Shape abstract methods"""
    def __init__(self, side):
        super().__init__("Square")
        self.side = side
    
    def area(self):
        """Implement abstract method"""
        return self.side ** 2
    
    def perimeter(self):
        """Implement abstract method"""
        return 4 * self.side

class Triangle(Shape):
    """Triangle class implementing Shape abstract methods"""
    def __init__(self, a, b, c, height):
        super().__init__("Triangle")
        self.a = a
        self.b = b
        self.c = c
        self.height = height
    
    def area(self):
        """Implement abstract method"""
        return 0.5 * self.b * self.height
    
    def perimeter(self):
        """Implement abstract method"""
        return self.a + self.b + self.c

square = Square(5)
triangle = Triangle(3, 4, 5, 4)

square.display()
# Output: Square: Area = 25, Perimeter = 20

triangle.display()
# Output: Triangle: Area = 8.0, Perimeter = 12

# shape = Shape("Generic")  # This would raise TypeError - cannot instantiate abstract class

print("\n===== 15. Polymorphism =====")
# Polymorphism: same interface, different implementations

class Animal:
    """Base Animal class"""
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        """Base method - to be overridden"""
        return "Some sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    def make_sound(self):
        return "Moo!"

# Polymorphism in action
animals = [Dog("Buddy"), Cat("Whiskers"), Cow("Bessie")]

for animal in animals:
    print(f"{animal.name} says: {animal.make_sound()}")
# Output:
# Buddy says: Woof!
# Whiskers says: Meow!
# Bessie says: Moo!

print("\n===== 16. Method Resolution Order (MRO) =====")
# MRO determines the order in which base classes are searched for methods

class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

d = D()
print(f"D's method: {d.method()}")
# Output: D's method: B
# MRO: D -> B -> C -> A

print(f"MRO: {D.__mro__}")
# Output: MRO: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

print("\n===== 17. Composition vs Inheritance =====")
# Composition: "has-a" relationship
# Inheritance: "is-a" relationship

class Engine:
    """Engine class for composition"""
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return "Engine started!"

class Car:
    """Car class using composition"""
    def __init__(self, brand, engine_hp):
        self.brand = brand
        self.engine = Engine(engine_hp)  # Composition: Car HAS-A Engine
    
    def start(self):
        return self.engine.start()

car = Car("Toyota", 200)
print(f"{car.brand} - {car.start()}")
# Output: Toyota - Engine started!

print("\n===== 18. Class Decorators =====")
# Decorators can be applied to classes

def add_method(cls):
    """Class decorator adding a method"""
    def new_method(self):
        return "This is an added method!"
    cls.new_method = new_method
    return cls

@add_method
class MyClass:
    def __init__(self, value):
        self.value = value

obj = MyClass(10)
print(obj.new_method())
# Output: This is an added method!

print("\n===== 19. Data Classes (Python 3.7+) =====")
# Data classes automatically generate special methods

from dataclasses import dataclass, field

@dataclass
class Point:
    """Data class for a point"""
    x: int
    y: int
    z: int = 0  # Default value

@dataclass
class Student:
    """Data class for a student"""
    name: str
    age: int
    grades: list = field(default_factory=list)

point1 = Point(3, 4)
point2 = Point(3, 4)
point3 = Point(5, 6)

print(f"Point1: {point1}")
# Output: Point1: Point(x=3, y=4, z=0)

print(f"Are point1 and point2 equal? {point1 == point2}")
# Output: Are point1 and point2 equal? True

print(f"Are point1 and point3 equal? {point1 == point3}")
# Output: Are point1 and point3 equal? False

student = Student("Rahul", 20, [85, 90, 92])
print(f"Student: {student}")
# Output: Student: Student(name='Rahul', age=20, grades=[85, 90, 92])

print("\n===== 20. __slots__ for Memory Optimization =====")
# __slots__ restricts attributes and saves memory

class PersonWithSlots:
    """Person class using __slots__"""
    __slots__ = ['name', 'age']  # Only these attributes allowed
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = PersonWithSlots("Rahul", 25)
print(f"Name: {person.name}, Age: {person.age}")
# Output: Name: Rahul, Age: 25

# person.city = "Mumbai"  # This would raise AttributeError

print("\n===== 21. Class Variables vs Instance Variables =====")
# Understanding the difference between class and instance variables

class Counter:
    """Counter class demonstrating class vs instance variables"""
    count = 0  # Class variable (shared)
    
    def __init__(self, name):
        self.name = name  # Instance variable
        self.instance_count = 0  # Instance variable
        Counter.count += 1  # Modify class variable
    
    def increment_instance(self):
        """Increment instance variable"""
        self.instance_count += 1
    
    def display(self):
        print(f"{self.name}: Instance count = {self.instance_count}, Class count = {Counter.count}")

c1 = Counter("Counter1")
c2 = Counter("Counter2")
c3 = Counter("Counter3")

c1.increment_instance()
c1.increment_instance()
c2.increment_instance()

c1.display()
# Output: Counter1: Instance count = 2, Class count = 3

c2.display()
# Output: Counter2: Instance count = 1, Class count = 3

c3.display()
# Output: Counter3: Instance count = 0, Class count = 3

print("\n===== 22. Operator Overloading =====")
# Overloading operators using special methods

class Vector:
    """Vector class with operator overloading"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Overload + operator"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Overload - operator"""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """Overload * operator"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __eq__(self, other):
        """Overload == operator"""
        return self.x == other.x and self.y == other.y

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1: {v1}")
# Output: v1: Vector(3, 4)

print(f"v2: {v2}")
# Output: v2: Vector(1, 2)

print(f"v1 + v2: {v1 + v2}")
# Output: v1 + v2: Vector(4, 6)

print(f"v1 - v2: {v1 - v2}")
# Output: v1 - v2: Vector(2, 2)

print(f"v1 * 3: {v1 * 3}")
# Output: v1 * 3: Vector(9, 12)

print(f"v1 == v2: {v1 == v2}")
# Output: v1 == v2: False

print("\n===== 23. Context Managers (__enter__ and __exit__) =====")
# Context managers allow using 'with' statement

class FileManager:
    """File manager as context manager"""
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """Called when entering 'with' block"""
        self.file = open(self.filename, self.mode)
        print(f"Opened file: {self.filename}")
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting 'with' block"""
        if self.file:
            self.file.close()
            print(f"Closed file: {self.filename}")
        return False  # Don't suppress exceptions

# Using context manager
with FileManager("test.txt", "w") as f:
    f.write("Hello, World!")
# Output:
# Opened file: test.txt
# Closed file: test.txt

print("\n===== 24. Important Notes =====")
print("- Classes are blueprints for creating objects")
print("- __init__ is the constructor method called when object is created")
print("- 'self' refers to the instance of the class")
print("- Instance attributes are specific to each object")
print("- Class attributes are shared by all instances")
print("- Inheritance allows code reuse and specialization")
print("- Method overriding: child classes can override parent methods")
print("- Encapsulation: use _ for protected, __ for private (convention)")
print("- Polymorphism: same interface, different implementations")
print("- @classmethod operates on class, @staticmethod doesn't need self/cls")
print("- @property creates getter, setter, and deleter methods")
print("- Special methods (__str__, __repr__, etc.) provide special behavior")
print("- Abstract classes cannot be instantiated, require method implementation")
print("- Multiple inheritance: class can inherit from multiple parents")
print("- MRO determines method lookup order in inheritance hierarchy")
print("- Composition (has-a) vs Inheritance (is-a) relationships")
print("- Data classes automatically generate __init__, __repr__, __eq__, etc.")
print("- __slots__ restricts attributes and saves memory")
print("- Operator overloading uses special methods (__add__, __sub__, etc.)")
print("- Context managers use __enter__ and __exit__ for 'with' statement")

# ================================
# End of Classes & OOP Concepts & Examples
# ================================
