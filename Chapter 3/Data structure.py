"""
TODO:Lists and list operations?

**Lists** are ordered, mutable collections in Python.

### **Key List Operations:**

- **Create a List:** `my_list = [1, 2, 3]`
- **Access Elements:** `my_list[0]` (first element)
- **Modify Elements:** `my_list[1] = "new_value"`
- **Append:** `my_list.append("item")`
- **Insert:** `my_list.insert(1, "item")`
- **Remove:** `my_list.remove("item")`
- **Pop:** `item = my_list.pop(2)` (removes and returns element at index 2)
- **Slice:** `sublist = my_list[1:3]`
- **Length:** `len(my_list)`
- **Concatenate:** `combined = my_list + another_list`
- **List Comprehension:** `[x**2 for x in range(5)]`

======================================================================================

TODO:Tuples and tuple operations?

**Tuples** are ordered, immutable collections in Python.

### **Key Tuple Operations:**

- **Create a Tuple:** `my_tuple = (1, 2, 3)` or `my_tuple = 1, 2, 3`
- **Access Elements:** `my_tuple[0]` (first element)
- **Immutable:** Elements cannot be changed after creation.

- **Length:** `len(my_tuple)`

- **Concatenate:** `combined = my_tuple + another_tuple`
- **Slicing:** `sub_tuple = my_tuple[1:3]`
- **Unpacking:** `a, b, c = my_tuple`
- **Single Element Tuple:** `(5,)` (note the comma)

Tuples are useful for storing fixed collections of items.

======================================================================================

TODO:Strings and string manipulation?

**Strings** in Python are immutable sequences of characters.

### **Key String Operations:**

- **Create a String:** `my_string = "Hello"`
- **Access Characters:** `my_string[0]` (first character)
- **Concatenation:** `combined = "Hello " + "World"`
- **Repetition:** `repeated = "Hello" * 3` (results in `"HelloHelloHello"`)
- **Slicing:** `sub_string = my_string[1:4]` (extracts `"ell"`)
- **Length:** `len(my_string)`
- **Find Substring:** `position = my_string.find("lo")` (returns the index)
- **Replace Substring:** `new_string = my_string.replace("Hello", "Hi")`
- **Convert Case:** `my_string.lower()`, `my_string.upper()`, `my_string.capitalize()`
- **Strip Whitespace:** `my_string.strip()` (removes leading/trailing whitespace)
- **Split into List:** `words = my_string.split(" ")`
- **Join List to String:** `joined = "-".join(["Hello", "World"])` (results in `"Hello-World"`)

Strings are powerful for text manipulation and formatting.

======================================================================================

TODO:Dictionaries and dictionary operations?

**Dictionaries** in Python are unordered collections of key-value pairs.

### **Key Dictionary Operations:**

- **Create a Dictionary:** `my_dict = {"key1": "value1", "key2": "value2"}`
- **Access Value:** `my_dict["key1"]` (returns `"value1"`)
- **Add/Update Item:** `my_dict["key3"] = "value3"`
- **Delete Item:** `del my_dict["key1"]`
- **Check Key Existence:** `"key1" in my_dict` (returns `True` or `False`)
- **Get Keys:** `keys = my_dict.keys()` (returns a view of keys)
- **Get Values:** `values = my_dict.values()` (returns a view of values)
- **Get Items:** `items = my_dict.items()` (returns a view of key-value pairs)
- **Iterate Over Dictionary:**
  ```python
  for key, value in my_dict.items():
      print(key, value)
  ```
- **Default Value Access:** `value = my_dict.get("key4", "default")` (returns `"default"` if `"key4"` doesn't exist)

Dictionaries are ideal for mapping relationships between keys and values.

======================================================================================

TODO:Sets and set operations?

**Sets** in Python are unordered collections of unique elements.

### **Key Set Operations:**

- **Create a Set:** `my_set = {1, 2, 3}` or `my_set = set([1, 2, 3])`
- **Add Element:** `my_set.add(4)`
- **Remove Element:** `my_set.remove(2)` (raises an error if not found) or `my_set.discard(2)` (no error if not found)
- **Check Membership:** `2 in my_set` (returns `True` or `False`)
- **Union:** `set1 | set2` or `set1.union(set2)` (combines elements)
- **Intersection:** `set1 & set2` or `set1.intersection(set2)` (common elements)
- **Difference:** `set1 - set2` or `set1.difference(set2)` (elements in `set1` but not `set2`)
- **Symmetric Difference:** `set1 ^ set2` or `set1.symmetric_difference(set2)` (elements in either set, but not both)
- **Clear Set:** `my_set.clear()` (removes all elements)

Sets are useful for operations involving unique items and for mathematical set operations.

======================================================================================

TODO:Working with collections (arrays, deque, namedtuples)?

Python provides several specialized collection types for different use cases:

### **Arrays** (`array` module):
- Used for storing elements of the same type efficiently.
- **Create an Array:**
  ```python
  import array
  arr = array.array('i', [1, 2, 3])  # 'i' denotes integers
  ```
- **Access/Modify Elements:** Same as lists (`arr[0]`, `arr[1] = 10`)
- **Append Element:** `arr.append(4)`
- **Remove Element:** `arr.remove(2)`

### **Deque** (`collections.deque`):
- A double-ended queue that supports fast appends and pops from both ends.
- **Create a Deque:**
  ```python
  from collections import deque
  d = deque([1, 2, 3])
  ```
- **Append to Right/Left:** `d.append(4)`, `d.appendleft(0)`
- **Pop from Right/Left:** `d.pop()`, `d.popleft()`
- **Rotate Elements:** `d.rotate(1)` (moves elements to the right by 1)

### **Namedtuples** (`collections.namedtuple`):
- Immutable and lightweight objects similar to tuples but with named fields.
- **Create a Namedtuple:**
  ```python
  from collections import namedtuple
  Point = namedtuple('Point', ['x', 'y'])
  p = Point(10, 20)
  ```
- **Access Elements by Name/Index:**
  ```python
  print(p.x, p[1])  # Output: 10 20
  ```

These collections are useful for various scenarios, from handling large homogeneous datasets to maintaining ordered data efficiently.

======================================================================================

TODO:List comprehensions and generator expressions?

**List comprehensions** and **generator expressions** are concise ways to create lists and iterators in Python.

### **List Comprehensions:**
- **Purpose:** Create a new list by applying an expression to each item in an iterable.
- **Syntax:**
  ```python
  [expression for item in iterable if condition]
  ```
- **Example:**
  ```python
  squares = [x**2 for x in range(5)]  # Output: [0, 1, 4, 9, 16]
  even_squares = [x**2 for x in range(5) if x % 2 == 0]  # Output: [0, 4, 16]
  ```

### **Generator Expressions:**
- **Purpose:** Create a generator (an iterator) that yields items one by one, which is more memory-efficient for large datasets.
- **Syntax:**
  ```python
  (expression for item in iterable if condition)
  ```
- **Example:**
  ```python
  squares_gen = (x**2 for x in range(5))
  for square in squares_gen:
      print(square)  # Outputs 0, 1, 4, 9, 16 one by one
  ```

### **Key Differences:**
- **List comprehensions** return a full list immediately, consuming more memory.
- **Generator expressions** return an iterator that computes each item on-the-fly, saving memory.

These constructs are great for creating new sequences from existing iterables with clear and concise syntax.

======================================================================================

"""