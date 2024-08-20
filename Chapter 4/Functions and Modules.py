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
"""
print('Success')