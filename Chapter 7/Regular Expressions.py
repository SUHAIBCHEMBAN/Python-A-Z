"""
TODO:Introduction to regular expressions?

### **Introduction to Regular Expressions**

**Regular expressions** (regex) are sequences of characters that define search patterns. They are used for searching, matching, and manipulating strings based on specific patterns. Regular expressions are widely used in text processing, data validation, and parsing tasks.

### **Key Concepts**

#### **1. Basic Syntax**

- **Literal Characters:** Match exact characters.
  - Example: `abc` matches "abc" in a string.

- **Special Characters:**
  - **`.`** (Dot): Matches any single character except newline.
    - Example: `a.c` matches "abc", "a-c", etc.
  - **`^`** (Caret): Matches the start of the string.
    - Example: `^abc` matches "abc" at the start of the string.
  - **`$`** (Dollar Sign): Matches the end of the string.
    - Example: `abc$` matches "abc" at the end of the string.

#### **2. Character Classes**

- **`[ ]`**: Defines a set of characters to match.
  - Example: `[abc]` matches "a", "b", or "c".
- **`[^ ]`**: Defines a set of characters to exclude.
  - Example: `[^abc]` matches any character except "a", "b", or "c".
- **`[a-z]`**: Matches any lowercase letter.
  - Example: `[a-z]` matches "a" to "z".

#### **3. Quantifiers**

- **`*`**: Matches zero or more occurrences of the preceding character.
  - Example: `a*` matches "", "a", "aa", etc.
- **`+`**: Matches one or more occurrences of the preceding character.
  - Example: `a+` matches "a", "aa", etc., but not "".
- **`?`**: Matches zero or one occurrence of the preceding character.
  - Example: `a?` matches "" or "a".
- **`{n}`**: Matches exactly n occurrences of the preceding character.
  - Example: `a{3}` matches "aaa".
- **`{n,}`**: Matches n or more occurrences.
  - Example: `a{2,}` matches "aa", "aaa", etc.
- **`{n,m}`**: Matches between n and m occurrences.
  - Example: `a{2,4}` matches "aa", "aaa", "aaaa".

#### **4. Special Sequences**

- **`\d`**: Matches any digit (equivalent to `[0-9]`).
- **`\D`**: Matches any non-digit.
- **`\w`**: Matches any alphanumeric character (equivalent to `[a-zA-Z0-9_]`).
- **`\W`**: Matches any non-alphanumeric character.
- **`\s`**: Matches any whitespace character (space, tab, newline).
- **`\S`**: Matches any non-whitespace character.

#### **5. Grouping and Alternation**

- **`( )`**: Groups patterns together.
  - Example: `(abc)+` matches "abc", "abcabc", etc.
- **`|`**: Acts as a logical OR between two patterns.
  - Example: `a|b` matches "a" or "b".

### **Using Regular Expressions in Python**

Python provides the `re` module to work with regular expressions.

#### **Basic Functions:**

- **`re.match(pattern, string)`**: Checks if the pattern matches at the start of the string.
  - Example:
    ```python
    import re
    result = re.match(r'\d+', '123abc')
    print(result.group())  # Output: 123
    ```

- **`re.search(pattern, string)`**: Searches for the pattern anywhere in the string.
  - Example:
    ```python
    result = re.search(r'\d+', 'abc123')
    print(result.group())  # Output: 123
    ```

- **`re.findall(pattern, string)`**: Returns all matches as a list.
  - Example:
    ```python
    results = re.findall(r'\d+', 'abc123def456')
    print(results)  # Output: ['123', '456']
    ```

- **`re.sub(pattern, repl, string)`**: Replaces occurrences of the pattern with `repl`.
  - Example:
    ```python
    result = re.sub(r'\d+', 'NUMBER', 'abc123def456')
    print(result)  # Output: abcNUMBERdefNUMBER
    ```

- **`re.split(pattern, string)`**: Splits the string by occurrences of the pattern.
  - Example:
    ```python
    result = re.split(r'\d+', 'abc123def456')
    print(result)  # Output: ['abc', 'def', '']
    ```

### **Summary**

- **Regular Expressions**: Patterns used for matching and manipulating strings.
- **Basic Syntax**: Literal characters, special characters, character classes.
- **Quantifiers**: Define the number of occurrences.
- **Special Sequences**: Shorthand for common character classes.
- **Grouping and Alternation**: Group patterns and choose between alternatives.
- **Python `re` Module**: Provides functions for pattern matching and manipulation.

Regular expressions are powerful tools for complex string operations and are essential for text processing tasks in programming.

======================================================================================

TODO:Pattern matching and searching?

### **Pattern Matching and Searching with Regular Expressions**

**Pattern matching and searching** involve finding specific sequences of characters within a string based on predefined patterns. In Python, this is commonly done using the `re` module, which provides functions to search, match, and manipulate strings using regular expressions.

### **Key Functions for Pattern Matching and Searching**

#### **1. `re.match()`**

- **Purpose:** Checks if the pattern matches at the beginning of the string.
- **Returns:** A match object if a match is found; otherwise, `None`.
- **Example:**
  ```python
  import re

  pattern = r'\d{3}'  # Pattern to match exactly 3 digits
  string = "123abc456"

  match = re.match(pattern, string)
  if match:
      print("Match found:", match.group())
  else:
      print("No match")
  ```
  - **Output:** `Match found: 123` (matches "123" at the start of the string).

#### **2. `re.search()`**

- **Purpose:** Searches the entire string for the first location where the pattern matches.
- **Returns:** A match object if a match is found; otherwise, `None`.
- **Example:**
  ```python
  string = "abc123def456"
  
  search = re.search(r'\d+', string)  # Pattern to match one or more digits
  if search:
      print("Search found:", search.group())
  else:
      print("No match")
  ```
  - **Output:** `Search found: 123` (finds "123" anywhere in the string).

#### **3. `re.findall()`**

- **Purpose:** Finds all non-overlapping matches of the pattern in the string.
- **Returns:** A list of all matches.
- **Example:**
  ```python
  string = "abc123def456ghi789"
  
  matches = re.findall(r'\d+', string)
  print("All matches:", matches)
  ```
  - **Output:** `All matches: ['123', '456', '789']` (finds all sequences of digits).

#### **4. `re.finditer()`**

- **Purpose:** Returns an iterator yielding match objects for all matches of the pattern in the string.
- **Returns:** An iterator of match objects.
- **Example:**
  ```python
  string = "abc123def456"
  
  iterator = re.finditer(r'\d+', string)
  for match in iterator:
      print("Match found:", match.group())
  ```
  - **Output:** 
    ```
    Match found: 123
    Match found: 456
    ```

### **Using Match Objects**

When a match is found using `re.match()`, `re.search()`, or `re.finditer()`, a **match object** is returned. This object provides useful methods to extract information about the match:

- **`group()`**: Returns the matched string.
- **`start()`**: Returns the starting position of the match.
- **`end()`**: Returns the ending position of the match.
- **`span()`**: Returns a tuple containing the start and end positions.

### **Examples of Pattern Matching**

#### **Example 1: Email Validation**

```python
pattern = r'^\w+@\w+\.\w+$'
email = "example@example.com"

match = re.match(pattern, email)
if match:
    print("Valid email:", match.group())
else:
    print("Invalid email")
```
- **Explanation:** The pattern checks if the string starts with one or more word characters, followed by an `@`, then one or more word characters, a `.` and one or more word characters, ensuring a simple email format.

#### **Example 2: Extracting Dates**

```python
pattern = r'\b\d{2}/\d{2}/\d{4}\b'
text = "Today's date is 27/08/2024. Tomorrow will be 28/08/2024."

dates = re.findall(pattern, text)
print("Dates found:", dates)
```
- **Explanation:** The pattern matches dates in the format `DD/MM/YYYY`, ensuring they are bounded by word boundaries (`\b`).

### **Summary**

- **`re.match()`**: Matches the pattern at the beginning of the string.
- **`re.search()`**: Finds the first occurrence of the pattern anywhere in the string.
- **`re.findall()`**: Returns all non-overlapping matches as a list.
- **`re.finditer()`**: Returns an iterator yielding match objects for all matches.

Regular expressions are powerful tools for pattern matching and searching, enabling complex text processing tasks in Python.

======================================================================================

TODO:Matching functions (match,search,findall)?

### **Matching Functions in Python's `re` Module**

Python's `re` module provides several functions to perform pattern matching on strings using regular expressions. The most commonly used functions are `match()`, `search()`, and `findall()`.

### **1. `re.match()`**

- **Purpose:** 
  - Checks for a match only at the beginning of the string.
  
- **Usage:**
  - `re.match(pattern, string)`
  
- **Returns:**
  - A match object if the pattern matches the start of the string; otherwise, `None`.
  
- **Example:**
  ```python
  import re

  pattern = r'\d+'  # Pattern to match one or more digits
  string = "123abc456"

  match = re.match(pattern, string)
  if match:
      print("Match found:", match.group())  # Output: Match found: 123
  else:
      print("No match")
  ```
  - **Explanation:** `re.match()` checks if the string starts with one or more digits.

### **2. `re.search()`**

- **Purpose:** 
  - Searches the entire string for the first occurrence of the pattern.
  
- **Usage:**
  - `re.search(pattern, string)`
  
- **Returns:**
  - A match object for the first match found; otherwise, `None`.
  
- **Example:**
  ```python
  string = "abc123def456"
  
  search = re.search(r'\d+', string)
  if search:
      print("Search found:", search.group())  # Output: Search found: 123
  else:
      print("No match")
  ```
  - **Explanation:** `re.search()` scans the entire string and returns the first sequence of digits.

### **3. `re.findall()`**

- **Purpose:** 
  - Finds all non-overlapping matches of the pattern in the string.
  
- **Usage:**
  - `re.findall(pattern, string)`
  
- **Returns:**
  - A list of all matches found.
  
- **Example:**
  ```python
  string = "abc123def456ghi789"
  
  matches = re.findall(r'\d+', string)
  print("All matches:", matches)  # Output: All matches: ['123', '456', '789']
  ```
  - **Explanation:** `re.findall()` finds every sequence of digits in the string and returns them as a list.

### **Summary**

- **`re.match()`**:
  - **Focus:** Beginning of the string.
  - **Use Case:** Verify if a string starts with a particular pattern.
  
- **`re.search()`**:
  - **Focus:** Anywhere in the string.
  - **Use Case:** Find the first occurrence of a pattern within a string.
  
- **`re.findall()`**:
  - **Focus:** Entire string.
  - **Use Case:** Retrieve all occurrences of a pattern within a string.

These functions provide flexible ways to perform pattern matching and text processing in Python.

======================================================================================

TODO:Modifiers and pattern syntax?

### **Modifiers and Pattern Syntax in Regular Expressions**

Regular expressions (regex) in Python allow for complex pattern matching, and modifiers (also known as flags) can change how these patterns are interpreted. Understanding both the pattern syntax and modifiers is essential for effective regex use.

### **Modifiers (Flags)**

Modifiers can be applied to a pattern to alter its behavior. They are typically passed as an additional argument to regex functions (like `re.match()`, `re.search()`, etc.) or included within the pattern using the `(?i)` syntax.

#### **Common Modifiers:**

1. **`re.IGNORECASE` (or `re.I`)**
   - **Purpose:** Makes the pattern case-insensitive.
   - **Example:**
     ```python
     import re
     pattern = r'abc'
     text = "ABCabc"
     matches = re.findall(pattern, text, re.I)
     print(matches)  # Output: ['ABC', 'abc']
     ```

2. **`re.MULTILINE` (or `re.M`)**
   - **Purpose:** Allows `^` and `$` to match the start and end of each line within a string, rather than just the start and end of the entire string.
   - **Example:**
     ```python
     text = First line
     Second line
     Third line
     matches = re.findall(r'^Second', text, re.M)
     print(matches)  # Output: ['Second']
     ```

3. **`re.DOTALL` (or `re.S`)**
   - **Purpose:** Allows the dot `.` to match newline characters, so it can match any character in the string.
   - **Example:**
     ```python
     text = "First line\nSecond line"
     match = re.search(r'First.*Second', text, re.S)
     print(match.group())  # Output: First line\nSecond line
     ```

4. **`re.VERBOSE` (or `re.X`)**
   - **Purpose:** Allows you to write more readable regex patterns by ignoring whitespace and comments within the pattern.
   - **Example:**
     ```python
     pattern = r'''
     \d+    # Match one or more digits
     \s     # Match a whitespace character
     \w+    # Match one or more word characters
     '''
     text = "123 abc"
     match = re.search(pattern, text, re.X)
     print(match.group())  # Output: 123 abc
     ```

5. **`re.ASCII` (or `re.A`)**
   - **Purpose:** Makes `\w`, `\b`, `\d`, `\s`, and other character classes match only ASCII characters, rather than the full Unicode range.
   - **Example:**
     ```python
     pattern = r'\w+'
     text = "Café"
     match = re.search(pattern, text, re.A)
     print(match.group())  # Output: Caf (doesn't match 'é' as it's non-ASCII)
     ```

### **Pattern Syntax**

The syntax of regular expressions is a combination of literals, special characters, and metacharacters that define the pattern to be matched.

#### **Basic Components:**

1. **Literal Characters**
   - Match themselves exactly.
   - Example: `a`, `1`, `@` match the characters "a", "1", and "@".

2. **Metacharacters**
   - Have special meanings.
   - Common ones include: `. ^ $ * + ? { } [ ] \ | ( )`

3. **Character Classes**
   - **`[abc]`**: Matches any one of the characters `a`, `b`, or `c`.
   - **`[^abc]`**: Matches any character except `a`, `b`, or `c`.
   - **`[a-z]`**: Matches any lowercase letter from `a` to `z`.
   - **`\d`**: Matches any digit (`[0-9]`).
   - **`\w`**: Matches any word character (letters, digits, underscore).
   - **`\s`**: Matches any whitespace character (spaces, tabs, newlines).

4. **Anchors**
   - **`^`**: Matches the start of a string.
   - **`$`**: Matches the end of a string.

5. **Quantifiers**
   - **`*`**: Matches 0 or more occurrences of the preceding element.
   - **`+`**: Matches 1 or more occurrences of the preceding element.
   - **`?`**: Matches 0 or 1 occurrence of the preceding element.
   - **`{n}`**: Matches exactly `n` occurrences.
   - **`{n,}`**: Matches `n` or more occurrences.
   - **`{n,m}`**: Matches between `n` and `m` occurrences.

6. **Grouping and Capturing**
   - **`(abc)`**: Groups together `abc` as a single unit and captures it.
   - **`(?:abc)`**: Groups together `abc` but does not capture it.

7. **Alternation**
   - **`a|b`**: Matches either `a` or `b`.

8. **Special Sequences**
   - **`\b`**: Matches a word boundary.
   - **`\B`**: Matches a non-word boundary.
   - **`\A`**: Matches the start of the string.
   - **`\Z`**: Matches the end of the string.

### **Example: Combining Modifiers and Syntax**

```python
import re

pattern = r'(?i)hello\s+\w+'
text = "Hello World"

match = re.search(pattern, text)
if match:
    print("Match found:", match.group())  # Output: Match found: Hello World
```
- **Explanation:** 
  - `(?i)`: Makes the pattern case-insensitive.
  - `hello\s+\w+`: Matches "hello", followed by one or more spaces, followed by one or more word characters.

### **Summary**

- **Modifiers (Flags)**: Change how the regex engine interprets patterns, such as making them case-insensitive or allowing them to match across multiple lines.
- **Pattern Syntax**: A combination of literals, metacharacters, character classes, quantifiers, and anchors that define the pattern to match.

Understanding modifiers and pattern syntax allows you to craft powerful and flexible regex patterns for text processing tasks.

======================================================================================

TODO:Grouping and capturing?

### **Grouping and Capturing (Short Overview)**

- **Grouping (`(...)`)**:
  - Groups parts of a pattern to apply quantifiers or perform alternation.
  - Example: `(abc)+` matches "abc" repeated one or more times.

- **Capturing (`(...)`)**:
  - Stores the matched content within the group for later use.
  - Example: `(\d+)-(\d+)` applied to "123-456" captures "123" and "456".

- **Non-Capturing Grouping (`(?:...)`)**:
  - Groups without capturing.
  - Example: `(?:abc)+` matches "abc" repeated but doesn't store it.

Use grouping for pattern structure and capturing for extracting specific parts of the match.

======================================================================================

TODO:Search and replace operations?

### **Search and Replace Operations (Short Overview)**

- **`re.sub()`**: 
  - **Purpose:** Replaces occurrences of a pattern with a specified replacement string.
  - **Syntax:** `re.sub(pattern, replacement, string)`
  - **Example:** 
    ```python
    import re
    result = re.sub(r'\d+', 'NUMBER', 'Item 123 cost 456 dollars')
    print(result)  # Output: 'Item NUMBER cost NUMBER dollars'
    ```

- **`re.subn()`**:
  - **Purpose:** Same as `re.sub()` but also returns the number of replacements made.
  - **Syntax:** `re.subn(pattern, replacement, string)`
  - **Example:**
    ```python
    result, count = re.subn(r'\d+', 'NUMBER', '123 and 456')
    print(result, count)  # Output: 'NUMBER and NUMBER', 2
    ``` 

Use `re.sub()` for simple replacements and `re.subn()` when you need to know how many substitutions were made.

======================================================================================

TODO:Regular expressions in Python modules?

### **Regular Expressions in Python Modules (Short Overview)**

- **`re` Module**:
  - The primary module for working with regular expressions in Python.
  - **Key Functions**:
    - **`re.match()`**: Checks for a match only at the start of the string.
    - **`re.search()`**: Searches the entire string for the first match.
    - **`re.findall()`**: Returns all matches in the string as a list.
    - **`re.sub()`**: Replaces occurrences of a pattern with a specified string.
    - **`re.split()`**: Splits a string by the occurrences of a pattern.

**Example Usage:**
```python
import re

pattern = r'\d+'
string = "There are 123 apples and 456 oranges."

# Find all numbers in the string
numbers = re.findall(pattern, string)
print(numbers)  # Output: ['123', '456']
```

Use the `re` module to handle all regex-related operations in Python.


======================================================================================
"""