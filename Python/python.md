# Python Interview Questions and Answers

### 1. What are Python decorators and how do you use them?

**Answer:**
Decorators in Python are a way to modify or enhance functions or methods without changing their actual code. They are functions that take another function as an argument and extend its behavior. Decorators are often used for logging, access control, instrumentation, and caching.

Example:
```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

### 2. Explain the difference between `deepcopy` and `shallow copy`.

**Answer:**
- **Shallow Copy**: Creates a new object, but inserts references into it to the objects found in the original. Changes to mutable objects in the shallow copy will affect the original.
- **Deep Copy**: Creates a new object and recursively copies all objects found in the original, creating a fully independent clone.

Example:
```python
import copy

original = [[1, 2, 3], [4, 5, 6]]
shallow_copied = copy.copy(original)
deep_copied = copy.deepcopy(original)

original[0][0] = 'X'
print(shallow_copied)  # [['X', 2, 3], [4, 5, 6]]
print(deep_copied)     # [[1, 2, 3], [4, 5, 6]]
```

### 3. What is the Global Interpreter Lock (GIL) in Python?

**Answer:**
The Global Interpreter Lock (GIL) is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecode simultaneously. This means that even in a multi-threaded Python program, only one thread can execute at a time. The GIL can be a bottleneck in CPU-bound and multi-threaded code, but it does not affect I/O-bound multi-threaded programs.

### 4. How do you manage memory in Python?

**Answer:**
Python manages memory using a private heap space where all objects and data structures are stored. The memory manager handles the allocation of heap space for Python objects. Python also has a built-in garbage collector that recycles unused memory, which helps in managing memory automatically.

### 5. What are list comprehensions and how do they differ from generator expressions?

**Answer:**
- **List Comprehensions**: Provide a concise way to create lists. They consist of brackets containing an expression followed by a `for` clause, and then zero or more `for` or `if` clauses. The result is a new list resulting from evaluating the expression in the context of the `for` and `if` clauses.

Example:
```python
squares = [x**2 for x in range(10)]
```

- **Generator Expressions**: Similar to list comprehensions, but use parentheses instead of brackets. They return a generator object that can be iterated over, which is more memory efficient for large datasets.

Example:
```python
squares_gen = (x**2 for x in range(10))
```

### 6. Explain the concept of monkey patching in Python.

**Answer:**
Monkey patching refers to the dynamic modification of a class or module at runtime. This can be useful for modifying third-party code or for testing purposes. However, it should be used with caution as it can lead to code that is difficult to understand and maintain.

Example:
```python
class A:
    def method(self):
        print("Original method")

def patched_method(self):
    print("Patched method")

A.method = patched_method
a = A()
a.method()  # Output: Patched method
```
