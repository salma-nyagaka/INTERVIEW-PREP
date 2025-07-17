# Python Interview Questions & Answers

## Basic Python Concepts

### Data Types and Variables

**Q: Explain the difference between mutable and immutable objects in Python. Give examples.**

**A:** In Python, objects are classified as either mutable or immutable based on whether they can be changed after creation.

**Immutable Objects:**
- Cannot be changed after creation
- Examples: `int`, `float`, `str`, `tuple`, `frozenset`, `bool`
- When you "modify" an immutable object, Python creates a new object

**Mutable Objects:**
- Can be changed after creation
- Examples: `list`, `dict`, `set`, custom objects
- Modifications happen in-place


**Implications:**
- Immutable objects are hashable and can be used as dictionary keys
- Mutable objects can lead to unexpected behavior if not handled carefully
- Immutable objects are thread-safe by default

**Q: What's the difference between `==` and `is` in Python?**

**A:** These operators test different types of equality:

**`==` (Equality operator):**
- Compares values/content of objects
- Calls the `__eq__()` method
- Can be overridden in custom classes

**`is` (Identity operator):**
- Compares object identity (memory location)
- Checks if two variables reference the same object
- Cannot be overridden

```python
# Examples
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True (same values)
print(a is b)  # False (different objects)
print(a is c)  # True (same object)

# String interning example
x = "hello"
y = "hello"
print(x == y)  # True
print(x is y)  # True (Python interns small strings)

# Integer caching
m = 100
n = 100
print(m is n)  # True (integers -5 to 256 are cached)

p = 1000
q = 1000
print(p is q)  # False (not cached)
```

**Best Practices:**
- Use `==` for value comparison
- Use `is` for singleton comparison (`None`, `True`, `False`)
- Never use `is` with numbers or strings (except for singletons)

**Q: Explain Python's variable scoping rules (LEGB rule).**

**A:** Python follows the LEGB rule for variable resolution:

**L - Local Scope:**
- Variables defined inside a function
- Highest priority in lookup

**E - Enclosing Scope:**
- Variables in the local scope of enclosing functions
- Relevant for nested functions
- An enclosing function is the outer function that contains an inner function

**G - Global Scope:**
- Variables defined at module level
- Accessible throughout the module

**B - Built-in Scope:**
- Built-in names like `print`, `len`, `str`
- Lowest priority in lookup



### Functions and Decorators

**Q: Explain different types of arguments in Python functions.**
- Parameter: The variable name in the function definition (name)
- Argument: The actual value passed when calling the function ("Alice")

**A:** Python supports several types of function arguments:

**1. Positional Arguments:**
```python
def greet(name, age):
    print(f"Hello {name}, you are {age} years old")

greet("Alice", 25)  # Must provide in order
```

**2. Keyword Arguments:**
```python
greet(age=25, name="Alice")  # Can provide in any order
```

**3. Default Arguments:**
```python
def greet(name, age=18):
    print(f"Hello {name}, you are {age} years old")

greet("Bob")  # age defaults to 18
```

**4. Variable-Length Arguments (*args):**
```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))  # 10
```

**5. Keyword Variable-Length Arguments (**kwargs):**
```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="New York")
```

**6. Combined Example:**
```python
def complex_function(required, default="default", *args, **kwargs):
    print(f"Required: {required}")
    print(f"Default: {default}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

complex_function("must_have", "custom", 1, 2, 3, name="Alice", age=25)
```

**Important Notes:**
- Order matters: positional → default → *args → **kwargs
- Avoid mutable default arguments (use `None` instead)

**Q: What are decorators? How do you create and use them?**

**A:** Decorators are functions that modify or extend the behavior of other functions without permanently modifying them.

**Basic Decorator:**
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
# Output:
# Before function call
# Hello, Alice!
# After function call
```

**Decorator with Arguments:**
```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Bob")  # Prints greeting 3 times
```

**Class-Based Decorator:**
```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count} of {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def add(x, y):
    return x + y

print(add(2, 3))  # Call 1 of add
print(add(4, 5))  # Call 2 of add
```

**Common Use Cases:**
- Logging and debugging
- Authentication and authorization
- Caching and memoization
- Timing and performance monitoring

**Q: What's the difference between a function and a method in Python?**

**A:** The main differences relate to how they're defined and called:

**Function:**
- Defined independently, not inside a class
- Called directly by name
- No automatic first parameter

**Method:**
- Defined inside a class
- Called on an instance or class
- Automatically receives first parameter (`self` for instance methods)

```python
# Function
def standalone_function(x):
    return x * 2

# Method
class MyClass:
    def __init__(self, value):
        self.value = value
    
    def instance_method(self):  # Instance method
        return self.value * 2
    
    @classmethod
    def class_method(cls, value):  # Class method
        return cls(value)
    
    @staticmethod
    def static_method(x):  # Static method
        return x * 2

# Usage
print(standalone_function(5))  # 10

obj = MyClass(5)
print(obj.instance_method())   # 10
print(MyClass.class_method(3).value)  # 3
print(MyClass.static_method(4))  # 8
```

**Method Types:**
- **Instance methods**: Operate on instance data, receive `self` as first parameter
- **Class methods**: Operate on class data, receive `cls` as first parameter, use `@classmethod`
- **Static methods**: Don't receive special first parameter, use `@staticmethod`. They behave like normal functions. When you have utility functions that are logically related to the class but don't need access to instance or class data

## Data Structures

### Lists and Tuples

**Q: When would you use a list vs a tuple vs a set?**

**A:** Each data structure has specific use cases:

**Lists:**
- **When to use**: Need ordered, mutable collection with duplicates
- **Characteristics**: Ordered, mutable, allows duplicates, indexed
- **Use cases**: Shopping cart items, sequence of operations, dynamic collections

```python
# List example
shopping_cart = ["apple", "banana", "apple"]
shopping_cart.append("orange")
print(shopping_cart[0])  # "apple"
```

**Tuples:**
- **When to use**: Need ordered, immutable collection
- **Characteristics**: Ordered, immutable, allows duplicates, indexed
- **Use cases**: Coordinates, database records, function returns, dictionary keys

```python
# Tuple example
coordinates = (10, 20)
person = ("Alice", 25, "Engineer")
# coordinates[0] = 15  # Error! Tuples are immutable
```

**Sets:**
- **When to use**: Need unique items, fast membership testing
- **Characteristics**: Unordered, mutable, no duplicates, not indexed
- **Use cases**: Removing duplicates, membership testing, mathematical operations

```python
# Set example
unique_ids = {1, 2, 3, 2, 1}  # {1, 2, 3}
print(2 in unique_ids)  # True (fast lookup)

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 & set2)  # {3} (intersection)
print(set1 | set2)  # {1, 2, 3, 4, 5} (union)
```

**Performance Comparison:**
- **List**: O(1) append, O(n) search, O(n) insert/delete
- **Tuple**: O(n) search, immutable operations
- **Set**: O(1) add/remove/lookup, no ordering

**Q: Explain list comprehensions and when to use them.**

**A:** List comprehensions provide a concise way to create lists based on existing iterables.

**Basic Syntax:**
```python
# [expression for item in iterable if condition]

