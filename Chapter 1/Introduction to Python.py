"""
What is python and it's history?

Python is a high-level, interpreted programming language known for its readability and simplicity. It was created by Guido van Rossum and first released in 1991. Python was designed to emphasize code readability, making it easier to write and maintain. Over time, it has become one of the most popular languages for web development, data analysis, automation, and more.

======================================================================================

Unique features and advantages of Python?

1. **Readability:** Simple, clean syntax that makes code easy to read and write.
2. **Versatility:** Supports various programming paradigms—object-oriented, procedural, and functional.
3. **Extensive Libraries:** A vast standard library and many third-party modules for diverse applications.
4. **Cross-Platform:** Runs on multiple operating systems, including Windows, macOS, and Linux.
5. **Strong Community Support:** A large, active community contributes to continuous development and resource availability.
6. **Integration:** Easily integrates with other languages and tools.
7. **Ease of Learning:** Great for beginners due to its simplicity and clear syntax.

======================================================================================

Python 2 vs. Python 3?

- **Release Date:** Python 2 was released in 2000, Python 3 in 2008.
- **Syntax Differences:** Python 3 introduced changes like `print` as a function (`print()`) instead of a statement.
- **Unicode:** Python 3 uses Unicode by default for strings, improving internationalization support.
- **Backward Compatibility:** Python 3 is not fully backward-compatible with Python 2, leading to challenges in porting code.
- **End of Life:** Python 2 reached end-of-life in January 2020, meaning it no longer receives updates or security patches.

Python 3 is the future of the language, with ongoing development and new features.

======================================================================================

Python identifiers, keywords, and indentation?

- **Identifiers:** Names used to identify variables, functions, classes, etc., in Python. They must start with a letter (a-z, A-Z) or an underscore (_), followed by letters, digits, or underscores. They are case-sensitive.

- **Keywords:** Reserved words in Python that have special meanings, like `if`, `else`, `while`, `for`, `def`, `class`, etc. These cannot be used as identifiers.

- **Indentation:** Python uses indentation (spaces or tabs) to define the structure of code blocks, like loops, functions, and conditionals. Consistent indentation is crucial, as it replaces the need for braces `{}` found in other languages.

======================================================================================

Comments and documentation strings?

- **Comments:** In Python, comments are used to explain code and are ignored by the interpreter. They start with a `#` symbol. Example: `# This is a comment`.

- **Documentation Strings (Docstrings):** Special multiline comments used to document functions, classes, or modules. They are enclosed in triple quotes (`""" """` or `''' '''`). Docstrings can be accessed with the `__doc__` attribute. Example:

  ```python
  def example_function():
      #This function does something.
      pass
  ```
======================================================================================

Command line arguments and user input?

- **Command Line Arguments:** These are inputs passed to a Python script from the command line. They can be accessed using the `sys.argv` list from the `sys` module, where `sys.argv[0]` is the script name and the subsequent elements are the arguments.

  Example:
  ```python
  import sys
  print(sys.argv)
  ```

- **User Input:** Python uses the `input()` function to get input from the user during script execution. The input is returned as a string.

  Example:
  ```python
  name = input("Enter your name: ")
  print("Hello, " + name)
  ```

======================================================================================

interpreter vs compiler?

- **Interpreter:** Translates and executes code line by line. Python uses an interpreter, allowing for immediate execution of code without needing a complete compiled file. This enables easier debugging but can be slower in execution.

- **Compiler:** Translates the entire code into machine language before execution. Compiled languages (like C or Java) typically run faster since the code is already translated, but they require a separate compilation step before running the program.


======================================================================================

Python data types and variables?

- **Data Types:** Python supports various built-in data types, including:
  - **Numbers:** `int` (integers), `float` (floating-point numbers), and `complex` (complex numbers).
  - **Strings:** Text data, represented with quotes (`'Hello'` or `"Hello"`).
  - **Lists:** Ordered, mutable collections (`[1, 2, 3]`).
  - **Tuples:** Ordered, immutable collections (`(1, 2, 3)`).
  - **Dictionaries:** Key-value pairs (`{'key': 'value'}`).
  - **Sets:** Unordered collections of unique elements (`{1, 2, 3}`).
  - **Booleans:** `True` or `False`.

- **Variables:** Names that store data values. They are created by assigning a value using `=`. Example:
  ```python
  age = 25
  name = "Alice"
  ```  
Python variables are dynamically typed, meaning you don't need to declare the type explicitly.

======================================================================================

Core built-in objects and functions?

Python has several core built-in objects and functions that are essential for programming. Here are some key ones:

### Core Built-in Objects:
- **`int`, `float`, `complex`:** Numeric types for integers, floating-point numbers, and complex numbers.
- **`str`:** String type for text.
- **`list`:** Ordered, mutable collections of items.
- **`tuple`:** Ordered, immutable collections.
- **`dict`:** Dictionary type for key-value pairs.
- **`set`:** Unordered collection of unique items.
- **`bool`:** Boolean type (`True` or `False`).
- **`None`:** Represents the absence of a value or a null value.

### Core Built-in Functions:
- **`print()`:** Outputs text or data to the console.
- **`len()`:** Returns the length of an object (like a list, string, or tuple).
- **`type()`:** Returns the type of an object.
- **`input()`:** Reads input from the user.
- **`range()`:** Generates a sequence of numbers, often used in loops.
- **`sum()`:** Returns the sum of an iterable's elements.
- **`min()`, `max()`:** Return the smallest and largest items in an iterable.
- **`abs()`:** Returns the absolute value of a number.
- **`round()`:** Rounds a number to a specified number of decimal places.
- **`sorted()`:** Returns a sorted list from an iterable.
- **`open()`:** Opens a file and returns a file object.
- **`enumerate()`:** Adds a counter to an iterable, returning it as an enumerate object.


======================================================================================

Numbers and mathematical operations?

Python supports various numerical operations and types:

### Numeric Types:
- **`int`:** Integer values (e.g., `5`, `-3`).
- **`float`:** Floating-point numbers for decimals (e.g., `3.14`, `-0.001`).
- **`complex`:** Complex numbers with real and imaginary parts (e.g., `2 + 3j`).

### Mathematical Operations:
- **Addition:** `+` (e.g., `5 + 3` results in `8`)
- **Subtraction:** `-` (e.g., `5 - 3` results in `2`)
- **Multiplication:** `*` (e.g., `5 * 3` results in `15`)
- **Division:** `/` (e.g., `5 / 2` results in `2.5`)
- **Floor Division:** `//` (e.g., `5 // 2` results in `2`)
- **Modulus:** `%` (e.g., `5 % 2` results in `1`)
- **Exponentiation:** `**` (e.g., `5 ** 2` results in `25`)
- **Square Root:** Use the `math.sqrt()` function (e.g., `math.sqrt(25)` results in `5.0`)

### Functions:
- **`abs(x)`:** Returns the absolute value of `x`.
- **`pow(x, y)`:** Returns `x` raised to the power of `y`.
- **`round(x, n)`:** Rounds `x` to `n` decimal places.

Python also provides the `math` module for more advanced mathematical functions, like `math.sin()`, `math.log()`, and `math.factorial()`.



======================================================================================

"""

