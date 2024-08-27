"""
TODO:Understading exceptions and errors?

### **Understanding Exceptions and Errors (Short Overview)**

- **Errors**:
  - **Syntax Errors**: Occur when Python cannot interpret your code due to incorrect syntax (e.g., missing colons, parentheses).
  - **Example**: `if True print("Hello")` raises a `SyntaxError` because of the missing colon.

- **Exceptions**:
  - **Runtime Errors**: Occur during program execution, even if the syntax is correct.
  - **Common Exceptions**:
    - **`ZeroDivisionError`**: Division by zero.
    - **`TypeError`**: Incompatible operation types.
    - **`ValueError`**: Function receives an argument of the correct type but inappropriate value.
  
- **Handling Exceptions**:
  - Use `try-except` blocks to catch and handle exceptions gracefully.
  - **Example**:
    ```python
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    ```

- **Raising Exceptions**:
  - Use `raise` to trigger an exception manually.
  - **Example**:
    ```python
    raise ValueError("Invalid input!")
    ```

Understanding exceptions helps prevent your program from crashing and allows you to handle unexpected situations effectively.

======================================================================================

TODO:Handling exceptions with try-excepts blockes?

### **Handling Exceptions with `try-except` Blocks (Short Overview)**

- **Purpose**: `try-except` blocks allow you to handle errors gracefully without crashing your program.

- **Basic Structure**:
  ```python
  try:
      # Code that might raise an exception
  except ExceptionType:
      # Code to handle the exception
  ```

- **Example**:
  ```python
  try:
      result = 10 / 0
  except ZeroDivisionError:
      print("Cannot divide by zero!")
  ```

- **Multiple Exceptions**:
  - Handle different exceptions separately.
  - Example:
    ```python
    try:
        value = int("abc")
    except ValueError:
        print("Invalid number!")
    except TypeError:
        print("Wrong type!")
    ```

- **Generic Exception Handling**:
  - Use `except` without specifying an exception type to catch any exception.
  - Example:
    ```python
    try:
        result = 10 / 0
    except:
        print("An error occurred!")
    ```

- **Else and Finally**:
  - **`else`**: Runs if no exception occurs.
  - **`finally`**: Always runs, regardless of whether an exception was raised or not.
  - Example:
    ```python
    try:
        result = 10 / 2
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    else:
        print("Division successful!")
    finally:
        print("Execution complete.")
    ```

Use `try-except` blocks to manage errors and maintain program stability.

======================================================================================

TODO:Raising exceptions with rise statements?

### **Raising Exceptions with `raise` Statements (Short Overview)**

- **Purpose**: The `raise` statement is used to trigger an exception intentionally in your code.

- **Basic Syntax**:
  ```python
  raise ExceptionType("Error message")
  ```

- **Example**:
  ```python
  def check_age(age):
      if age < 0:
          raise ValueError("Age cannot be negative!")
      return age

  try:
      check_age(-5)
  except ValueError as e:
      print(e)  # Output: Age cannot be negative!
  ```

- **Custom Exceptions**:
  - You can define your own exception classes by inheriting from `Exception`.
  - Example:
    ```python
    class CustomError(Exception):
        pass

    raise CustomError("This is a custom error!")
    ```

Use the `raise` statement to enforce constraints or signal errors in your code intentionally.

======================================================================================

TODO:Exception chaining and traceback?

### **Exception Chaining and Traceback (Short Overview)**

- **Exception Chaining (`raise ... from`)**:
  - **Purpose**: Links a new exception to an original exception, providing context for the error.
  - **Syntax**:
    ```python
    raise NewException("Message") from OriginalException
    ```
  - **Example**:
    ```python
    try:
        x = int("abc")
    except ValueError as e:
        raise TypeError("Type conversion failed") from e
    ```
  - **Explanation**: The above code raises a `TypeError`, showing that it was caused by a `ValueError`. This helps in understanding the root cause of the problem.

- **Traceback**:
  - **Purpose**: Provides a detailed report of where the error occurred, showing the sequence of function calls leading up to the exception.
  - **Automatic Display**: When an unhandled exception occurs, Python automatically prints the traceback.
  - **Example**:
    ```python
    try:
        1 / 0
    except ZeroDivisionError as e:
        import traceback
        traceback.print_exc()
    ```
  - **Explanation**: The above code prints the full traceback of the exception, showing the exact location and cause of the error.

- **Traceback Example Output**:
  ```
  Traceback (most recent call last):
    File "example.py", line 2, in <module>
      1 / 0
  ZeroDivisionError: division by zero
  ```

Understanding exception chaining and traceback helps in debugging and provides clarity on how errors propagate in your code.

======================================================================================

TODO:Logging and error reporting?

### **Logging and Error Reporting (Short Overview)**

- **Logging**:
  - **Purpose**: Records events, errors, and other information to help diagnose issues in a program.
  - **Using the `logging` Module**:
    - **Basic Setup**:
      ```python
      import logging
      logging.basicConfig(level=logging.INFO)
      ```
    - **Logging Levels**:
      - **`DEBUG`**: Detailed information, typically of interest only when diagnosing problems.
      - **`INFO`**: Confirmation that things are working as expected.
      - **`WARNING`**: An indication that something unexpected happened or indicative of some problem.
      - **`ERROR`**: A more serious problem, due to which the software has not been able to perform some function.
      - **`CRITICAL`**: A very serious error, indicating the program itself may be unable to continue running.
    - **Example**:
      ```python
      logging.info("Program started")
      try:
          1 / 0
      except ZeroDivisionError:
          logging.error("Division by zero occurred", exc_info=True)
      ```

- **Error Reporting**:
  - **Purpose**: Alerts developers or users about errors that have occurred in the program.
  - **Integrating with Logging**:
    - **`exc_info=True`**: Logs the traceback along with the error message.
    - **Example**:
      ```python
      try:
          value = int("abc")
      except ValueError as e:
          logging.error("Error converting value", exc_info=True)
      ```

- **Log Files**:
  - Redirect logs to a file instead of the console.
  - **Example**:
    ```python
    logging.basicConfig(filename='app.log', level=logging.ERROR)
    logging.error("An error occurred")
    ```
  - This saves all `ERROR` level and above logs to `app.log`.

- **Advanced Reporting**:
  - **External Tools**: Integrate with error reporting services (e.g., Sentry) to monitor and manage errors in real-time.
  - **Alerts**: Automatically notify the development team when critical errors occur.

Logging and error reporting are essential for monitoring the health of your application and diagnosing issues efficiently.

======================================================================================

TODO:Debugging and techiques and tools?

### **Debugging Techniques and Tools (Short Overview)**

- **Debugging Techniques**:
  - **Print Statements**:
    - **Purpose**: Quick and simple way to check variable values or program flow.
    - **Example**:
      ```python
      x = 5
      print(f"x value is: {x}")
      ```
    - **Limitation**: Not suitable for complex debugging or large codebases.
  
  - **Using a Debugger**:
    - **Purpose**: Allows you to pause execution, inspect variables, and step through code.
    - **Common Debugging Steps**:
      1. **Set Breakpoints**: Points in the code where execution will pause.
      2. **Step Over**: Move to the next line of code.
      3. **Step Into**: Dive into function calls to inspect them line by line.
      4. **Inspect Variables**: Check the current state of variables.
      5. **Continue Execution**: Run the code until the next breakpoint.

  - **Tracing**:
    - **Purpose**: Follow the flow of execution to identify where the problem occurs.
    - **Example**: Using `sys.settrace()` or `trace` module for detailed function calls and execution flow.
  
  - **Rubber Duck Debugging**:
    - **Purpose**: Explain your code or problem out loud (or to an inanimate object) to gain clarity and find errors yourself.

- **Debugging Tools**:
  - **Built-in Python Debugger (`pdb`)**:
    - **Usage**: 
      ```python
      import pdb
      pdb.set_trace()
      ```
    - **Features**:
      - Set breakpoints, inspect variables, and step through code interactively.
  
  - **Integrated Development Environment (IDE) Debuggers**:
    - **Popular Options**: 
      - **PyCharm**: Provides advanced debugging features, including variable inspection, breakpoints, and step execution.
      - **VS Code**: Comes with a powerful debugger for Python, with support for breakpoints, variable inspection, and more.
  
  - **Logging**:
    - **Purpose**: Persistent record of program behavior, useful for post-mortem analysis.
    - **Tool**: Use Python’s `logging` module to capture logs at various levels (DEBUG, INFO, WARNING, ERROR, CRITICAL).

  - **Third-Party Tools**:
    - **Sentry**: For real-time error tracking and debugging.
    - **PySnooper**: For simple tracing of code execution and variables.

Debugging is essential for identifying and fixing errors in your code. Using a combination of techniques like print statements, debugging tools, and log analysis will help you efficiently diagnose and solve issues.

======================================================================================

"""