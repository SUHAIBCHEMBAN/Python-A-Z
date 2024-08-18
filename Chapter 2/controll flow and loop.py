"""
TODO:Conditional statements (if, elif, else)?

Conditional statements control the flow of execution based on conditions:

- **`if`**: Executes code if the condition is `True`.
- **`elif`**: Checks another condition if the previous one is `False`.
- **`else`**: Executes code if none of the conditions are `True`.

**Example:**
```python
if x > 10:
    # Code for x > 10
elif x == 10:
    # Code for x == 10
else:
    # Code for x < 10
```

TODO:Looping structures (for, while)?

Looping structures allow repeated execution of code:

- **`for` Loop**: Iterates over a sequence (like a list or range).
  ```python
  for item in sequence:
      # Code to execute
  ```

- **`while` Loop**: Repeats as long as a condition is `True`.
  ```python
  while condition:
      # Code to execute
  ```

TODO:Iteration and iterable objects?

- **Iteration:** The process of looping through elements in a collection (like a list, tuple, or string) one at a time.

- **Iterable Objects:** Objects that can be looped over (e.g., lists, tuples, strings, dictionaries). They implement the `__iter__()` method, returning an iterator.

**Example:**
```python
my_list = [1, 2, 3]
for item in my_list:  # Iteration
    print(item)
```

TODO:Range and xrange functions?

- **`range()` Function:** Generates a sequence of numbers in Python 3. It returns a range object (an immutable sequence), which can be iterated over.

  **Example:**
  ```python
  for i in range(5):
      print(i)
  ```
  **Output:**
  ```
  0
  1
  2
  3
  4
  ```

- **`xrange()` Function:** Exists only in Python 2. It behaves like `range()` but generates numbers on-the-fly (like an iterator) and is more memory-efficient for large ranges.

  In Python 3, `xrange()` is replaced by `range()`, which has the same memory-efficient behavior.


TODO:Control flow keywords (break, continue, pass)?

Control flow keywords manage the flow of loops:

- **`break`:** Exits the loop immediately, stopping further iterations.
  ```python
  for i in range(5):
      if i == 3:
          break
      print(i)
  ```
  **Output:**
  ```
  0
  1
  2
  ```

- **`continue`:** Skips the current iteration and moves to the next one.
  ```python
  for i in range(5):
      if i == 3:
          continue
      print(i)
  ```
  **Output:**
  ```
  0
  1
  2
  4
  ```

- **`pass`:** Does nothing and acts as a placeholder in code where a statement is syntactically required but no action is needed.
  ```python
  for i in range(5):
      if i == 3:
          pass  # No action
      print(i)
  ```
  **Output:**
  ```
  0
  1
  2
  3
  4
  ```


TODO:Exception handling with try-except blocks?

**Exception handling** in Python is done using `try-except` blocks to catch and handle errors gracefully:

- **`try`:** Code that may raise an exception is placed here.
- **`except`:** Code that runs if an exception occurs in the `try` block.

**Example:**
```python
try:
    x = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero")
```

**Output:**
```
Cannot divide by zero
```

You can also catch multiple exceptions or use a general `except` to catch any exception.


TODO:Handling common exceptions?

Here’s how to handle some common exceptions in Python:

- **`ZeroDivisionError`:** Raised when dividing by zero.
  ```python
  try:
      result = 10 / 0
  except ZeroDivisionError:
      print("Cannot divide by zero")
  ```

- **`TypeError`:** Raised when an operation is applied to an incompatible type.
  ```python
  try:
      result = "2" + 2
  except TypeError:
      print("Cannot add a string and an integer")
  ```

- **`ValueError`:** Raised when a function receives an argument of the right type but inappropriate value.
  ```python
  try:
      number = int("abc")
  except ValueError:
      print("Invalid value for conversion to int")
  ```

- **`FileNotFoundError`:** Raised when trying to open a file that doesn't exist.
  ```python
  try:
      file = open("nonexistent_file.txt")
  except FileNotFoundError:
      print("File not found")
  ```

These exceptions allow you to manage errors and maintain program stability.


TODO:Raising custom exceptions?

You can raise custom exceptions in Python using the `raise` keyword, typically with a custom exception class that inherits from Python's built-in `Exception` class.

### **Example of Raising a Custom Exception:**
```python
class MyCustomError(Exception):
    ***Custom exception for specific errors.***
    pass

def check_value(value):
    if value < 0:
        raise MyCustomError("Negative value not allowed!")

try:
    check_value(-1)
except MyCustomError as e:
    print(e)
```

**Output:**
```
Negative value not allowed!
```

This allows you to create meaningful exceptions tailored to your application's needs.

"""