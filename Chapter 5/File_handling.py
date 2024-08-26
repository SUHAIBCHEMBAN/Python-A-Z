"""

TODO:Reading and writing text files?

### **Reading and Writing Text Files:**

**1. **Reading Text Files:**

- **Open a File:**
  ```python
  with open('filename.txt', 'r') as file:
      content = file.read()
  ```

- **Read Line by Line:**
  ```python
  with open('filename.txt', 'r') as file:
      lines = file.readlines()
  ```

- **Read First Line:**
  ```python
  with open('filename.txt', 'r') as file:
      first_line = file.readline()
  ```

**2. **Writing Text Files:**

- **Write to a File:**
  ```python
  with open('filename.txt', 'w') as file:
      file.write('Hello, world!')
  ```

- **Append to a File:**
  ```python
  with open('filename.txt', 'a') as file:
      file.write('\nAppended text.')
  ```

**3. **File Modes:**
- `'r'`: Read (default).
- `'w'`: Write (creates a new file or overwrites).
- `'a'`: Append (adds to an existing file).
- `'b'`: Binary mode (e.g., `'rb'`, `'wb'` for binary files).

### **Examples:**

- **Read Entire File:**
  ```python
  with open('example.txt', 'r') as file:
      content = file.read()
      print(content)
  ```

- **Write to File:**
  ```python
  with open('example.txt', 'w') as file:
      file.write('This is a new line of text.')
  ```

- **Append to File:**
  ```python
  with open('example.txt', 'a') as file:
      file.write('\nThis is an appended line.')
  ```

Using the `with` statement ensures that the file is properly closed after its block is executed, making file operations safer and more efficient.

======================================================================================

TODO:File modes and file objects?

### **File Modes:**

When opening a file in Python, you specify the mode to determine how you will interact with the file. Here are the common file modes:

- **`'r'` (Read):** Opens the file for reading (default). The file must exist.
  ```python
  with open('file.txt', 'r') as file:
      content = file.read()
  ```

- **`'w'` (Write):** Opens the file for writing. Creates a new file or truncates an existing file.
  ```python
  with open('file.txt', 'w') as file:
      file.write('Hello, World!')
  ```

- **`'a'` (Append):** Opens the file for appending. Creates a new file if it does not exist.
  ```python
  with open('file.txt', 'a') as file:
      file.write('Appending text.')
  ```

- **`'b'` (Binary):** Opens the file in binary mode. Can be combined with other modes (e.g., `'rb'`, `'wb'`).
  ```python
  with open('file.bin', 'rb') as file:
      content = file.read()
  ```

- **`'x'` (Exclusive Creation):** Creates a new file, but fails if the file already exists.
  ```python
  with open('file.txt', 'x') as file:
      file.write('Exclusive creation.')
  ```

### **File Objects:**

File objects represent an open file and provide methods to interact with it.

- **`file.read(size=-1)`**: Reads the entire file or a specified number of bytes.
  ```python
  content = file.read()
  ```

- **`file.readline(size=-1)`**: Reads a single line or up to a specified number of bytes.
  ```python
  line = file.readline()
  ```

- **`file.readlines(hint=-1)`**: Reads all lines or a specified number of lines.
  ```python
  lines = file.readlines()
  ```

- **`file.write(string)`**: Writes a string to the file.
  ```python
  file.write('Some text')
  ```

- **`file.writelines(lines)`**: Writes a list of strings to the file.
  ```python
  file.writelines(['Line 1', 'Line 2'])
  ```

- **`file.flush()`**: Flushes the internal buffer to the file.
  ```python
  file.flush()
  ```

- **`file.seek(offset, whence)`**: Moves the file pointer to a specified position.
  ```python
  file.seek(0)  # Move to the beginning of the file
  ```

- **`file.tell()`**: Returns the current file pointer position.
  ```python
  position = file.tell()
  ```

- **`file.close()`**: Closes the file.
  ```python
  file.close()
  ```

**Example Usage:**
```python
# Open a file and read its content
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Open a file and write to it
with open('example.txt', 'w') as file:
    file.write('Hello, World!')

# Append to a file
with open('example.txt', 'a') as file:
    file.write('\nAppended text.')

# Open a file in binary mode
with open('example.bin', 'rb') as file:
    binary_content = file.read()
    print(binary_content)
```

### **Summary:**
- **File Modes:** Determine how a file is opened (`'r'`, `'w'`, `'a'`, `'b'`, `'x'`).
- **File Objects:** Provide methods to read, write, and manipulate the file. Use the `with` statement for automatic file handling.

======================================================================================

TODO:File system operations (moving,renaming,deleting files)?

### **File System Operations:**

Python's `os` and `shutil` modules provide functions for performing file system operations such as moving, renaming, and deleting files.

### **1. Moving Files:**

**Using `shutil.move`:**
- Moves a file or directory to a new location.

**Example:**
```python
import shutil

# Move file from 'source.txt' to 'destination.txt'
shutil.move('source.txt', 'destination.txt')
```

**Note:** If `destination.txt` exists, it will be overwritten.

### **2. Renaming Files:**

**Using `os.rename`:**
- Renames a file or directory.

**Example:**
```python
import os

# Rename file from 'old_name.txt' to 'new_name.txt'
os.rename('old_name.txt', 'new_name.txt')
```

**Note:** This operation will fail if `new_name.txt` already exists.

### **3. Deleting Files:**

**Using `os.remove`:**
- Deletes a single file.

**Example:**
```python
import os

# Delete 'file_to_delete.txt'
os.remove('file_to_delete.txt')
```

**Using `os.rmdir` and `shutil.rmtree`:**
- **`os.rmdir`:** Deletes an empty directory.
  ```python
  import os
  
  # Delete empty directory 'empty_directory'
  os.rmdir('empty_directory')
  ```
  
- **`shutil.rmtree`:** Deletes a directory and its contents.
  ```python
  import shutil
  
  # Delete directory 'dir_to_delete' and all its contents
  shutil.rmtree('dir_to_delete')
  ```

### **Summary:**

- **Moving Files:** Use `shutil.move(source, destination)`.
- **Renaming Files:** Use `os.rename(old_name, new_name)`.
- **Deleting Files:** Use `os.remove(file)` for files, `os.rmdir(dir)` for empty directories, and `shutil.rmtree(dir)` for directories with contents.

======================================================================================

TODO:Working with CSV and JSON files?

### **Working with CSV Files:**

**CSV (Comma-Separated Values)** files are commonly used for data storage and manipulation.

**1. Reading CSV Files:**

**Using `csv` module:**
```python
import csv

# Reading a CSV file
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Each row is a list of strings
```

**2. Writing CSV Files:**

**Using `csv` module:**
```python
import csv

# Writing to a CSV file
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])  # Writing header
    writer.writerow(['Alice', 30, 'New York'])
    writer.writerow(['Bob', 25, 'Los Angeles'])
```

**3. Handling CSV with Headers:**

**Reading with headers:**
```python
import csv

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)  # Reads CSV into dictionaries
    for row in reader:
        print(row['Name'], row['Age'])
```

**Writing with headers:**
```python
import csv

header = ['Name', 'Age', 'City']
rows = [['Alice', 30, 'New York'], ['Bob', 25, 'Los Angeles']]

with open('data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()  # Write header
    for row in rows:
        writer.writerow(dict(zip(header, row)))
```

### **Working with JSON Files:**

**JSON (JavaScript Object Notation)** files are used for storing structured data.

**1. Reading JSON Files:**

**Using `json` module:**
```python
import json

# Reading a JSON file
with open('data.json', 'r') as file:
    data = json.load(file)  # Parses JSON into a Python dictionary
    print(data)
```

**2. Writing JSON Files:**

**Using `json` module:**
```python
import json

data = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

# Writing to a JSON file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)  # Converts Python dictionary to JSON and writes it
```

**3. Handling Pretty-Printed JSON:**

**Writing JSON with indentation:**
```python
import json

data = {
    'name': 'Bob',
    'age': 25,
    'city': 'Los Angeles'
}

with open('data_pretty.json', 'w') as file:
    json.dump(data, file, indent=4)  # Pretty-print JSON with indentation
```

**4. Converting Between JSON and Python Objects:**

**Converting JSON string to Python object:**
```python
import json

json_string = '{"name": "Alice", "age": 30, "city": "New York"}'
data = json.loads(json_string)  # Converts JSON string to Python dictionary
```

**Converting Python object to JSON string:**
```python
import json

data = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}
json_string = json.dumps(data)  # Converts Python dictionary to JSON string
```

### **Summary:**

- **CSV Files:** Use `csv.reader` for reading and `csv.writer` for writing. Use `csv.DictReader` and `csv.DictWriter` for handling headers.
- **JSON Files:** Use `json.load` and `json.dump` for reading and writing JSON to files. Use `json.loads` and `json.dumps` for converting between JSON strings and Python objects.

======================================================================================

TODO:Reading and writing binary files?

### **Reading and Writing Binary Files:**

Binary files contain data in a format that is not meant to be human-readable, such as images, audio files, or compiled programs. Python provides methods to handle binary data using the `open()` function with binary modes.

### **1. Reading Binary Files:**

**Open a File in Binary Mode:**
```python
# Open a file for reading in binary mode
with open('file.bin', 'rb') as file:
    content = file.read()  # Reads the entire file as bytes
```

**Reading Specific Bytes:**
```python
with open('file.bin', 'rb') as file:
    byte_data = file.read(10)  # Reads the first 10 bytes
```

**Reading Line by Line:**
```python
with open('file.bin', 'rb') as file:
    for line in file:
        print(line)  # Each line is read as bytes
```

### **2. Writing Binary Files:**

**Open a File in Binary Write Mode:**
```python
# Open a file for writing in binary mode
with open('file.bin', 'wb') as file:
    file.write(b'Hello, World!')  # Writes bytes to the file
```

**Writing Bytes:**
```python
data = bytes([0, 1, 2, 3, 4, 5])  # Create a bytes object
with open('file.bin', 'wb') as file:
    file.write(data)  # Write the bytes to the file
```

### **3. Appending to Binary Files:**

**Open a File in Binary Append Mode:**
```python
# Open a file for appending in binary mode
with open('file.bin', 'ab') as file:
    file.write(b'Additional data')  # Appends bytes to the end of the file
```

### **4. File Modes for Binary Files:**

- **`'rb'` (Read Binary):** Opens the file for reading in binary mode.
- **`'wb'` (Write Binary):** Opens the file for writing in binary mode (overwrites the file).
- **`'ab'` (Append Binary):** Opens the file for appending in binary mode.

### **Summary:**

- **Reading Binary Files:** Use `'rb'` mode to read. Methods include `file.read()`, `file.read(size)`, and iterating over `file`.
- **Writing Binary Files:** Use `'wb'` mode to write. Use `file.write(bytes)` for writing binary data.
- **Appending to Binary Files:** Use `'ab'` mode to append data to the end of a file.

======================================================================================

TODO:Exception handling in file operations?

### **Exception Handling in File Operations:**

When working with files, exceptions can occur due to various reasons like file not found, permission issues, or other IO errors. Python’s `try-except` blocks can handle these exceptions gracefully.

### **1. Handling File Not Found Errors:**

**Example:**
```python
try:
    with open('nonexistent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist.")
```

### **2. Handling Permission Errors:**

**Example:**
```python
try:
    with open('/root/protected_file.txt', 'r') as file:
        content = file.read()
except PermissionError:
    print("Permission denied.")
```

### **3. Handling IO Errors:**

**Example:**
```python
try:
    with open('file.txt', 'w') as file:
        file.write('Hello, World!')
except IOError:
    print("An IO error occurred.")
```

### **4. Handling Multiple Exceptions:**

**Example:**
```python
try:
    with open('file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
except IOError:
    print("IO error occurred.")
```

### **5. Using `finally` for Cleanup:**

The `finally` block executes code regardless of whether an exception was raised or not. It’s useful for cleanup operations.

**Example:**
```python
try:
    file = open('file.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()  # Ensures the file is closed
```

**Using `with` Statement (Automatically Handles Cleanup):**
The `with` statement automatically handles closing the file, even if an exception occurs.

**Example:**
```python
try:
    with open('file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
```

### **Summary:**

- **`FileNotFoundError`:** Handle cases where the file does not exist.
- **`PermissionError`:** Handle cases where the file cannot be accessed due to permissions.
- **`IOError`:** Handle general IO errors.
- **`finally`:** Use for cleanup actions like closing files.
- **`with` Statement:** Preferred method for file operations to handle exceptions and ensure files are closed automatically.

======================================================================================
"""