# Traditional approach
squares = []
for x in range(10):
    if x % 2 == 0:
        squares.append(x**2)

# List comprehension
squares = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]
```

**Advanced Examples:**
```python
# Nested comprehensions
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Dictionary comprehension
word_lengths = {word: len(word) for word in ["hello", "world", "python"]}
# {'hello': 5, 'world': 5, 'python': 6}

# Set comprehension
unique_lengths = {len(word) for word in ["hello", "world", "python"]}
# {5, 6}

# Generator expression (memory efficient)
squares_gen = (x**2 for x in range(1000000))  # Creates generator, not list
```

**When to Use:**
- ✅ Simple transformations and filtering
- ✅ Better readability for simple operations
- ✅ Memory efficiency with generator expressions
- ❌ Complex logic (use traditional loops)
- ❌ Side effects (printing, file operations)

**Performance:**
List comprehensions are generally faster than equivalent for loops because they're optimized at the C level.

### Dictionaries

**Q: How do Python dictionaries work internally? What are the time complexities?**

**A:** Python dictionaries are implemented using hash tables with several optimizations:

**Internal Structure:**
- Uses hash function to convert keys to indices
- Handles collisions using open addressing
- Maintains insertion order (Python 3.7+)
- Compact representation to save memory

**Time Complexities:**
- **Average case**: O(1) for get, set, delete
- **Worst case**: O(n) when many hash collisions occur
- **Space complexity**: O(n)

```python
# Dictionary operations
person = {"name": "Alice", "age": 25}

# O(1) operations
print(person["name"])      # Access
person["city"] = "NYC"     # Insert
person["age"] = 26         # Update
del person["city"]         # Delete
print("name" in person)    # Membership test

# Dictionary methods
print(person.keys())       # dict_keys(['name', 'age'])
print(person.values())     # dict_values(['Alice', 26])
print(person.items())      # dict_items([('name', 'Alice'), ('age', 26)])
```

**Hash Requirements:**
- Keys must be hashable (immutable)
- Custom objects need `__hash__()` and `__eq__()` methods

```python
# Valid keys
valid_keys = {
    "string": "value",
    42: "number",
    (1, 2): "tuple",
    frozenset([1, 2]): "frozenset"
}

# Invalid keys would cause TypeError
# invalid = {[1, 2]: "list"}  # Lists are not hashable
```

**Q: What's the difference between `dict.get()` and `dict[]` for accessing values?**

**A:** These methods handle missing keys differently:

**`dict[]` (subscript notation):**
- Raises `KeyError` if key doesn't exist
- Direct access, slightly faster for existing keys

**`dict.get()`:**
- Returns `None` or specified default if key doesn't exist
- Safer for uncertain key existence

```python
person = {"name": "Alice", "age": 25}

# Using dict[]
try:
    print(person["name"])     # "Alice"
    print(person["height"])   # KeyError!
except KeyError:
    print("Key not found")

# Using dict.get()
print(person.get("name"))         # "Alice"
print(person.get("height"))       # None
print(person.get("height", 0))    # 0 (custom default)

# Practical usage
def process_user(user_data):
    # Safe access with defaults
    name = user_data.get("name", "Unknown")
    age = user_data.get("age", 0)
    is_active = user_data.get("active", True)
    
    return f"{name} ({age}) - Active: {is_active}"
```

**When to Use:**
- **`dict[]`**: When you're certain the key exists or want to handle KeyError explicitly
- **`dict.get()`**: When key might not exist and you want to provide a default

**Performance:**
`dict[]` is slightly faster for existing keys, but `dict.get()` is more robust.

## Object-Oriented Programming

### Classes and Objects

**Q: Explain the difference between `__init__` and `__new__` methods.**

**A:** Both methods are involved in object creation, but they serve different purposes:

**`__new__` method:**
- Creates the object instance
- Called before `__init__`
- Static method that returns a new instance
- Rarely overridden except for singletons or immutable types

**`__init__` method:**
- Initializes the object after it's created
- Called after `__new__`
- Instance method that modifies `self`
- Commonly overridden for object initialization

```python
class Person:
    def __new__(cls, name):
        print(f"Creating instance of {cls.__name__}")
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, name):
        print(f"Initializing instance with name: {name}")
        self.name = name

# Usage
p = Person("Alice")
# Output:
# Creating instance of Person
# Initializing instance with name: Alice
```

**Singleton Pattern using `__new__`:**
```python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            print("Singleton initialized")

# Usage
s1 = Singleton()  # Singleton initialized
s2 = Singleton()  # No output (already initialized)
print(s1 is s2)   # True
```

**Key Differences:**
- `__new__` creates, `__init__` initializes
- `__new__` returns an instance, `__init__` returns None
- `__new__` is called once per object, `__init__` can be called multiple times
- Override `__new__` for creation control, `__init__` for initialization

**Q: What are Python's magic methods (dunder methods)? Give examples.**

**A:** Magic methods (double underscore methods) define how objects behave with built-in Python operations:

**Common Magic Methods:**

**Object Creation and Representation:**
```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        # Human-readable string
        return f"{self.title} by {self.author}"
    
    def __repr__(self):
        # Developer-friendly representation
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):
        # Called by len()
        return self.pages

book = Book("1984", "George Orwell", 328)
print(str(book))    # "1984 by George Orwell"
print(repr(book))   # "Book('1984', 'George Orwell', 328)"
print(len(book))    # 328
```

**Arithmetic Operations:**
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # Vector(4, 6)
print(v1 * 3)   # Vector(3, 6)
print(v1 == v2) # False
```

**Container Methods:**
```python
class Playlist:
    def __init__(self):
        self.songs = []
    
    def __getitem__(self, index):
        return self.songs[index]
    
    def __setitem__(self, index, value):
        self.songs[index] = value
    
    def __delitem__(self, index):
        del self.songs[index]
    
    def __len__(self):
        return len(self.songs)
    
    def __contains__(self, item):
        return item in self.songs

playlist = Playlist()
playlist.songs = ["Song1", "Song2", "Song3"]
print(playlist[0])        # "Song1"
print(len(playlist))      # 3
print("Song1" in playlist) # True
```

