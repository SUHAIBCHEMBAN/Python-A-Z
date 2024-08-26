"""
TODO:Introduction to OOP concepts?

### **Introduction to Object-Oriented Programming (OOP) Concepts:**

Object-Oriented Programming (OOP) is a programming paradigm based on the concept of objects. OOP is designed to improve code organization, reuse, and maintenance. The core concepts of OOP are:

### **1. Classes and Objects:**

- **Class:** A blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
  
  **Example:**
  ```python
  class Dog:
      def __init__(self, name, age):
          self.name = name
          self.age = age
      
      def bark(self):
          return "Woof!"
  ```

- **Object:** An instance of a class. Each object can hold different values for its attributes.

  **Example:**
  ```python
  my_dog = Dog("Buddy", 4)
  print(my_dog.name)  # Output: Buddy
  print(my_dog.bark())  # Output: Woof!
  ```

### **2. Encapsulation:**

- **Encapsulation:** Bundling data (attributes) and methods (functions) that operate on the data into a single unit (a class). It also involves restricting direct access to some of an object's components.

  **Example:**
  ```python
  class Account:
      def __init__(self, balance):
          self.__balance = balance  # Private attribute

      def deposit(self, amount):
          self.__balance += amount

      def get_balance(self):
          return self.__balance
  ```

### **3. Inheritance:**

- **Inheritance:** A mechanism to create a new class based on an existing class. The new class (child) inherits attributes and methods from the existing class (parent).

  **Example:**
  ```python
  class Animal:
      def speak(self):
          return "Animal sound"

  class Cat(Animal):
      def purr(self):
          return "Purr"
      
  my_cat = Cat()
  print(my_cat.speak())  # Output: Animal sound
  print(my_cat.purr())   # Output: Purr
  ```

### **4. Polymorphism:**

- **Polymorphism:** The ability to use a single interface to represent different underlying forms (data types). It allows methods to do different things based on the object they are acting upon.

  **Example:**
  ```python
  class Bird:
      def speak(self):
          return "Tweet"

  class Dog:
      def speak(self):
          return "Woof"

  def make_animal_speak(animal):
      print(animal.speak())

  my_bird = Bird()
  my_dog = Dog()

  make_animal_speak(my_bird)  # Output: Tweet
  make_animal_speak(my_dog)   # Output: Woof
  ```

### **5. Abstraction:**

- **Abstraction:** Hiding complex implementation details and showing only the essential features of an object. It allows focusing on what an object does rather than how it does it.

  **Example:**
  ```python
  from abc import ABC, abstractmethod

  class Shape(ABC):
      @abstractmethod
      def area(self):
          pass

  class Rectangle(Shape):
      def __init__(self, width, height):
          self.width = width
          self.height = height

      def area(self):
          return self.width * self.height

  rect = Rectangle(5, 10)
  print(rect.area())  # Output: 50
  ```

### **Summary:**

- **Classes and Objects:** Classes define the blueprint, while objects are instances of classes.
- **Encapsulation:** Bundles data and methods, and restricts direct access to some components.
- **Inheritance:** Creates new classes from existing ones, inheriting attributes and methods.
- **Polymorphism:** Allows methods to use different implementations based on the object.
- **Abstraction:** Hides complex details and exposes only essential features.

These OOP concepts help in building modular, reusable, and maintainable code.

======================================================================================

TODO:Creating and using classes and objects?

### **Creating and Using Classes and Objects**

In Python, classes and objects are central to object-oriented programming. Here’s a guide on how to create and use them:

### **1. Creating a Class:**

A class is a blueprint for creating objects. It defines attributes (variables) and methods (functions) that the objects created from the class will have.

**Basic Structure:**
```python
class MyClass:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
    
    def method1(self):
        return f"Attribute1: {self.attribute1}, Attribute2: {self.attribute2}"
    
    def method2(self, value):
        return self.attribute1 * value
```

**Explanation:**
- **`__init__` Method:** Initializes an object with attributes.
- **`self`:** Refers to the instance of the class.

### **2. Creating an Object:**

To create an object, you instantiate the class by calling it with the required arguments.

**Example:**
```python
# Creating an object of MyClass
obj = MyClass(10, 20)
```

### **3. Accessing Attributes and Methods:**

You can access and modify attributes and call methods using the object.

**Example:**
```python
# Accessing attributes
print(obj.attribute1)  # Output: 10

# Calling methods
print(obj.method1())  # Output: Attribute1: 10, Attribute2: 20
print(obj.method2(5))  # Output: 50
```

### **4. Modifying Attributes:**

Attributes can be modified directly or through methods.

**Example:**
```python
# Modifying attributes
obj.attribute1 = 15
print(obj.method1())  # Output: Attribute1: 15, Attribute2: 20
```

### **5. Adding Class Methods and Static Methods:**

**Class Methods:** Operate on the class itself rather than on instances of the class. Use the `@classmethod` decorator.

**Static Methods:** Do not modify class or instance state. Use the `@staticmethod` decorator.

**Example:**
```python
class MyClass:
    count = 0
    
    def __init__(self, attribute1):
        self.attribute1 = attribute1
        MyClass.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count
    
    @staticmethod
    def greet():
        return "Hello, World!"

# Using class methods and static methods
print(MyClass.get_count())  # Output: Number of instances
print(MyClass.greet())      # Output: Hello, World!
```

### **6. Inheritance:**

You can create a new class that inherits from an existing class.

**Example:**
```python
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def bark(self):
        return "Woof!"

# Creating an object of the derived class
my_dog = Dog()
print(my_dog.speak())  # Output: Animal sound
print(my_dog.bark())   # Output: Woof!
```

### **7. Encapsulation and Private Attributes:**

Encapsulation hides the internal state and only exposes a controlled interface.

**Example:**
```python
class Person:
    def __init__(self, name):
        self.__name = name  # Private attribute

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

# Accessing private attributes via methods
person = Person("Alice")
print(person.get_name())  # Output: Alice
person.set_name("Bob")
print(person.get_name())  # Output: Bob
```

### **Summary:**

- **Creating a Class:** Define attributes and methods using the `class` keyword.
- **Creating Objects:** Instantiate the class using its constructor (`__init__` method).
- **Accessing Attributes/Methods:** Use dot notation (`obj.attribute`, `obj.method()`).
- **Modifying Attributes:** Directly or via methods.
- **Class and Static Methods:** Use `@classmethod` and `@staticmethod` decorators.
- **Inheritance:** Create derived classes that extend functionality.
- **Encapsulation:** Use private attributes and provide access through methods.

These principles help in designing modular and maintainable code using OOP.

======================================================================================

TODO:Methods and method types (instance,class,static)?

### **Methods and Method Types in Python**

In Python, methods are functions defined within a class that operate on instances or the class itself. There are three main types of methods: instance methods, class methods, and static methods.

### **1. Instance Methods**

**Definition:** Instance methods are the most common type of method. They operate on an instance of the class and can access and modify the instance's attributes.

**Syntax:**
```python
class MyClass:
    def __init__(self, value):
        self.value = value
    
    def instance_method(self):
        return f"Value is {self.value}"
```

**Usage:**
```python
obj = MyClass(10)
print(obj.instance_method())  # Output: Value is 10
```

**Key Points:**
- **First Parameter:** Always `self`, which refers to the instance of the class.
- **Access:** Can access and modify instance attributes.

### **2. Class Methods**

**Definition:** Class methods operate on the class itself rather than instances. They can modify class state that applies across all instances of the class.

**Syntax:**
```python
class MyClass:
    count = 0

    @classmethod
    def increment_count(cls):
        cls.count += 1
        return cls.count
```

**Usage:**
```python
print(MyClass.increment_count())  # Output: 1
print(MyClass.increment_count())  # Output: 2
```

**Key Points:**
- **First Parameter:** Always `cls`, which refers to the class itself.
- **Decorator:** Defined using the `@classmethod` decorator.
- **Access:** Can access and modify class attributes but not instance attributes.

### **3. Static Methods**

**Definition:** Static methods do not operate on an instance or the class. They are used for utility functions that don’t need to access or modify class or instance state.

**Syntax:**
```python
class MyClass:
    @staticmethod
    def static_method(param1, param2):
        return f"Parameters are {param1} and {param2}"
```

**Usage:**
```python
print(MyClass.static_method(5, 10))  # Output: Parameters are 5 and 10
```

**Key Points:**
- **No `self` or `cls`:** Does not take `self` or `cls` as the first parameter.
- **Decorator:** Defined using the `@staticmethod` decorator.
- **Access:** Cannot access or modify instance or class attributes.

### **Summary**

- **Instance Methods:**
  - **Definition:** Operate on an instance.
  - **First Parameter:** `self`.
  - **Access:** Instance attributes.
  
- **Class Methods:**
  - **Definition:** Operate on the class.
  - **First Parameter:** `cls`.
  - **Decorator:** `@classmethod`.
  - **Access:** Class attributes.

- **Static Methods:**
  - **Definition:** Independent of class or instance.
  - **No `self` or `cls`.**
  - **Decorator:** `@staticmethod`.
  - **Access:** Cannot access class or instance attributes.

Each method type serves a specific purpose and helps in organizing code effectively according to its functionality.

======================================================================================

TODO:Inheritance and subclasses?

### **Inheritance and Subclasses in Python**

Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class (subclass) to inherit attributes and methods from an existing class (superclass). This promotes code reuse and establishes a hierarchical relationship between classes.

### **1. Basic Inheritance**

**Definition:** Inheritance allows a subclass to inherit properties and methods from a superclass, enabling the subclass to reuse code.

**Example:**
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def bark(self):
        return "Woof!"
```

**Usage:**
```python
my_dog = Dog("Buddy")
print(my_dog.name)   # Output: Buddy (inherited from Animal)
print(my_dog.speak())  # Output: Animal sound (inherited from Animal)
print(my_dog.bark())   # Output: Woof! (defined in Dog)
```

### **2. Overriding Methods**

**Definition:** A subclass can provide a specific implementation of a method that is already defined in its superclass. This is called method overriding.

**Example:**
```python
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"
```

**Usage:**
```python
my_dog = Dog()
print(my_dog.speak())  # Output: Woof! (overrides Animal's speak method)
```

### **3. The `super()` Function**

**Definition:** `super()` allows you to call methods from the superclass from within the subclass, useful for extending or modifying inherited methods.

**Example:**
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the superclass constructor
        self.breed = breed

    def speak(self):
        return f"{super().speak()} - Woof!"
```

**Usage:**
```python
my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.name)   # Output: Buddy
print(my_dog.breed)  # Output: Golden Retriever
print(my_dog.speak())  # Output: Animal sound - Woof!
```

### **4. Multiple Inheritance**

**Definition:** A class can inherit from more than one base class. This is called multiple inheritance.

**Example:**
```python
class Animal:
    def speak(self):
        return "Animal sound"

class Pet:
    def play(self):
        return "Playing"

class Dog(Animal, Pet):
    def bark(self):
        return "Woof!"
```

**Usage:**
```python
my_dog = Dog()
print(my_dog.speak())  # Output: Animal sound (from Animal)
print(my_dog.play())   # Output: Playing (from Pet)
print(my_dog.bark())   # Output: Woof! (defined in Dog)
```

### **5. Abstract Base Classes (ABCs)**

**Definition:** Abstract base classes define methods that must be implemented by any subclass. They cannot be instantiated directly and are used to create a common interface.

**Example:**
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"
```

**Usage:**
```python
# This will raise an error:
# my_animal = Animal()

my_dog = Dog()
print(my_dog.speak())  # Output: Woof!
```

### **Summary**

- **Inheritance:** Allows a subclass to inherit attributes and methods from a superclass.
- **Overriding Methods:** A subclass can override methods from the superclass to provide specific behavior.
- **`super()`:** Used to call methods from the superclass and extend their functionality.
- **Multiple Inheritance:** A subclass can inherit from multiple superclasses.
- **Abstract Base Classes (ABCs):** Define methods that must be implemented by subclasses and cannot be instantiated directly.

Inheritance promotes code reuse and helps in building a logical hierarchy among classes, making the code more organized and maintainable.

======================================================================================

TODO:Method overriding and super()?

### **Method Overriding and `super()` in Python**

#### **1. Method Overriding**

**Definition:** Method overriding occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. This allows the subclass to alter or extend the behavior of the method inherited from the superclass.

**Example:**
```python
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"
```

**Usage:**
```python
my_dog = Dog()
print(my_dog.speak())  # Output: Woof! (overrides Animal's speak method)
```

**Key Points:**
- **Same Method Name:** The subclass method has the same name as the superclass method.
- **Polymorphism:** Allows different subclasses to have different implementations of the same method, facilitating polymorphism.

#### **2. The `super()` Function**

**Definition:** The `super()` function provides a way to call methods from a superclass from within a subclass. It is commonly used to extend or modify inherited methods, while still leveraging the functionality of the superclass.

**Syntax:**
```python
super().method_name()
```

**Example:**
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the superclass constructor
        self.breed = breed

    def speak(self):
        return f"{super().speak()} - Woof!"  # Call the superclass method and extend it
```

**Usage:**
```python
my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.name)     # Output: Buddy (inherited from Animal)
print(my_dog.breed)    # Output: Golden Retriever
print(my_dog.speak())  # Output: Animal sound - Woof! (extends the speak method)
```

**Key Points:**
- **Initialization (`__init__`):** Use `super()` to call the parent class’s constructor if the subclass constructor extends it.
- **Method Extension:** Use `super()` to call and extend the behavior of a method from the superclass.

#### **3. Example of Method Overriding and `super()` Together**

**Example:**
```python
class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)  # Initialize the Shape part
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def describe(self):
        return f"This is a {self.color} rectangle with area {self.area()}"

class ColoredRectangle(Rectangle):
    def __init__(self, color, width, height, border_color):
        super().__init__(color, width, height)  # Initialize Rectangle part
        self.border_color = border_color

    def describe(self):
        base_description = super().describe()  # Call describe from Rectangle
        return f"{base_description} and a border color of {self.border_color}"
```

**Usage:**
```python
rect = ColoredRectangle("red", 10, 5, "black")
print(rect.describe())  
# Output: This is a red rectangle with area 50 and a border color of black
```

**Summary:**
- **Method Overriding:** Subclass provides a new implementation of a method inherited from the superclass.
- **`super()`:** Calls methods from the superclass to extend or modify their functionality, and to access the superclass's attributes and methods.

Together, these concepts allow for flexible and reusable code by enabling subclasses to tailor inherited behavior and utilize superclass functionality effectively.

======================================================================================

TODO:Polymorphism and method overloading?

### **Polymorphism and Method Overloading in Python**

#### **1. Polymorphism**

**Definition:** Polymorphism is a programming concept that allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different underlying forms (data types). In Python, polymorphism is often achieved through method overriding and dynamic method dispatch.

**Types of Polymorphism:**
- **Method Overriding:** Subclasses provide a specific implementation of a method that is already defined in their superclass. 

**Example:**
```python
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def make_animal_speak(animal):
    print(animal.speak())

# Using polymorphism
animals = [Dog(), Cat()]
for animal in animals:
    make_animal_speak(animal)
```

**Output:**
```
Woof!
Meow!
```

**Key Points:**
- **Single Interface:** The `make_animal_speak` function uses the same interface (`speak` method) to interact with different types of animals.
- **Dynamic Dispatch:** Python dynamically determines which `speak` method to call based on the object's type.

#### **2. Method Overloading**

**Definition:** Method overloading allows multiple methods with the same name but different signatures (different parameters) within the same class. However, Python does not support method overloading in the traditional sense. Instead, Python provides a single method with flexible parameters.

**Python Approach to Overloading:**

In Python, you achieve a similar effect using default arguments, variable-length arguments (`*args`, `**kwargs`), and type checking within methods.

**Example Using Default Arguments:**
```python
class Printer:
    def print_message(self, message="Hello, World!", times=1):
        for _ in range(times):
            print(message)

# Using method with default arguments
printer = Printer()
printer.print_message()           # Output: Hello, World!
printer.print_message("Hi!")      # Output: Hi!
printer.print_message("Hi!", 3)   # Output: Hi! Hi! Hi!
```

**Example Using Variable-Length Arguments:**
```python
class Calculator:
    def add(self, *args):
        return sum(args)

# Using method with variable-length arguments
calc = Calculator()
print(calc.add(1, 2))            # Output: 3
print(calc.add(1, 2, 3, 4, 5))  # Output: 15
```

**Example Using Type Checking:**
```python
class Processor:
    def process(self, data):
        if isinstance(data, str):
            return f"Processing string: {data}"
        elif isinstance(data, int):
            return f"Processing integer: {data}"
        else:
            return "Unsupported data type"

# Using method with type checking
proc = Processor()
print(proc.process("text"))  # Output: Processing string: text
print(proc.process(42))      # Output: Processing integer: 42
```

**Key Points:**
- **Single Method with Flexible Parameters:** Define a method with default arguments or use variable-length arguments.
- **Type Checking:** Implement logic within the method to handle different types of inputs.

#### **Summary**

- **Polymorphism:** Allows different classes to be treated through a common interface, enabling flexible and reusable code. Achieved via method overriding and dynamic method dispatch.
- **Method Overloading:** Python does not support traditional method overloading but achieves similar functionality through default arguments, variable-length arguments, and type checking.

Both concepts facilitate code flexibility and adaptability, making it easier to work with various types and perform operations in a consistent manner.

======================================================================================

TODO:Encapsulation and date hiding?

### **Encapsulation and Data Hiding in Python**

#### **1. Encapsulation**

**Definition:** Encapsulation is an OOP principle that involves bundling data (attributes) and methods (functions) that operate on the data into a single unit or class. It also involves restricting direct access to some of the object's components, which is known as data hiding.

**Purpose:**
- **Organize Code:** Encapsulation helps in organizing code by grouping related attributes and methods together.
- **Control Access:** It provides control over how attributes are accessed and modified, enhancing the integrity and security of data.

**Example:**
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Private attribute

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            raise ValueError("Salary must be positive")

# Usage
emp = Employee("John", 50000)
print(emp.name)  # Output: John
print(emp.get_salary())  # Output: 50000

emp.set_salary(60000)
print(emp.get_salary())  # Output: 60000

# Direct access to private attribute (not recommended)
# print(emp.__salary)  # Raises AttributeError
```

**Key Points:**
- **Private Attributes:** Use double underscores (`__`) to declare private attributes that should not be accessed directly.
- **Getter and Setter Methods:** Provide methods to access and modify private attributes, enforcing validation and control.

#### **2. Data Hiding**

**Definition:** Data hiding is a concept where the internal state of an object is hidden from the outside. It is achieved by making attributes private and only exposing them through public methods. This ensures that the object's internal state cannot be directly modified or accessed, protecting it from unintended changes and misuse.

**Levels of Data Hiding in Python:**
- **Public:** Attributes and methods accessible from outside the class.
- **Protected:** Attributes and methods intended for internal use by the class and its subclasses (conventionally denoted by a single underscore `_`).
- **Private:** Attributes and methods intended to be hidden from outside access (denoted by double underscores `__`).

**Example:**
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError("Insufficient funds or invalid amount")

    def get_balance(self):
        return self.__balance

# Usage
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500

# Attempting direct access to private attribute (not recommended)
# print(account.__balance)  # Raises AttributeError
```

**Key Points:**
- **Public Access:** Allowed directly.
- **Protected Access:** Conventionally used to indicate attributes or methods intended for internal use (`_attribute`).
- **Private Access:** Restricted, with access provided through public methods (`__attribute`).

#### **Summary**

- **Encapsulation:** Bundles data and methods into a class and controls access to the data through public methods.
- **Data Hiding:** Hides the internal state of an object from direct access, using private attributes and methods to protect the integrity of the object's state.

These concepts help in building robust and maintainable code by ensuring that an object's internal state is controlled and manipulated only through well-defined interfaces.

======================================================================================

TODO:Special Methods (dunder methods)?

### **Special Methods (Dunder Methods) in Python**

Special methods, also known as "dunder" (double underscore) methods, are predefined methods in Python that start and end with double underscores. They allow you to define how objects of a class behave with built-in operations and functions. These methods are used to implement operator overloading, object representation, and more.

### **Common Special Methods**

#### **1. Initialization and Representation**

- **`__init__(self, ...)`**
  - **Purpose:** Constructor; initializes an instance of the class.
  - **Example:**
    ```python
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    ```

- **`__repr__(self)`**
  - **Purpose:** Provides a string representation of the object for debugging; intended to be unambiguous.
  - **Example:**
    ```python
    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age!r})"
    ```

- **`__str__(self)`**
  - **Purpose:** Provides a string representation of the object for end-users; intended to be readable.
  - **Example:**
    ```python
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    ```

#### **2. Comparison Operators**

- **`__eq__(self, other)`**
  - **Purpose:** Implements equality comparison (`==`).
  - **Example:**
    ```python
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
    ```

- **`__ne__(self, other)`**
  - **Purpose:** Implements inequality comparison (`!=`).
  - **Example:**
    ```python
    def __ne__(self, other):
        return not (self == other)
    ```

- **`__lt__(self, other)`**
  - **Purpose:** Implements less than comparison (`<`).
  - **Example:**
    ```python
    def __lt__(self, other):
        return self.age < other.age
    ```

- **`__le__(self, other)`**
  - **Purpose:** Implements less than or equal to comparison (`<=`).
  - **Example:**
    ```python
    def __le__(self, other):
        return self.age <= other.age
    ```

- **`__gt__(self, other)`**
  - **Purpose:** Implements greater than comparison (`>`).
  - **Example:**
    ```python
    def __gt__(self, other):
        return self.age > other.age
    ```

- **`__ge__(self, other)`**
  - **Purpose:** Implements greater than or equal to comparison (`>=`).
  - **Example:**
    ```python
    def __ge__(self, other):
        return self.age >= other.age
    ```

#### **3. Arithmetic Operators**

- **`__add__(self, other)`**
  - **Purpose:** Implements addition (`+`).
  - **Example:**
    ```python
    def __add__(self, other):
        return self.age + other.age
    ```

- **`__sub__(self, other)`**
  - **Purpose:** Implements subtraction (`-`).
  - **Example:**
    ```python
    def __sub__(self, other):
        return self.age - other.age
    ```

- **`__mul__(self, other)`**
  - **Purpose:** Implements multiplication (`*`).
  - **Example:**
    ```python
    def __mul__(self, other):
        return self.age * other.age
    ```

- **`__truediv__(self, other)`**
  - **Purpose:** Implements division (`/`).
  - **Example:**
    ```python
    def __truediv__(self, other):
        return self.age / other.age
    ```

#### **4. Container Methods**

- **`__len__(self)`**
  - **Purpose:** Returns the length of the container.
  - **Example:**
    ```python
    def __len__(self):
        return len(self.items)
    ```

- **`__getitem__(self, key)`**
  - **Purpose:** Implements indexing (`[]`).
  - **Example:**
    ```python
    def __getitem__(self, key):
        return self.items[key]
    ```

- **`__setitem__(self, key, value)`**
  - **Purpose:** Implements item assignment (`[]`).
  - **Example:**
    ```python
    def __setitem__(self, key, value):
        self.items[key] = value
    ```

- **`__delitem__(self, key)`**
  - **Purpose:** Implements item deletion (`del []`).
  - **Example:**
    ```python
    def __delitem__(self, key):
        del self.items[key]
    ```

#### **5. Context Management**

- **`__enter__(self)`**
  - **Purpose:** Enter the runtime context related to this object (used in `with` statements).
  - **Example:**
    ```python
    def __enter__(self):
        return self
    ```

- **`__exit__(self, exc_type, exc_value, traceback)`**
  - **Purpose:** Exit the runtime context related to this object.
  - **Example:**
    ```python
    def __exit__(self, exc_type, exc_value, traceback):
        pass
    ```

### **Summary**

- **Initialization and Representation:**
  - `__init__(self, ...)`: Constructor.
  - `__repr__(self)`: Unambiguous string representation.
  - `__str__(self)`: Readable string representation.

- **Comparison Operators:**
  - `__eq__(self, other)`: Equality.
  - `__ne__(self, other)`: Inequality.
  - `__lt__(self, other)`: Less than.
  - `__le__(self, other)`: Less than or equal to.
  - `__gt__(self, other)`: Greater than.
  - `__ge__(self, other)`: Greater than or equal to.

- **Arithmetic Operators:**
  - `__add__(self, other)`: Addition.
  - `__sub__(self, other)`: Subtraction.
  - `__mul__(self, other)`: Multiplication.
  - `__truediv__(self, other)`: Division.

- **Container Methods:**
  - `__len__(self)`: Length.
  - `__getitem__(self, key)`: Indexing.
  - `__setitem__(self, key, value)`: Item assignment.
  - `__delitem__(self, key)`: Item deletion.

- **Context Management:**
  - `__enter__(self)`: Enter context.
  - `__exit__(self, exc_type, exc_value, traceback)`: Exit context.

Special methods provide the hooks needed to customize and control how objects interact with built-in Python operations and syntax.

======================================================================================

"""