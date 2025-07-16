
### 🔹 Beginner-Level Questions and Answers

**1. What are the key features of Python?**

* Easy to read and write
* Interpreted and dynamically typed
* High-level language
* Large standard library
* Supports OOP and functional programming
* Platform-independent

**2. What is the difference between a list and a tuple?**

* **List**: Mutable, defined using `[]`
* **Tuple**: Immutable, defined using `()`

**3. What is PEP 8 and why is it important?**
PEP 8 is the Python Enhancement Proposal that provides guidelines and best practices for writing clean Python code. It promotes code readability and consistency.

**4. What are Python’s data types?**

* Numeric: `int`, `float`, `complex`
* Sequence: `list`, `tuple`, `range`, `str`
* Set: `set`, `frozenset`
* Mapping: `dict`
* Boolean: `bool`
* Binary: `bytes`, `bytearray`, `memoryview`

**5. What is the difference between `is` and `==`?**

* `==` checks **value equality**
* `is` checks **object identity**

---

### 🔸 Intermediate-Level Questions and Answers

**1. What are list comprehensions?**
A concise way to create lists:

```python
squares = [x*x for x in range(5)]
```

**2. What is a generator?**
A function that yields values one at a time using `yield`, conserving memory.

```python
def gen():
    for i in range(3):
        yield i
```

**3. What is a decorator?**
A function that modifies another function’s behavior.

```python
def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper
```

**4. What’s the difference between `deepcopy()` and `copy()`?**

* `copy()` creates a shallow copy (nested objects are referenced).
* `deepcopy()` creates a deep copy (all nested objects are copied).

**5. What does the `with` statement do?**
Manages context (like files) automatically, ensuring cleanup:

```python
with open("file.txt") as f:
    data = f.read()
```

---

### 🔺 Advanced-Level Questions and Answers

**1. What are metaclasses?**
Metaclasses are classes of classes. They define how classes behave. You can control class creation using `__new__` and `__init__`.

**2. What is the Global Interpreter Lock (GIL)?**
GIL is a mutex in CPython that allows only one thread to execute Python bytecode at a time, affecting true parallelism in multithreading.

**3. How does async/await work?**
Used for asynchronous programming. `async` defines a coroutine, and `await` pauses execution until the awaited task is done.

```python
async def fetch():
    await some_async_call()
```

**4. What is `__slots__`?**
Used to restrict attribute creation in a class and save memory by preventing the creation of `__dict__`:

```python
class MyClass:
    __slots__ = ['x', 'y']
```

**5. What are descriptors?**
Objects that define `__get__`, `__set__`, or `__delete__` to manage attribute access. Often used in custom property implementations.

---

Would you like more **hands-on coding tasks with solutions** or questions for specific roles like **Data Scientist** or **Backend Developer**?