**Context Manager:**
```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False

# Usage
with FileManager("test.txt", "w") as f:
    f.write("Hello, World!")
```

### Inheritance and Polymorphism

**Q: Explain method resolution order (MRO) in Python.**

**A:** Method Resolution Order determines the order in which Python searches for methods in inheritance hierarchies, especially with multiple inheritance.

**MRO Algorithm:**
Python uses the C3 linearization algorithm, which ensures:
- Child classes are checked before parent classes
- Left-to-right order for multiple inheritance
- Each class appears only once in the MRO

**Example:**
```python
class A:
    def method(self):
        print("A.method")

class B(A):
    def method(self):
        print("B.method")

class C(A):
    def method(self):
        print("C.method")

class D(B, C):
    pass

# Check MRO
print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# Method resolution
d = D()
d.method()  # "B.method" (B comes before C in MRO)
```

**Complex Example:**
```python
class Base:
    def method(self):
        print("Base.method")

class Left(Base):
    def method(self):
        print("Left.method")
        super().method()

class Right(Base):
    def method(self):
        print("Right.method")
        super().method()

class Child(Left, Right):
    def method(self):
        print("Child.method")
        super().method()

# MRO: Child -> Left -> Right -> Base -> object
child = Child()
child.method()
# Output:
# Child.method
# Left.method
# Right.method
# Base.method
```

**Best Practices:**
- Use `super()` instead of direct parent class calls
- Design inheritance hierarchies to be simple and logical
- Use `ClassName.__mro__` to debug inheritance issues

**Q: What's the difference between composition and inheritance?**

**A:** Both are ways to achieve code reuse, but they have different approaches and trade-offs:

**Inheritance ("is-a" relationship):**
- Subclass inherits from parent class
- Tight coupling between classes
- Supports polymorphism naturally

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):  # Dog IS-A Animal
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):  # Cat IS-A Animal
    def speak(self):
        return f"{self.name} says Meow!"

# Polymorphism
animals = [Dog("Buddy"), Cat("Whiskers")]
for animal in animals:
    print(animal.speak())
```

**Composition ("has-a" relationship):**
- Object contains other objects
- Loose coupling between classes
- More flexible and easier to test

```python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return "Engine started"

class Car:  # Car HAS-A Engine
    def __init__(self, make, model, horsepower):
        self.make = make
        self.model = model
        self.engine = Engine(horsepower)  # Composition
    
    def start(self):
        return f"{self.make} {self.model}: {self.engine.start()}"

# Usage
car = Car("Toyota", "Camry", 200)
print(car.start())  # "Toyota Camry: Engine started"
```

**When to Use:**

**Inheritance:**
- Clear "is-a" relationship
- Want to leverage polymorphism
- Behavior is fundamental to the object's nature

**Composition:**
- "has-a" or "uses-a" relationship
- Want flexibility to change behavior
- Components can be reused in different contexts
- Easier unit testing

**Modern Best Practice:**
"Favor composition over inheritance" - composition is often more flexible and maintainable.

## Advanced Topics

### Generators and Iterators

**Q: What are generators and how do they differ from regular functions?**

**A:** Generators are functions that can be paused and resumed, yielding values on-demand rather than computing all values at once.

**Key Differences:**

**Regular Function:**
```python
def get_squares(n):
    result = []
    for i in range(n):
        result.append(i**2)
    return result

squares = get_squares(5)  # [0, 1, 4, 9, 16] - all computed immediately
```

**Generator Function:**
```python
def get_squares_gen(n):
    for i in range(n):
        yield i**2

squares_gen = get_squares_gen(5)  # Generator object, nothing computed yet
print(next(squares_gen))  # 0 (computes first value)
print(next(squares_gen))  # 1 (computes second value)
```

**Benefits of Generators:**
- **Memory Efficient**: Don't store all values in memory
- **Lazy Evaluation**: Compute values only when needed
- **Infinite Sequences**: Can represent infinite data streams

**Generator Examples:**
```python
# Infinite sequence
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib))  # First 10 Fibonacci numbers

# Generator with state
def countdown(n):
    while n > 0:
        yield n
        n -= 1
    return "Done!"

# Generator expressions
squares = (x**2 for x in range(10))
even_squares = (x for x in squares if x % 2 == 0)
```

**Generator Methods:**
```python
def my_generator():
    try:
        yield 1
        yield 2
        yield 3
    except GeneratorExit:
        print("Generator is being closed")
    finally:
        print("Cleanup")

gen = my_generator()
print(next(gen))  # 1
gen.close()       # Triggers cleanup
```

**Q: Explain the iterator protocol in Python.**

**A:** The iterator protocol defines how objects can be iterated over using `for` loops and `next()`.

**Iterator Protocol Requirements:**
1. `__iter__()` method: Returns the iterator object
2. `__next__()` method: Returns the next value, raises `StopIteration` when done

**Custom Iterator:**
```python
class CountDown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1

# Usage
for num in CountDown(5):
    print(num)  # 5, 4, 3, 2, 1
```

**Iterable vs Iterator:**
```python
# Iterable (can be iterated over)
class NumberRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        return NumberRangeIterator(self.start, self.end)

# Iterator (does the actual iteration)
class NumberRangeIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1

# Usage
numbers = NumberRange(1, 5)
for num in numbers:
    print(num)  # 1, 2, 3, 4

# Can iterate multiple times
for num in numbers:
    print(num)  # 1, 2, 3, 4 (works again)
```

**Built-in Iterators:**
```python
# Lists, tuples, strings, dicts are all iterable
my_list = [1, 2, 3]
iterator = iter(my_list)
print(next(iterator))  # 1
print(next(iterator))  # 2

# File objects are iterators
with open('file.txt') as f:
    for line in f:  # Reads line by line, memory efficient
        print(line.strip())
```

### Context Managers

**Q: What are context managers and how do you implement them?**

**A:** Context managers define runtime context for executing code blocks, ensuring proper resource management with automatic cleanup.

**Two Ways to Implement:**

**1. Class-based (using `__enter__` and `__exit__`):**
```python
class DatabaseConnection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connection = None
    
    def __enter__(self):
        print(f"Connecting to {self.host}:{self.port}")
        self.connection = f"Connected to {self.host}:{self.port}"
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing connection")
        self.connection = None
        
        # Handle exceptions
        if exc_type is not None:
            print(f"Exception occurred: {exc_val}")
            return False  # Don't suppress exception
        return True

