"""
TODO:Decorators and metaprogramming?

### **Decorators and Metaprogramming (Short Overview)**

#### **Decorators**
- **Purpose**: Modify or enhance the behavior of functions or methods without changing their code.
- **Basic Syntax**:
  ```python
  def decorator(func):
      def wrapper(*args, **kwargs):
          # Code to execute before the function
          result = func(*args, **kwargs)
          # Code to execute after the function
          return result
      return wrapper

  @decorator
  def my_function():
      print("Hello, World!")
  ```
- **Usage**:
  - **Function Decorators**: Enhance functions (e.g., logging, access control).
  - **Class Decorators**: Modify or extend class behavior.
  - **Chaining Decorators**: Multiple decorators can be stacked on a single function.

- **Common Built-In Decorators**:
  - **`@staticmethod`**: Defines a method that doesn’t operate on an instance or class.
  - **`@classmethod`**: Defines a method that operates on the class rather than an instance.
  - **`@property`**: Converts a method into a read-only property.

#### **Metaprogramming**
- **Purpose**: Writing code that manipulates other code (e.g., functions, classes) dynamically.
- **Key Concepts**:
  - **Introspection**: Examine the type or properties of objects at runtime.
  - **Example**:
    ```python
    print(type(10))  # <class 'int'>
    print(dir(str))  # List all attributes and methods of 'str'
    ```

- **Dynamic Class Creation (`type`)**:
  - **Purpose**: Create classes dynamically at runtime.
  - **Syntax**:
    ```python
    MyClass = type('MyClass', (BaseClass,), {'attribute': value})
    ```
  - **Example**:
    ```python
    MyClass = type('MyClass', (object,), {'greet': lambda self: "Hello"})
    obj = MyClass()
    print(obj.greet())  # Output: Hello
    ```

- **Metaclasses**:
  - **Purpose**: A class of a class; defines how classes behave.
  - **Syntax**:
    ```python
    class Meta(type):
        def __new__(cls, name, bases, dct):
            # Modify the class here
            return super().__new__(cls, name, bases, dct)

    class MyClass(metaclass=Meta):
        pass
    ```
  - **Use Cases**: Enforcing coding standards, adding methods/attributes automatically.

**Summary**:
- **Decorators** are for modifying functions/methods easily.
- **Metaprogramming** involves writing code that writes or manipulates other code, allowing for more dynamic and flexible designs.

======================================================================================

TODO:Context managers and the "with" statement?

### **Context Managers and the `with` Statement (Short Overview)**

#### **Context Managers**
- **Purpose**: Manage resources efficiently by setting up and tearing down resources automatically.
- **Common Use Cases**:
  - **File Handling**: Automatically closing files after reading/writing.
  - **Database Connections**: Ensuring connections are closed after use.
  - **Locking Mechanisms**: Managing locks in multithreaded environments.

#### **The `with` Statement**
- **Purpose**: Simplifies the use of context managers by handling resource setup and cleanup automatically.
- **Basic Syntax**:
  ```python
  with context_manager as resource:
      # Use the resource
  ```
  - **Example (File Handling)**:
    ```python
    with open('file.txt', 'r') as file:
        data = file.read()
    # File is automatically closed after the block
    ```

#### **Creating Custom Context Managers**
- **Using a Class**:
  - Implement `__enter__()` and `__exit__()` methods in a class.
  - **Example**:
    ```python
    class MyContext:
        def __enter__(self):
            print("Entering")
            return self
        
        def __exit__(self, exc_type, exc_value, traceback):
            print("Exiting")
    
    with MyContext() as ctx:
        print("Inside the block")
    ```
  - **Output**:
    ```
    Entering
    Inside the block
    Exiting
    ```

- **Using the `contextlib` Module**:
  - **`contextlib.contextmanager`**: A decorator that turns a generator function into a context manager.
  - **Example**:
    ```python
    from contextlib import contextmanager

    @contextmanager
    def my_context():
        print("Entering")
        yield
        print("Exiting")
    
    with my_context():
        print("Inside the block")
    ```
  - **Output**:
    ```
    Entering
    Inside the block
    Exiting
    ```

**Summary**:
- **Context Managers** ensure proper resource management.
- **The `with` Statement** simplifies working with context managers, ensuring setup and cleanup are automatically handled.
- **Custom Context Managers** can be created using classes or the `contextlib` module.

======================================================================================

TODO:Generators and iterators?

### **Generators and Iterators (Short Overview)**

#### **Iterators**
- **Purpose**: Objects that represent a stream of data, allowing you to traverse through it one element at a time.
- **Key Methods**:
  - **`__iter__()`**: Returns the iterator object itself.
  - **`__next__()`**: Returns the next item in the sequence and raises `StopIteration` when there are no more items.
- **Example**:
  ```python
  my_list = [1, 2, 3]
  iterator = iter(my_list)
  
  print(next(iterator))  # Output: 1
  print(next(iterator))  # Output: 2
  print(next(iterator))  # Output: 3
  ```

#### **Generators**
- **Purpose**: Simplified way to create iterators using functions and the `yield` statement.
- **Key Characteristics**:
  - Use **`yield`** to produce a series of values lazily (one at a time) instead of returning them all at once.
  - Automatically create an iterator when called.
- **Example**:
  ```python
  def count_up_to(max):
      count = 1
      while count <= max:
          yield count
          count += 1

  generator = count_up_to(3)

  print(next(generator))  # Output: 1
  print(next(generator))  # Output: 2
  print(next(generator))  # Output: 3
  ```

- **Advantages**:
  - **Memory Efficiency**: Only one item is generated at a time, making them ideal for large data sets or streams.
  - **Simpler Code**: Generators are easier to implement than custom iterator classes.

- **Generator Expressions**:
  - Similar to list comprehensions but generate items lazily.
  - **Example**:
    ```python
    squares = (x * x for x in range(5))
    for square in squares:
        print(square)  # Outputs: 0, 1, 4, 9, 16
    ```

**Summary**:
- **Iterators** are objects you can traverse through with `__iter__()` and `__next__()`.
- **Generators** simplify the creation of iterators using functions and `yield`, providing a more efficient way to handle sequences of data.

======================================================================================

TODO:Corontines and asynchronous programming?

### **Coroutines and Asynchronous Programming (Short Overview)**

#### **Coroutines**
- **Purpose**: Special functions that can pause and resume execution, allowing for cooperative multitasking.
- **Defining Coroutines**:
  - Use the `async def` keyword to define a coroutine.
  - **Example**:
    ```python
    async def my_coroutine():
        print("Coroutine started")
        await asyncio.sleep(1)
        print("Coroutine ended")
    ```

- **Key Concepts**:
  - **`await`**: Pauses the coroutine until the awaited task is completed, allowing other tasks to run in the meantime.
  - **Running Coroutines**: Coroutines need to be run within an event loop (e.g., using `asyncio.run()`).

#### **Asynchronous Programming**
- **Purpose**: Enables writing concurrent code using coroutines, allowing tasks to run independently without blocking each other.
- **Benefits**:
  - **Non-Blocking I/O**: Efficiently handles tasks like network requests or file I/O without blocking the main thread.
  - **Improved Performance**: Suitable for tasks that involve waiting (e.g., web scraping, API calls).

- **The `asyncio` Module**:
  - **Event Loop**: Core component that runs and manages coroutines.
  - **Example**:
    ```python
    import asyncio

    async def say_hello():
        print("Hello")
        await asyncio.sleep(1)
        print("World")

    asyncio.run(say_hello())  # Output: Hello (pause) World
    ```

- **Concurrent Tasks**:
  - **`asyncio.gather()`**: Run multiple coroutines concurrently.
  - **Example**:
    ```python
    async def task1():
        await asyncio.sleep(1)
        print("Task 1 done")

    async def task2():
        await asyncio.sleep(2)
        print("Task 2 done")

    asyncio.run(asyncio.gather(task1(), task2()))
    ```

- **Asynchronous I/O**:
  - **Purpose**: Handle I/O-bound tasks (like reading files, network requests) asynchronously.
  - **Example**:
    ```python
    async def fetch_data():
        await asyncio.sleep(2)
        return "Data fetched"

    async def main():
        data = await fetch_data()
        print(data)

    asyncio.run(main())
    ```

**Summary**:
- **Coroutines**: Functions that can pause (`await`) and resume, allowing for cooperative multitasking.
- **Asynchronous Programming**: Uses coroutines to run tasks concurrently without blocking, improving efficiency in I/O-bound and high-latency operations. The `asyncio` module provides tools to manage and run these tasks effectively.

======================================================================================

TODO:Muti-threading and concuurncy?

### **Multithreading and Concurrency (Short Overview)**

#### **Multithreading**
- **Purpose**: Allows multiple threads to run concurrently within a single process, enabling tasks to be executed simultaneously.
- **Key Concepts**:
  - **Thread**: A separate flow of execution. In Python, threads run in the same memory space.
  - **Global Interpreter Lock (GIL)**: A mechanism in CPython that allows only one thread to execute Python bytecode at a time, limiting true parallelism in CPU-bound tasks.
  
- **Common Use Cases**:
  - **I/O-bound tasks**: Such as reading/writing files, network operations, where the GIL is less of a concern.
  
- **Creating Threads**:
  - **Using the `threading` Module**:
    ```python
    import threading

    def print_numbers():
        for i in range(5):
            print(i)

    thread = threading.Thread(target=print_numbers)
    thread.start()
    thread.join()  # Waits for the thread to finish
    ```

#### **Concurrency**
- **Purpose**: Refers to the ability of a system to handle multiple tasks at the same time, which can be achieved via multithreading, multiprocessing, or asynchronous programming.
- **Concurrency vs. Parallelism**:
  - **Concurrency**: Multiple tasks make progress at overlapping times (not necessarily simultaneously).
  - **Parallelism**: Multiple tasks run exactly at the same time (requires multiple CPU cores).

- **Concurrency Techniques**:
  - **Multithreading**: For I/O-bound tasks.
  - **Multiprocessing**: For CPU-bound tasks, using multiple processes to bypass the GIL.
  - **Asynchronous Programming**: Uses coroutines and event loops for concurrent task management (ideal for I/O-bound tasks with long waits).

- **Thread Safety**:
  - **Locks**: Prevents multiple threads from modifying shared data simultaneously.
    ```python
    lock = threading.Lock()
    lock.acquire()
    # Critical section
    lock.release()
    ```
  - **`ThreadPoolExecutor`**: Manages a pool of threads to execute tasks concurrently.
    ```python
    from concurrent.futures import ThreadPoolExecutor

    def task(n):
        return n * 2

    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(task, [1, 2, 3, 4, 5])
    ```

**Summary**:
- **Multithreading**: Enables concurrent execution of threads in a single process, ideal for I/O-bound tasks. Python's GIL limits parallelism in CPU-bound tasks.
- **Concurrency**: The broader concept of managing multiple tasks at once, which can be achieved using multithreading, multiprocessing, or asynchronous programming, depending on the task requirements.

======================================================================================

TODO:Working with dates and times (datetime module)?

### **Working with Dates and Times (`datetime` Module) (Short Overview)**

#### **`datetime` Module Overview**
- **Purpose**: Provides classes for manipulating dates and times in both simple and complex ways.
- **Common Classes**:
  - **`datetime.date`**: Represents a date (year, month, day).
  - **`datetime.time`**: Represents a time (hour, minute, second, microsecond).
  - **`datetime.datetime`**: Combines both date and time.
  - **`datetime.timedelta`**: Represents a duration, the difference between two dates or times.

#### **Creating Date and Time Objects**
- **Date Object**:
  ```python
  from datetime import date
  today = date.today()  # Get current date
  custom_date = date(2023, 8, 27)  # Create a specific date
  print(today)  # Output: 2024-08-27
  ```
- **Time Object**:
  ```python
  from datetime import time
  custom_time = time(14, 30, 45)  # Create a specific time
  print(custom_time)  # Output: 14:30:45
  ```
- **Datetime Object**:
  ```python
  from datetime import datetime
  now = datetime.now()  # Get current date and time
  custom_datetime = datetime(2023, 8, 27, 14, 30, 45)  # Specific date and time
  print(now)  # Output: 2024-08-27 14:30:45.123456
  ```

#### **Formatting and Parsing Dates/Times**
- **Formatting**: Convert datetime objects to strings.
  - **`strftime()`**: Format datetime objects into readable strings.
  ```python
  formatted = now.strftime("%Y-%m-%d %H:%M:%S")
  print(formatted)  # Output: 2024-08-27 14:30:45
  ```
- **Parsing**: Convert strings to datetime objects.
  - **`strptime()`**: Parse strings into datetime objects.
  ```python
  parsed_date = datetime.strptime("2024-08-27", "%Y-%m-%d")
  print(parsed_date)  # Output: 2024-08-27 00:00:00
  ```

#### **Manipulating Dates and Times**
- **Arithmetic with `timedelta`**:
  - **Adding/Subtracting Days**:
    ```python
    from datetime import timedelta
    tomorrow = today + timedelta(days=1)
    print(tomorrow)  # Output: 2024-08-28
    ```
  - **Calculating Differences**:
    ```python
    difference = tomorrow - today
    print(difference)  # Output: 1 day, 0:00:00
    ```

#### **Handling Time Zones**
- **`pytz` Module**: Used with `datetime` for time zone support.
  - **Example**:
    ```python
    import pytz
    utc = pytz.utc
    local_tz = pytz.timezone('US/Eastern')
    utc_now = datetime.now(utc)
    local_time = utc_now.astimezone(local_tz)
    print(local_time)
    ```

**Summary**:
- The `datetime` module is essential for managing dates and times, offering tools to create, format, manipulate, and compare date and time objects. For handling time zones, use `pytz` alongside `datetime`.

======================================================================================

TODO:Working with regular expressions (re module)?

### **Working with Regular Expressions (`re` Module) (Short Overview)**

#### **Basic Concepts**
- **Purpose**: Match, search, and manipulate strings based on patterns.
- **Regular Expressions (Regex)**: Patterns used to match sequences of characters in text.

#### **Common Functions in `re` Module**
- **`re.match()`**: Checks for a match only at the beginning of the string.
  - **Example**:
    ```python
    import re
    result = re.match(r'\d+', '123abc')
    print(result.group())  # Output: 123
    ```

- **`re.search()`**: Searches the entire string for the first occurrence of the pattern.
  - **Example**:
    ```python
    result = re.search(r'\d+', 'abc123def')
    print(result.group())  # Output: 123
    ```

- **`re.findall()`**: Returns a list of all non-overlapping matches of the pattern.
  - **Example**:
    ```python
    result = re.findall(r'\d+', 'abc123def456')
    print(result)  # Output: ['123', '456']
    ```

- **`re.finditer()`**: Returns an iterator yielding match objects for all non-overlapping matches.
  - **Example**:
    ```python
    result = re.finditer(r'\d+', 'abc123def456')
    for match in result:
        print(match.group())  # Output: 123, 456
    ```

- **`re.sub()`**: Replaces occurrences of the pattern with a specified replacement string.
  - **Example**:
    ```python
    result = re.sub(r'\d+', 'number', 'abc123def456')
    print(result)  # Output: abcnumberdefnumber
    ```

#### **Pattern Syntax**
- **Basic Patterns**:
  - **`\d`**: Matches any digit.
  - **`\w`**: Matches any word character (alphanumeric + underscore).
  - **`\s`**: Matches any whitespace character.
  - **`.`**: Matches any character except newline.

- **Quantifiers**:
  - **`*`**: Matches 0 or more occurrences.
  - **`+`**: Matches 1 or more occurrences.
  - **`?`**: Matches 0 or 1 occurrence.
  - **`{n}`**: Matches exactly `n` occurrences.
  - **`{n,}`**: Matches `n` or more occurrences.
  - **`{n,m}`**: Matches between `n` and `m` occurrences.

- **Anchors**:
  - **`^`**: Matches the start of the string.
  - **`$`**: Matches the end of the string.

- **Character Classes**:
  - **`[abc]`**: Matches any character `a`, `b`, or `c`.
  - **`[^abc]`**: Matches any character except `a`, `b`, or `c`.

- **Groups and Capturing**:
  - **`()`**: Creates a capturing group.
  - **Example**:
    ```python
    result = re.search(r'(\d+)', 'abc123')
    print(result.group(1))  # Output: 123
    ```

#### **Modifiers**
- **`re.IGNORECASE`**: Case-insensitive matching.
  - **Example**:
    ```python
    result = re.search(r'abc', 'ABC', re.IGNORECASE)
    print(result.group())  # Output: ABC
    ```

- **`re.MULTILINE`**: `^` and `$` match the start and end of each line.
- **`re.DOTALL`**: `.` matches newline characters as well.

**Summary**:
- The `re` module provides powerful tools for string pattern matching and manipulation using regular expressions. Key functions include `match()`, `search()`, `findall()`, `finditer()`, and `sub()`. Regular expressions use patterns and special characters to specify the strings you want to match or replace.

======================================================================================

"""