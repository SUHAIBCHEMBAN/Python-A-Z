"""
TODO:Defining and calling functions?

### **Defining Functions:**
To define a function in Python, use the `def` keyword followed by the function name, parameters in parentheses, and a colon. The code block within the function is indented.

**Syntax:**
```python
def function_name(parameter1, parameter2):
    # Code block
    return result
```

**Example:**
```python
def add(a, b):
    return a + b
```

### **Calling Functions:**
To call a function, use its name followed by arguments in parentheses.

**Syntax:**
```python
result = function_name(arg1, arg2)
```

**Example:**
```python
sum = add(5, 3)  # Output: 8
```

### **Default Arguments:**
You can provide default values for parameters.

**Example:**
```python
def greet(name="World"):
    return f"Hello, {name}!"
```

**Calling:**
```python
print(greet())          # Output: "Hello, World!"
print(greet("Alice"))   # Output: "Hello, Alice!"
```

### **Keyword Arguments:**
You can specify arguments by name.

**Example:**
```python
def power(base, exponent=2):
    return base ** exponent
```

**Calling:**
```python
print(power(3))           # Output: 9 (3^2)
print(power(3, exponent=3))  # Output: 27 (3^3)
```

Functions allow you to encapsulate and reuse code efficiently.

======================================================================================

TODO:Function parameters and arguments?

### **Function Parameters:**
- **Parameters** are placeholders defined in a function signature that specify what kind of inputs the function can accept.
- They are defined when you create the function.

**Example:**
```python
def greet(name, message):
    print(f"{message}, {name}!")
```
Here, `name` and `message` are parameters.

### **Function Arguments:**
- **Arguments** are the actual values you pass to a function when you call it. These values are assigned to the corresponding parameters.

**Example:**
```python
greet("Alice", "Hello")
```
Here, `"Alice"` and `"Hello"` are arguments.

### **Types of Arguments:**
1. **Positional Arguments:** Passed in the order of the parameters.
   ```python
   greet("Alice", "Hi")  # Output: "Hi, Alice!"
   ```

2. **Keyword Arguments:** Passed by explicitly naming the parameter.
   ```python
   greet(message="Good morning", name="Bob")  # Output: "Good morning, Bob!"
   ```

3. **Default Arguments:** Parameters with default values that can be overridden.
   ```python
   def greet(name, message="Hello"):
       print(f"{message}, {name}!")
   greet("Charlie")  # Output: "Hello, Charlie!"
   ```

4. **Arbitrary Arguments (`*args`):** Allows passing a variable number of positional arguments.
   ```python
   def add(*args):
       return sum(args)
   print(add(1, 2, 3))  # Output: 6
   ```

5. **Arbitrary Keyword Arguments (`**kwargs`):** Allows passing a variable number of keyword arguments.
   ```python
   def display_info(**kwargs):
       for key, value in kwargs.items():
           print(f"{key}: {value}")
   display_info(name="Alice", age=30)  # Output: name: Alice, age: 30
   ```

Parameters define what arguments a function expects, and arguments are the actual data you pass to those parameters.

======================================================================================

TODO:Scope and lifetime of variables?

### **Scope of Variables:**
- **Scope** refers to the region of the code where a variable is accessible.

1. **Local Scope:**
   - Variables defined inside a function are **local** to that function.
   - They can only be accessed within the function.
   ```python
   def my_function():
       local_var = 10  # Local scope
       print(local_var)

   my_function()
   print(local_var)  # Error: local_var is not defined outside the function
   ```

2. **Global Scope:**
   - Variables defined outside any function are **global**.
   - They can be accessed anywhere in the code, including inside functions.
   ```python
   global_var = 20  # Global scope

   def my_function():
       print(global_var)  # Accessible within the function

   my_function()
   ```

3. **Enclosing Scope:**
   - Applies to nested functions. The inner function can access variables from its enclosing function.
   ```python
   def outer_function():
       enclosing_var = "Hello"

       def inner_function():
           print(enclosing_var)  # Accessing enclosing scope
       
       inner_function()

   outer_function()
   ```

4. **Built-in Scope:**
   - Refers to the built-in names in Python like `len()`, `print()`, etc.

### **Lifetime of Variables:**
- **Local Variables:** Exist only during the execution of the function. Once the function exits, the local variables are destroyed.
  ```python
  def my_function():
      local_var = 10  # Created when the function is called
      print(local_var)
  my_function()       # local_var is destroyed after function ends
  ```

- **Global Variables:** Exist for the lifetime of the program, from when they are defined until the program terminates.
  ```python
  global_var = 20  # Created when the script runs and lasts until it ends
  ```

### **Modifying Global Variables:**
- Use the `global` keyword to modify a global variable inside a function.
  ```python
  count = 0

  def increment():
      global count
      count += 1

  increment()
  print(count)  # Output: 1
  ```

**Summary:**  
- **Scope** determines where a variable can be accessed.
- **Lifetime** refers to how long a variable exists in memory.

======================================================================================

TODO:Return values and mutiple return statements?

### **Return Values:**
- **Return values** are the outputs a function provides after it finishes execution.
- Use the `return` keyword to send a value back to the caller.

**Example:**
```python
def add(a, b):
    return a + b

result = add(5, 3)  # Output: 8
```

### **Multiple Return Statements:**
- A function can have multiple `return` statements, but only one will execute, depending on the flow of control.
- The function exits as soon as a `return` statement is executed.

**Example:**
```python
def check_number(x):
    if x > 0:
        return "Positive"
    elif x < 0:
        return "Negative"
    else:
        return "Zero"

print(check_number(10))  # Output: "Positive"
print(check_number(-5))  # Output: "Negative"
print(check_number(0))   # Output: "Zero"
```

### **Returning Multiple Values:**
- Python allows a function to return multiple values as a tuple.

**Example:**
```python
def get_stats(a, b):
    sum = a + b
    diff = a - b
    return sum, diff  # Returning a tuple

result = get_stats(10, 5)
print(result)        # Output: (15, 5)

sum, diff = get_stats(10, 5)
print(sum, diff)     # Output: 15 5
```

**Summary:**
- **Single return:** Ends the function and returns a value.
- **Multiple return statements:** Allows different paths in the function to return different values.
- **Returning multiple values:** Packs them into a tuple for easy access.

======================================================================================

TODO:Anonymous functions (lamda functions)?

### **Anonymous Functions (Lambda Functions):**
- **Lambda functions** are small, unnamed functions defined using the `lambda` keyword in Python.
- They can have any number of arguments but only one expression, which is evaluated and returned.
- Commonly used for short, simple functions that are used temporarily, often within higher-order functions like `map()`, `filter()`, or `sorted()`.

### **Syntax:**
```python
lambda arguments: expression
```

### **Example:**
```python
# A lambda function that adds 10 to a number
add_10 = lambda x: x + 10
print(add_10(5))  # Output: 15
```

### **Using Lambda Functions with Built-in Functions:**

1. **With `map()`:**
   - Applies a function to all items in an iterable.
   ```python
   numbers = [1, 2, 3, 4]
   squares = map(lambda x: x**2, numbers)
   print(list(squares))  # Output: [1, 4, 9, 16]
   ```

2. **With `filter()`:**
   - Filters elements based on a condition.
   ```python
   numbers = [1, 2, 3, 4, 5, 6]
   even_numbers = filter(lambda x: x % 2 == 0, numbers)
   print(list(even_numbers))  # Output: [2, 4, 6]
   ```

3. **With `sorted()`:**
   - Sorts items based on a key function.
   ```python
   points = [(1, 2), (3, 1), (5, -1)]
   sorted_points = sorted(points, key=lambda x: x[1])
   print(sorted_points)  # Output: [(5, -1), (3, 1), (1, 2)]
   ```

### **Key Points:**
- **Anonymous:** Lambda functions do not have a name, making them ideal for short-term use.
- **Single Expression:** They can only contain a single expression, not multiple statements.
- **Use Cases:** Ideal for simple operations like sorting, filtering, or mapping.

Lambda functions are a concise way to create small, throwaway functions in Python.

======================================================================================

TODO:Modules and importing modules?

### **Modules:**
- **Modules** are files containing Python code (functions, classes, variables) that can be reused in other Python programs.
- A module allows you to organize your code into separate files for better maintainability and readability.

### **Creating a Module:**
- Simply save a `.py` file with the functions, classes, or variables you want to reuse.
  
**Example:**
```python
# my_module.py
def greet(name):
    return f"Hello, {name}!"
```

### **Importing Modules:**
- You can import a module into another Python script to use its content.

### **Basic Import:**
```python
import my_module
print(my_module.greet("Alice"))  # Output: Hello, Alice!
```

### **Import Specific Items:**
- Import specific functions, classes, or variables from a module.
```python
from my_module import greet
print(greet("Bob"))  # Output: Hello, Bob!
```

### **Import with Alias:**
- Use an alias to rename the module or function for easier access.
```python
import my_module as mm
print(mm.greet("Charlie"))  # Output: Hello, Charlie!
```

### **Importing All Items:**
- Import everything from a module (not recommended for large modules to avoid conflicts).
```python
from my_module import *
print(greet("Dave"))  # Output: Hello, Dave!
```

### **Built-in Modules:**
- Python comes with many built-in modules, like `math`, `os`, `datetime`.
  
**Example:**
```python
import math
print(math.sqrt(16))  # Output: 4.0
```

### **Installing External Modules:**
- Use `pip`, Python’s package manager, to install and import external modules.
  
**Example:**
```bash
pip install requests
```
```python
import requests
response = requests.get("https://api.example.com")
print(response.status_code)
```

### **Module Search Path:**
- Python searches for modules in the following order:
  1. The directory of the script being run.
  2. Directories listed in the `PYTHONPATH` environment variable.
  3. Default system paths (e.g., standard library paths).

Modules are a fundamental way to structure and reuse code in Python, making it easy to manage larger projects by separating functionality into different files.

======================================================================================

TODO:Exploring built-in modules (math,random,detatime)?

### **Exploring Built-in Modules:**

Python provides several built-in modules to perform various tasks, such as mathematical operations, generating random numbers, and working with dates and times.

### **1. `math` Module:**
- **Purpose:** Provides mathematical functions and constants.

**Common Functions:**
```python
import math

# Square root
print(math.sqrt(16))  # Output: 4.0

# Power
print(math.pow(2, 3))  # Output: 8.0

# Trigonometric functions
print(math.sin(math.pi / 2))  # Output: 1.0

# Constants
print(math.pi)   # Output: 3.141592653589793
print(math.e)    # Output: 2.718281828459045
```

### **2. `random` Module:**
- **Purpose:** Generates random numbers and performs random operations.

**Common Functions:**
```python
import random

# Generate a random float between 0.0 and 1.0
print(random.random())  # Output: e.g., 0.37444887175646646

# Generate a random integer within a range
print(random.randint(1, 10))  # Output: e.g., 7

# Choose a random element from a list
choices = ['apple', 'banana', 'cherry']
print(random.choice(choices))  # Output: e.g., 'banana'

# Shuffle a list
random.shuffle(choices)
print(choices)  # Output: e.g., ['cherry', 'banana', 'apple']

# Generate a random sample from a list
print(random.sample(choices, 2))  # Output: e.g., ['banana', 'apple']
```

### **3. `datetime` Module:**
- **Purpose:** Provides classes for manipulating dates and times.

**Common Functions and Classes:**
```python
import datetime

# Get the current date and time
now = datetime.datetime.now()
print(now)  # Output: e.g., 2024-08-26 10:15:42.123456

# Get the current date
today = datetime.date.today()
print(today)  # Output: e.g., 2024-08-26

# Create a specific date
birthday = datetime.date(1990, 5, 15)
print(birthday)  # Output: 1990-05-15

# Calculate the difference between dates
days_until_birthday = birthday - today
print(days_until_birthday.days)  # Output: e.g., -12500

# Format dates as strings
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)  # Output: e.g., "2024-08-26 10:15:42"
```

### **Summary:**
- **`math` Module:** Ideal for advanced mathematical calculations.
- **`random` Module:** Useful for generating random data, making choices, or simulating randomness.
- **`datetime` Module:** Essential for managing and manipulating date and time information.

These modules are versatile tools in Python, enabling a wide range of functionalities without needing to install additional packages.

======================================================================================

TODO:Creating and using custom modules?

### **Creating and Using Custom Modules:**

**1. Create a Custom Module:**

1. **Define the Module:**
   - Create a Python file (`.py`) with functions, classes, or variables.

   **Example (`my_module.py`):**
   ```python
   def greet(name):
       return f"Hello, {name}!"

   def add(a, b):
       return a + b
   ```

2. **Save the File:**
   - Save the file with a `.py` extension, e.g., `my_module.py`.

**2. Use the Custom Module:**

1. **Import the Module:**
   - Use the `import` statement in another Python script to access the module's functions or classes.

   **Example:**
   ```python
   import my_module

   print(my_module.greet("Alice"))  # Output: Hello, Alice!
   print(my_module.add(5, 3))       # Output: 8
   ```

2. **Import Specific Items:**
   - Import specific functions or classes from the module.

   **Example:**
   ```python
   from my_module import greet

   print(greet("Bob"))  # Output: Hello, Bob!
   ```

3. **Use Aliases:**
   - Rename the module or functions for easier access.

   **Example:**
   ```python
   import my_module as mm

   print(mm.greet("Charlie"))  # Output: Hello, Charlie!
   ```

### **Summary:**
- **Create:** Define a `.py` file with desired functions/classes.
- **Use:** Import and call functions/classes from the module in other scripts.

======================================================================================

TODO:Package management and virtual environments?

### **Package Management:**

**1. **Installing Packages:**
   - Use `pip`, Python's package manager, to install packages from the Python Package Index (PyPI).

   **Command:**
   ```bash
   pip install package_name
   ```
   **Example:**
   ```bash
   pip install requests
   ```

**2. **Uninstalling Packages:**
   - Remove packages with `pip uninstall`.

   **Command:**
   ```bash
   pip uninstall package_name
   ```

**3. **Listing Installed Packages:**
   - List all installed packages with `pip list`.

   **Command:**
   ```bash
   pip list
   ```

**4. **Freezing Dependencies:**
   - Save the current environment’s packages to a `requirements.txt` file.

   **Command:**
   ```bash
   pip freeze > requirements.txt
   ```

   - Install packages from `requirements.txt` using:

   **Command:**
   ```bash
   pip install -r requirements.txt
   ```

### **Virtual Environments:**

**1. **Creating a Virtual Environment:**
   - Isolate project dependencies to avoid conflicts.

   **Command:**
   ```bash
   python -m venv env
   ```

   - This creates a directory named `env` with a separate Python environment.

**2. **Activating the Virtual Environment:**
   - Activate the environment to use its packages.

   **Windows:**
   ```bash
   env\Scripts\activate
   ```

   **macOS/Linux:**
   ```bash
   source env/bin/activate
   ```

**3. **Deactivating the Virtual Environment:**
   - Return to the global Python environment.

   **Command:**
   ```bash
   deactivate
   ```

**4. **Managing Dependencies in Virtual Environments:**
   - Use `pip` within the virtual environment to install and manage packages.

**Example:**
```bash
pip install flask
```

### **Summary:**
- **Package Management:** Use `pip` to install, uninstall, list, and freeze packages.
- **Virtual Environments:** Create isolated environments to manage project-specific dependencies using `venv` and `pip`.

======================================================================================

"""