# Usage
with DatabaseConnection("localhost", 5432) as conn:
    print(f"Using {conn}")
    # Exception handling
    # raise ValueError("Something went wrong")
```

**2. Function-based (using `@contextmanager` decorator):**
```python
from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.time()
    try:
        yield start
    finally:
        end = time.time()
        print(f"Elapsed time: {end - start:.2f} seconds")

# Usage
with timer():
    time.sleep(1)
    print("Some operation")
# Output: Some operation
#         Elapsed time: 1.00 seconds
```

**Advanced Context Manager:**
```python
from contextlib import contextmanager
import threading

@contextmanager
def acquire_lock(lock):
    print("Acquiring lock...")
    acquired = lock.acquire(timeout=5)
    if not acquired:
        raise RuntimeError("Could not acquire lock")
    
    try:
        print("Lock acquired")
        yield lock
    finally:
        print("Releasing lock")
        lock.release()

# Usage
lock = threading.Lock()
with acquire_lock(lock):
    print("Critical section")
    # Do thread-safe operations
```

**Common Use Cases:**
- File operations (automatic closing)
- Database connections (automatic cleanup)
- Thread locks (automatic release)
- Temporary state changes
- Resource management

### Decorators and Metaprogramming

**Q: How do you create a decorator that takes arguments?**

**A:** Decorators with arguments require a three-level nested function structure:

**Basic Pattern:**
```python
def decorator_with_args(arg1, arg2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Use arg1, arg2, func, args, kwargs
            return func(*args, **kwargs)
        return wrapper
    return decorator

@decorator_with_args("hello", "world")
def my_function():
    pass
```

**Practical Example - Retry Decorator:**
```python
import time
import functools

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
                    print(f"Attempt {attempt + 1} failed: {e}")
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def unreliable_function():
    import random
    if random.random() < 0.7:
        raise Exception("Random failure")
    return "Success!"

# Usage
result = unreliable_function()
print(result)
```

**Caching Decorator:**
```python
def cache(max_size=100):
    def decorator(func):
        cache_dict = {}
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Create cache key
            key = str(args) + str(sorted(kwargs.items()))
            
            if key in cache_dict:
                print(f"Cache hit for {func.__name__}")
                return cache_dict[key]
            
            # Clear cache if too large
            if len(cache_dict) >= max_size:
                cache_dict.clear()
            
            result = func(*args, **kwargs)
            cache_dict[key] = result
            return result
        
        # Add cache inspection methods
        wrapper.cache_info = lambda: f"Cache size: {len(cache_dict)}"
        wrapper.cache_clear = lambda: cache_dict.clear()
        
        return wrapper
    return decorator

@cache(max_size=50)
def expensive_function(n):
    print(f"Computing for {n}")
    return n ** 2

# Usage
print(expensive_function(5))  # Computing for 5 -> 25
print(expensive_function(5))  # Cache hit -> 25
print(expensive_function.cache_info())  # Cache size: 1
```

**Q: What are metaclasses and when would you use them?**

**A:** Metaclasses are "classes that create classes" - they define how classes are constructed.

**Basic Understanding:**
```python
# Everything in Python is an object
class MyClass:
    pass

# MyClass is an instance of 'type' metaclass
print(type(MyClass))  # <class 'type'>
print(type(type))     # <class 'type'>

# Creating class with type() metaclass
MyDynamicClass = type('MyDynamicClass', (), {'attr': 'value'})
print(MyDynamicClass.attr)  # 'value'
```

**Custom Metaclass:**
```python
class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

# Usage
s1 = Singleton("first")
s2 = Singleton("second")
print(s1 is s2)  # True
print(s1.value)  # "first" (initialization only happens once)
```

**Attribute Validation Metaclass:**
```python
class ValidatedMeta(type):
    def __new__(mcs, name, bases, dct):
        # Validate all methods have docstrings
        for key, value in dct.items():
            if callable(value) and not key.startswith('_'):
                if not hasattr(value, '__doc__') or not value.__doc__:
                    raise ValueError(f"Method {key} must have a docstring")
        
        return super().__new__(mcs, name, bases, dct)

class MyClass(metaclass=ValidatedMeta):
    def method_with_doc(self):
        """This method has documentation."""
        pass
    
    # This would raise ValueError:
    # def method_without_doc(self):
    #     pass
```

**ORM-like Metaclass:**
```python
class ModelMeta(type):
    def __new__(mcs, name, bases, dct):
        # Auto-generate __init__ based on class attributes
        fields = {}
        for key, value in dct.items():
            if isinstance(value, type):
                fields[key] = value
        
        def __init__(self, **kwargs):
            for field_name, field_type in fields.items():
                value = kwargs.get(field_name)
                if value is not None and not isinstance(value, field_type):
                    raise TypeError(f"{field_name} must be {field_type.__name__}")
                setattr(self, field_name, value)
        
        dct['__init__'] = __init__
        dct['_fields'] = fields
        
        return super().__new__(mcs, name, bases, dct)

class User(metaclass=ModelMeta):
    name = str
    age = int
    email = str

# Usage
user = User(name="Alice", age=25, email="alice@example.com")
print(user.name)  # "Alice"
# user = User(name="Bob", age="invalid")  # TypeError
```

**When to Use Metaclasses:**
- Framework development (Django models, SQLAlchemy)
- API design where class creation needs customization
- Enforcing coding standards across multiple classes
- Creating domain-specific languages (DSLs)

**Remember:** "If you're not sure whether you need metaclasses, you don't need them."

## Error Handling

### Exceptions

**Q: Explain Python's exception hierarchy and how to handle exceptions properly.**

**A:** Python has a well-defined exception hierarchy with `BaseException` at the root:

**Exception Hierarchy:**
```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── StopIteration
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   └── OverflowError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── TypeError
    ├── ValueError
    └── ... (many more)
```

# Exception Handling Best Practices in Python
- An exception is an event that occurs during program execution that disrupts the normal flow of instructions. It's Python's way of signaling that something unexpected or erroneous has happened.


- Exception handling is crucial for writing robust, maintainable Python code. Here are the key best practices:


## 1. Be Specific with Exception Types

**❌ Bad: Catching all exceptions**
Don't use bare `except:` clauses as they catch all exceptions, making it difficult to identify and handle specific problems.

**✅ Good: Catch specific exceptions**
Catch specific exception types and handle each appropriately. This allows for targeted error handling and better debugging.

## 2. Use Multiple Except Blocks

Handle different exceptions with appropriate responses. For example, when making HTTP requests, handle timeout errors differently from connection errors, and authentication errors differently from server errors.

## 3. Use Finally for Cleanup

Always use `finally` for cleanup operations that must run regardless of whether an exception occurred. This is essential for closing file handles, database connections, or other resources.

## 4. Use Else Clause for Success Logic

The `else` clause runs only if no exceptions occurred in the `try` block. This is useful for code that should only run on successful completion, keeping success logic separate from error handling.

## 5. Avoid Silent Failures: Don't use bare except: pass blocks


## 6. Use Context Managers for Resource Management

**❌ Bad: Manual resource management**
Manually managing resources like file handles or database connections is error-prone and can lead to resource leaks.

**✅ Good: Use context managers**
Use `with` statements and context managers to ensure resources are properly cleaned up, even if exceptions occur.

## 7. Create Meaningful Custom Exceptions

Create custom exception classes that provide meaningful information about what went wrong. Include relevant attributes like error codes, field names, or context that will help with debugging and handling.

## 8. Use Exception Chaining

Chain exceptions to preserve the original error context using `raise ... from ...`. This maintains the full error trail while adding your own context.

## 9. Log Exceptions Properly

Use proper logging to record exceptions with appropriate levels (warning, error, critical) and include stack traces when necessary. This helps with debugging and monitoring.

## 10. Use Assertions for Debug Checks

Use assertions for conditions that should never be false during development. Assertions help catch programming errors early but can be disabled in production.

## 11. Exception Handling in Class Methods

When designing classes, ensure proper exception handling in methods. Validate inputs, handle resource cleanup, and provide meaningful error messages that help users understand what went wrong.

## 12. Testing Exception Handling

Write tests that verify your exception handling works correctly. Test both that exceptions are raised when expected and that they're not raised when they shouldn't be.

## Key Exception Handling Principles

1. **Be Specific**: Catch specific exceptions rather than using bare `except:`
2. **Handle Appropriately**: Only catch exceptions you can meaningfully handle
3. **Clean Up**: Use `finally` or context managers for resource cleanup
4. **Log Errors**: Provide meaningful error messages and logging
5. **Fail Fast**: Don't hide errors that indicate serious problems
6. **Use Custom Exceptions**: Create domain-specific exceptions for clarity
7. **Chain Exceptions**: Preserve original error context when re-raising
8. **Test Exception Paths**: Write tests for both success and failure scenarios
9. **Document Exceptions**: Document what exceptions your functions can raise
10. **Avoid Silent Failures**: Don't use bare `except: pass` blocks

Following these practices will make your code more robust, maintainable, and easier to debug!
**Q: How do you create and use custom exceptions effectively?**

**A:** Custom exceptions should be meaningful, well-structured, and provide useful information:

**Exception Hierarchy Design:**
```python
# Base exception for your application
class AppError(Exception):
    """Base exception for application errors"""
    pass

# Specific exception categories
class DatabaseError(AppError):
    """Database-related errors"""
    pass

class ValidationError(AppError):
    """Data validation errors"""
    def __init__(self, message, field_name=None, field_value=None):
        super().__init__(message)
        self.field_name = field_name
        self.field_value = field_value

class AuthenticationError(AppError):
    """Authentication-related errors"""
    pass

class AuthorizationError(AppError):
    """Authorization-related errors"""
    pass
```

**Rich Exception Information:**
```python
class HTTPError(Exception):
    def __init__(self, status_code, message, url=None, headers=None):
        self.status_code = status_code
        self.url = url
        self.headers = headers or {}
        super().__init__(message)
    
    def __str__(self):
        return f"HTTP {self.status_code}: {super().__str__()}"
    
    def is_client_error(self):
        return 400 <= self.status_code < 500
    
    def is_server_error(self):
        return 500 <= self.status_code < 600

# Usage
try:
    raise HTTPError(404, "Not Found", "https://api.example.com/users/123")
except HTTPError as e:
    print(f"Error: {e}")
    print(f"Status: {e.status_code}")
    print(f"URL: {e.url}")
    print(f"Is client error: {e.is_client_error()}")
```

**Exception Chaining:**
```python
class ProcessingError(Exception):
    """Error during data processing"""
    pass

def process_data(data):
    try:
        # Some processing that might fail
        result = complex_operation(data)
        return result
    except ValueError as e:
        # Chain the original exception
        raise ProcessingError(f"Failed to process data: {data}") from e
    except Exception as e:
        # Re-raise with additional context
        raise ProcessingError(f"Unexpected error processing: {data}") from e

def complex_operation(data):
    if not isinstance(data, dict):
        raise ValueError("Data must be a dictionary")
    return data

# Usage
try:
    process_data("invalid")
except ProcessingError as e:
    print(f"Processing error: {e}")
    print(f"Caused by: {e.__cause__}")
```

## Testing and Debugging

### Unit Testing

**Q: How do you write unit tests in Python? Explain different testing frameworks.**

**A:** Python offers several testing frameworks, with `unittest` being built-in and `pytest` being very popular:

**1. unittest (Built-in):**
```python
import unittest
from unittest.mock import patch, MagicMock

class Calculator:
    def add(self, a, b):
        return a + b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Run before each test method"""
        self.calc = Calculator()
    
    def tearDown(self):
        """Run after each test method"""
        pass
    
    def test_add(self):
        """Test addition"""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
    
    def test_divide(self):
        """Test division"""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.333333, places=5)
    
    def test_divide_by_zero(self):
        """Test division by zero raises exception"""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
    
    def test_divide_by_zero_message(self):
        """Test exception message"""
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
```

**2. pytest (Popular third-party):**
```python
# test_calculator_pytest.py
import pytest
from calculator import Calculator

class TestCalculator:
    def setup_method(self):
        """Run before each test method"""
        self.calc = Calculator()
    
    def test_add(self):
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
    
    def test_divide(self):
        assert self.calc.divide(10, 2) == 5
        assert abs(self.calc.divide(1, 3) - 0.333333) < 0.000001
    
    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(10, 0)
    
    @pytest.mark.parametrize("a,b,expected", [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
        (100, -50, 50)
    ])
    def test_add_parametrized(self, a, b, expected):
        assert self.calc.add(a, b) == expected

# Run with: pytest test_calculator_pytest.py -v
```

**3. Advanced Testing with Mocking:**
```python
import unittest
from unittest.mock import patch, MagicMock, call
import requests

class WeatherService:
    def __init__(self, api_key):
        self.api_key = api_key
    
    def get_temperature(self, city):
        response = requests.get(f"http://api.weather.com/{city}")
        if response.status_code == 200:
            return response.json()['temperature']
        raise Exception("Weather service unavailable")

class TestWeatherService(unittest.TestCase):
    def setUp(self):
        self.service = WeatherService("test_key")
    
    @patch('requests.get')
    def test_get_temperature_success(self, mock_get):
        # Mock the response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'temperature': 25}
        mock_get.return_value = mock_response
        
        # Test
        temp = self.service.get_temperature("London")
        
        # Assertions
        self.assertEqual(temp, 25)
        mock_get.assert_called_once_with("http://api.weather.com/London")
    
    @patch('requests.get')
    def test_get_temperature_failure(self, mock_get):
        # Mock failed response
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response
        
        # Test exception
        with self.assertRaises(Exception):
            self.service.get_temperature("London")
```

**4. Fixtures and Test Data:**
```python
# conftest.py (pytest fixtures)
import pytest
import tempfile
import os

@pytest.fixture
def temp_file():
    """Create a temporary file for testing"""
    fd, path = tempfile.mkstemp()
    yield path
    os.close(fd)
    os.unlink(path)

@pytest.fixture
def sample_data():
    """Provide sample data for tests"""
    return {
        'users': [
            {'id': 1, 'name': 'Alice'},
            {'id': 2, 'name': 'Bob'}
        ]
    }

# test_file_operations.py
def test_file_write_read(temp_file, sample_data):
    # Use fixtures in test
    with open(temp_file, 'w') as f:
        f.write(str(sample_data))
    
    with open(temp_file, 'r') as f:
        content = f.read()
    
    assert str(sample_data) in content
```

**Q: How do you debug Python code effectively?**

**A:** Python provides several debugging tools and techniques:

**1. Print Debugging (Basic):**
```python
def factorial(n):
    print(f"factorial({n}) called")  # Debug print
    if n <= 1:
        print(f"Base case reached: {n}")
        return 1
    result = n * factorial(n - 1)
    print(f"factorial({n}) = {result}")
    return result

print(factorial(5))
```

**2. Python Debugger (pdb):**
```python
import pdb

def complex_function(data):
    processed = []
    for item in data:
        pdb.set_trace()  # Breakpoint
        if isinstance(item, dict):
            processed.append(item['value'])
        else:
            processed.append(item * 2)
    return processed

# pdb commands:
# n (next line)
# s (step into)
# c (continue)
# l (list code)
# p <variable> (print variable)
# pp <variable> (pretty print)
# h (help)
```

**3. Context Manager Debugging:**
```python
from contextlib import contextmanager
import time

@contextmanager
def debug_timer(operation_name):
    start = time.time()
    print(f"Starting {operation_name}")
    try:
        yield
    except Exception as e:
        print(f"Error in {operation_name}: {e}")
        raise
    finally:
        end = time.time()
        print(f"{operation_name} took {end - start:.3f} seconds")

# Usage
with debug_timer("database query"):
    # Some operation
    time.sleep(0.1)
```

**4. Logging for Debugging:**
```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def process_user_data(users):
    logger.debug(f"Processing {len(users)} users")
    
    for user in users:
        logger.debug(f"Processing user: {user.get('name', 'Unknown')}")
        try:
            # Process user
            validate_user(user)
            logger.info(f"User {user['name']} processed successfully")
        except Exception as e:
            logger.error(f"Error processing user {user.get('name', 'Unknown')}: {e}")
            logger.exception("Full traceback:")  # Includes traceback

def validate_user(user):
    if 'name' not in user:
        raise ValueError("User must have a name")
    if 'email' not in user:
        raise ValueError("User must have an email")
```

**5. Profiling and Performance Debugging:**
```python
import cProfile
import pstats
from functools import wraps

def profile_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        result = func(*args, **kwargs)
        pr.disable()
        
        stats = pstats.Stats(pr)
        stats.sort_stats('cumulative')
        stats.print_stats(10)  # Top 10 functions
        
        return result
    return wrapper

@profile_function
def slow_function():
    # Simulate slow operation
    total = 0
    for i in range(100000):
        total += i ** 2
    return total

# Memory profiling with memory_profiler
# pip install memory-profiler
from memory_profiler import profile

@profile
def memory_intensive_function():
    # This will show line-by-line memory usage
    big_list = [i for i in range(100000)]
    return sum(big_list)
```

## Performance and Optimization

### Performance Tips

**Q: How do you optimize Python code for better performance?**

**A:** Python optimization involves understanding bottlenecks and applying appropriate techniques:

**1. Profiling First:**
```python
import cProfile
import time

def profile_code():
    # Code to profile
    data = list(range(100000))
    result = [x**2 for x in data if x % 2 == 0]
    return result

# Profile the code
cProfile.run('profile_code()')
```

**2. Data Structure Optimization:**
```python
# Slow: Multiple list lookups
def slow_lookup(items, targets):
    result = []
    for target in targets:
        if target in items:  # O(n) lookup
            result.append(target)
    return result

# Fast: Use set for O(1) lookup
def fast_lookup(items, targets):
    items_set = set(items)  # O(n) conversion once
    return [target for target in targets if target in items_set]  # O(1) lookup

# Performance test
import time
items = list(range(10000))
targets = [100, 200, 300, 400, 500]

start = time.time()
slow_result = slow_lookup(items, targets)
slow_time = time.time() - start

start = time.time()
fast_result = fast_lookup(items, targets)
fast_time = time.time() - start

print(f"Slow: {slow_time:.4f}s, Fast: {fast_time:.4f}s")
```

**3. String Optimization:**
```python
# Slow: String concatenation in loop
def slow_string_building(items):
    result = ""
    for item in items:
        result += str(item) + ", "  # Creates new string each time
    return result

# Fast: Use join()
def fast_string_building(items):
    return ", ".join(str(item) for item in items)

# Even faster for large datasets: Use list and join
def fastest_string_building(items):
    parts = []
    for item in items:
        parts.append(str(item))
    return ", ".join(parts)
```

**4. List Comprehensions vs Loops:**


**6. Avoid Global Variables:**


**Q: Explain the GIL (Global Interpreter Lock) and its implications.**

**A:** The Global Interpreter Lock (GIL) is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecode simultaneously.

**What GIL Does:**
- Ensures thread safety for Python objects
- Prevents race conditions in reference counting
- Simplifies memory management


**Alternatives to GIL:**
```python
# 1. Multiprocessing for CPU-bound tasks
from multiprocessing import Pool
import os

def cpu_intensive_task(n):
    return sum(i * i for i in range(n))

def use_multiprocessing():
    with Pool(processes=os.cpu_count()) as pool:
        results = pool.map(cpu_intensive_task, [1000000] * 4)
    return results

# 2. asyncio for I/O-bound tasks
import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def fetch_multiple_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    return results

# 3. Concurrent.futures for mixed workloads
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def use_concurrent_futures():
    # For I/O-bound tasks
    with ThreadPoolExecutor(max_workers=4) as executor:
        io_futures = [executor.submit(io_bound_task) for _ in range(4)]
        io_results = [f.result() for f in io_futures]
    
    # For CPU-bound tasks
    with ProcessPoolExecutor(max_workers=4) as executor:
        cpu_futures = [executor.submit(cpu_bound_task, 1000000) for _ in range(4)]
        cpu_results = [f.result() for f in cpu_futures]
    
    return io_results, cpu_results
```

**When GIL Matters:**
- **CPU-bound tasks**: Use multiprocessing
- **I/O-bound tasks**: Use threading or asyncio
- **Mixed workloads**: Use concurrent.futures

**Best Practices:**
- Profile your code to identify bottlenecks
- Use appropriate concurrency model for your use case
- Consider alternative Python implementations (PyPy, Jython) for specific needs
- Use C extensions for performance-critical code

## Libraries and Frameworks

### Popular Libraries

**Q: Explain how to work with popular Python libraries like NumPy, Pandas, and Requests.**

**A:** These libraries are essential for data science, web development, and scientific computing:

**1. NumPy (Numerical Computing):**
```python
import numpy as np

# Array creation and operations
arr = np.array([1, 2, 3, 4, 5])
matrix = np.array([[1, 2], [3, 4]])

# Array operations (vectorized)
print(arr * 2)  # [2, 4, 6, 8, 10]
print(arr + arr)  # [2, 4, 6, 8, 10]

# Mathematical functions
print(np.sqrt(arr))  # Square root
print(np.mean(arr))  # Mean
print(np.std(arr))   # Standard deviation

# Array indexing and slicing
print(arr[1:4])      # [2, 3, 4]
print(arr[arr > 3])  # [4, 5] (boolean indexing)

# Linear algebra
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.dot(a, b))  # Matrix multiplication

# Broadcasting
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_1d = np.array([10, 20, 30])
print(arr_2d + arr_1d)  # Broadcasts 1D array to 2D
```

**2. Pandas (Data Analysis):**
```python
import pandas as pd

# DataFrame creation
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New York', 'London', 'Paris']
}
df = pd.DataFrame(data)

# Data inspection
print(df.head())
print(df.info())
print(df.describe())

# Data selection
print(df['name'])  # Series
print(df[['name', 'age']])  # DataFrame
print(df[df['age'] > 28])  # Filtering

# Data manipulation
df['age_group'] = df['age'].apply(lambda x: 'Young' if x < 30 else 'Old')
df_sorted = df.sort_values('age')
df_grouped = df.groupby('age_group').mean()

# File operations
df.to_csv('data.csv', index=False)
df_loaded = pd.read_csv('data.csv')

# Missing data handling
df.fillna(0)  # Fill missing values
df.dropna()   # Drop rows with missing values

# Data aggregation
pivot_table = df.pivot_table(values='age', index='city', aggfunc='mean')
```

**3. Requests (HTTP Library):**
```python
import requests
import json

# GET request
response = requests.get('https://api.github.com/users/octocat')
print(response.status_code)  # 200
print(response.json())       # JSON response

# POST request
data = {'key': 'value'}
response = requests.post('https://httpbin.org/post', json=data)
print(response.json())

# Request with headers
headers = {'Authorization': 'Bearer token123'}
response = requests.get('https://api.example.com/data', headers=headers)

# Request with parameters
params = {'q': 'python', 'sort': 'stars'}
response = requests.get('https://api.github.com/search/repositories', params=params)

# Error handling
try:
    response = requests.get('https://api.example.com/data', timeout=5)
    response.raise_for_status()  # Raises HTTPError for bad responses
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
except requests.exceptions.Timeout:
    print("Request timed out")

# Session for persistent connections
session = requests.Session()
session.headers.update({'User-Agent': 'My App'})
response = session.get('https://api.example.com/data')
```

**Q: How do you handle asynchronous programming in Python?**

**A:** Python provides several approaches for asynchronous programming, with `asyncio` being the most common:

**1. Basic asyncio:**
```python
import asyncio
import time

# Synchronous version
def sync_task(name, duration):
    print(f"Task {name} starting")
    time.sleep(duration)
    print(f"Task {name} completed")
    return f"Result from {name}"

def run_sync_tasks():
    start = time.time()
    results = []
    results.append(sync_task("A", 2))
    results.append(sync_task("B", 1))
    results.append(sync_task("C", 3))
    print(f"Sync total time: {time.time() - start:.2f}s")
    return results

# Asynchronous version
async def async_task(name, duration):
    print(f"Task {name} starting")
    await asyncio.sleep(duration)  # Non-blocking sleep
    print(f"Task {name} completed")
    return f"Result from {name}"

async def run_async_tasks():
    start = time.time()
    # Run tasks concurrently
    tasks = [
        async_task("A", 2),
        async_task("B", 1),
        async_task("C", 3)
    ]
    results = await asyncio.gather(*tasks)
    print(f"Async total time: {time.time() - start:.2f}s")
    return results

# Run async function
if __name__ == "__main__":
    # asyncio.run(run_async_tasks())
    pass
```

**2. Async HTTP Requests:**
```python
import aiohttp
import asyncio

async def fetch_url(session, url):
    try:
        async with session.get(url) as response:
            return {
                'url': url,
                'status': response.status,
                'content': await response.text()
            }
    except Exception as e:
        return {'url': url, 'error': str(e)}

async def fetch_multiple_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)
    return results

# Usage
urls = [
    'https://httpbin.org/delay/1',
    'https://httpbin.org/delay/2',
    'https://httpbin.org/delay/3'
]

async def main():
    results = await fetch_multiple_urls(urls)
    for result in results:
        print(f"URL: {result['url']}, Status: {result.get('status', 'Error')}")

# asyncio.run(main())
```

**3. Async Context Managers:**
```python
import asyncio
import aiofiles

class AsyncDatabaseConnection:
    async def __aenter__(self):
        print("Connecting to database...")
        await asyncio.sleep(0.1)  # Simulate connection time
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Closing database connection...")
        await asyncio.sleep(0.1)  # Simulate cleanup time
        return False

    async def execute_query(self, query):
        print(f"Executing: {query}")
        await asyncio.sleep(0.2)  # Simulate query time
        return f"Result for {query}"

async def database_operations():
    async with AsyncDatabaseConnection() as db:
        result1 = await db.execute_query("SELECT * FROM users")
        result2 = await db.execute_query("SELECT * FROM orders")
        return [result1, result2]

# File I/O with aiofiles
async def read_files_async(filenames):
    async def read_file(filename):
        async with aiofiles.open(filename, 'r') as f:
            content = await f.read()
            return {'filename': filename, 'content': content}
    
    tasks = [read_file(filename) for filename in filenames]
    return await asyncio.gather(*tasks)
```

**4. Async Generators:**
```python
import asyncio
import random

async def async_data_stream():
    """Simulate streaming data"""
    for i in range(10):
        await asyncio.sleep(0.5)  # Simulate data arrival
        yield f"Data item {i}"

async def process_stream():
    async for item in async_data_stream():
        print(f"Processing: {item}")
        # Process the item
        await asyncio.sleep(0.1)

# Async comprehension
async def async_comprehension_example():
    # Async list comprehension
    results = [item async for item in async_data_stream()]
    
    # Async generator expression
    processed = (item.upper() async for item in async_data_stream())
    
    return results, processed
```

**5. Mixing Sync and Async:**
```python
import asyncio
import concurrent.futures
import time

def cpu_bound_task(n):
    """CPU-intensive task that blocks"""
    total = 0
    for i in range(n):
        total += i ** 2
    return total

async def run_cpu_bound_async(n):
    """Run CPU-bound task in thread pool"""
    loop = asyncio.get_event_loop()
    
    # Run in thread pool
    with concurrent.futures.ThreadPoolExecutor() as executor:
        result = await loop.run_in_executor(executor, cpu_bound_task, n)
    
    return result

async def mixed_workload():
    """Mix I/O and CPU tasks"""
    # I/O task
    await asyncio.sleep(1)
    
    # CPU task (non-blocking)
    cpu_result = await run_cpu_bound_async(100000)
    
    # More I/O
    await asyncio.sleep(0.5)
    
    return cpu_result
```

**Best Practices for Async Programming:**
- Use `asyncio.run()` for the main entry point
- Always `await` async functions
- Use `asyncio.gather()` for concurrent execution
- Handle exceptions properly with try-except
- Use async context managers for resource management
- Don't mix blocking and non-blocking operations

## Advanced Python Features

### Metaclasses and Descriptors

**Q: What are descriptors in Python and how do you use them?**

**A:** Descriptors are objects that define how attribute access is handled for other objects. They implement the descriptor protocol with `__get__`, `__set__`, and `__delete__` methods.

**Basic Descriptor:**
```python
class Descriptor:
    def __init__(self, name=None):
        self.name = name
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, None)
    
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value
    
    def __delete__(self, instance):
        del instance.__dict__[self.name]

class MyClass:
    attr = Descriptor('attr')

obj = MyClass()
obj.attr = "value"  # Calls __set__
print(obj.attr)     # Calls __get__
```

**Practical Example - Validation Descriptor:**
```python
class ValidatedAttribute:
    def __init__(self, validator, name=None):
        self.validator = validator
        self.name = name
    
    def __set_name__(self, owner, name):
        # Python 3.6+ automatic name setting
        self.name = name
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)
    
    def __set__(self, instance, value):
        if not self.validator(value):
            raise ValueError(f"Invalid value for {self.name}: {value}")
        instance.__dict__[self.name] = value

# Validators
def positive_number(value):
    return isinstance(value, (int, float)) and value > 0

def non_empty_string(value):
    return isinstance(value, str) and len(value.strip()) > 0

class Person:
    name = ValidatedAttribute(non_empty_string)
    age = ValidatedAttribute(positive_number)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Usage
try:
    person = Person("Alice", 25)
    print(f"{person.name} is {person.age} years old")
    
    person.age = -5  # ValueError: Invalid value for age: -5
except ValueError as e:
    print(e)
```

**Property Descriptor (Built-in):**
```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9

# Usage
temp = Temperature(25)
print(f"Celsius: {temp.celsius}°C")
print(f"Fahrenheit: {temp.fahrenheit}°F")
temp.fahrenheit = 86
print(f"Celsius: {temp.celsius}°C")
```

**Caching Descriptor:**
```python
import functools

class CachedProperty:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__
        functools.update_wrapper(self, func)
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        # Check if value is cached
        cache_name = f"_cached_{self.name}"
        if hasattr(instance, cache_name):
            return getattr(instance, cache_name)
        
        # Compute and cache value
        value = self.func(instance)
        setattr(instance, cache_name, value)
        return value
    
    def __set__(self, instance, value):
        # Allow setting cached value
        cache_name = f"_cached_{self.name}"
        setattr(instance, cache_name, value)
    
    def __delete__(self, instance):
        # Clear cached value
        cache_name = f"_cached_{self.name}"
        if hasattr(instance, cache_name):
            delattr(instance, cache_name)

class DataProcessor:
    def __init__(self, data):
        self.data = data
    
    @CachedProperty
    def processed_data(self):
        print("Processing data...")  # This will only print once
        return [x * 2 for x in self.data]
    
    @CachedProperty
    def data_sum(self):
        print("Computing sum...")  # This will only print once
        return sum(self.processed_data)

# Usage
processor = DataProcessor([1, 2, 3, 4, 5])
print(processor.processed_data)  # "Processing data..." + result
print(processor.processed_data)  # Just result (cached)
print(processor.data_sum)        # "Computing sum..." + result
print(processor.data_sum)        # Just result (cached)
```

### Memory Management

**Q: How does Python manage memory? Explain reference counting and garbage collection.**

**A:** Python uses a combination of reference counting and cyclic garbage collection for memory management:

**1. Reference Counting:**


**2. Circular References Problem:**

# Even if we delete references, objects won't be deallocated
# due to circular reference

# Force garbage collection

**4. Memory Profiling:**

**5. Memory Management Best Practices:**

**Memory Management Tips:**
- Use `__slots__` for classes with fixed attributes
- Use generators for large datasets
- Avoid circular references or use weak references
- Use appropriate data structures (deque, array, etc.)
- Profile memory usage to identify bottlenecks
- Use context managers for resource management
- Be aware of reference cycles in complex object graphs

This comprehensive guide covers the essential Python concepts and advanced topics commonly asked in interviews. Each answer includes practical examples and best practices that demonstrate real-world understanding of Python programming.