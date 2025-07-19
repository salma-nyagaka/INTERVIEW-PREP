# Python 3.13.5
system architecture

## Definition

Python is a high-level, interpreted programming language known for its simple, readable syntax that resembles English

---

## Uses

* Developing websites and software
* Task automation
* Data analysis
* Data visualization

---

## Advantages

* **Easy to Read, Learn and Write**
  Python has an English-like syntax, making it easier to read and understand.

* **Interpreted Language**
  Executes code line by line. Stops and reports errors immediately when they occur.

* **Very Productive**
  Developers focus on problem-solving rather than syntax complexities.

* **Dynamically Typed**
  No need to declare variable types explicitly (duck typing).

* **Free and Open-Source**
  Can be used, modified, and redistributed freely.

* **Vast Library Support**
  Extensive standard library that reduces the need for external packages.

* **Portability**
  Code can be written once and run on any platform without changes.

---

## Disadvantages

* **Slow Speed**
  Line-by-line execution and dynamic typing slow it down.

* **Not Memory Efficient**
  Uses a lot of memory for simplicity.

* **Weak in Mobile Computing**
  Rarely used in mobile apps due to memory and performance limitations.

* **Database Access**
  Less robust when working with databases.

* **Runtime Errors**
  Dynamically typed nature can lead to type-related runtime errors.

---

## Object-Oriented Programming (OOP)

### Concept

Structuring a program by bundling properties and behaviors into objects.

#### Class

A template for creating objects.

**Instance**
* Realization of an object
* `__init__`: Initializes state
* `__str__`: Converts object to string


**Attributes**

* **Class Attribute**: Shared across all instances
* **Instance Attribute**: Unique to each instance

**Behaviors**

* **Instance Methods**: Defined within a class and called by an instance

#### Inheritance
* `super()`: Access parent class
* `self`: Refers to the instance of a class


**Inheritance Types**
* **Single**: One child from one parent
* **Multiple**: One child from multiple parents
* **Multilevel**: Chain of inheritance
* **Hierarchical**: Multiple children from one parent
* **Hybrid**: Combination of above types


##### Encapsulation
- Bundles data and methods together while controlling access to the internal workings of an object.
* **Protected Members**: Use `_`.
    - attributes or methods intended for internal use within a class and its subclasses, but not for external/public access.
* **Private Members**: Use `__`
    - Not accessible outside or in derived classes.


##### Abstraction
- Hides complex implementation; only essential features are shown.


##### Object 

- Actual instance created from class 


##### Polymorphism
    
- It's the ability for different objects to respond to the same interface/method call in their own unique way.

1. **Overriding**

- Child class replaces parent's method with its own implementation:

2. **Overloading**

- Same method name handles different parameter combinations:


---

## Data Structures

- A way to organize and store data in memory for efficient access and manipulation.

### Built-in

* **Lists**: Ordered, mutable, any data type
* **Sets**: Unordered, unique, mutable
* **Tuples**: Ordered, immutable
* **Dictionaries**: Key-value pairs

### User-defined
* **Arrays**: Fixed-size collection of elements of the same type stored in contiguous memory locations.

* **Stacks**: Last In, First Out (LIFO) structure - like a stack of plates, you can only add/remove from the top.

* **Queues**: First In, First Out (FIFO) structure - like a line at a store, first person in line gets served first.

* **Trees**: Hierarchical structure with parent-child relationships, like a family tree or folder structure.

* **Linked Lists**: Chain of nodes where each node contains data and a pointer/reference to the next node.

* **HashMaps**: Key-value storage using hash functions for fast lookup, similar to Python dictionaries.

* **Graphs**: Network of vertices (nodes) connected by edges, like social networks or city road maps.


---

## Scaling Techniques

### Horizontal Scaling (Scale Out)
**Definition**: Add more servers/machines to handle increased load.

**Techniques:**
* **Load Balancing**: Distribute requests across multiple servers
* **Microservices**: Break application into independent services
* **Database Sharding**: Split database across multiple servers
* **Content Delivery Networks (CDN)**: Distribute content globally
* **Auto-scaling**: Automatically add/remove servers based on demand
* **Clustering**: Group multiple servers to work as one system
* **Message Queues**: Distribute work across multiple workers
* **Caching Layers**: Multiple cache servers (Redis clusters)

**Pros**: Nearly unlimited scaling, fault tolerance, cost-effective for large scale
**Cons**: Complex setup, network latency, data consistency challenges

---

### Vertical Scaling (Scale Up)
**Definition**: Increase power of existing server (CPU, RAM, storage).

**Techniques:**
* **CPU Upgrade**: More cores or faster processors
* **Memory Increase**: Add more RAM for better performance
* **Storage Enhancement**: Faster SSDs or more disk space
* **Network Upgrade**: Higher bandwidth connections
* **Database Optimization**: Better indexes, query optimization
* **Code Optimization**: Improve application efficiency
* **Caching**: In-memory caching (Redis, Memcached)
* **Connection Pooling**: Reuse database connections

**Pros**: Simple implementation, no architectural changes, low latency(ime delay between when a request is made and when a response is received.)
**Cons**: Hardware limits, single point of failure, expensive at scale

---

### Hybrid Approach
Most real-world systems use **both** techniques:
- Vertical scaling for immediate performance boosts
- Horizontal scaling for long-term growth and reliability

**Example**: Start with a powerful server (vertical), then add more servers behind a load balancer (horizontal) as traffic grows.
* Set `CONN_MAX_AGE` to maintain persistent connections

---



## Library & API Installation Checklist

* Understand the solution it solves
* Check for bugs/stability
* Version compatibility
* Future maintenance and support

---

## JSON Handling in Python
-  lightweight, text-based data format used to store and exchange data between systems.

| Method       | Description                                 |
| ------------ | ------------------------------------------- |
| `json.loads` | Converts JSON string to Python dictionary   |
| `json.dumps` | Converts Python object to JSON string       |
| `json.load`  | Parses(means to analyze and break down data into understandable components that a program can work with.) JSON from a file object              |
| `json.dump`  | Converts Python object and writes to a file |

---

## ORM (Object-Relational Mapping)

Converts data between relational DB and OOP languages.

---

## Multithreading vs Multiprocessing

* **Multithreading**:
  Threads share memory, run concurrently (not in parallel due to GIL)

* **Multiprocessing**:
  Processes run in parallel, with separate memory

---

## Design Concepts

* **Design Patterns**
* **Architecture Design**
* **Data Scraping**
* **System Integration**

---

## APIs

####  What is an API?

Interface for systems to communicate.

 **REST** (Representational State Transfer) is an **architectural style** for designing web APIs that use standard HTTP methods to interact with resources.

**Core Principles:**
- **Stateless**: Each request contains all needed information
- **Resource-based**: Everything is a resource with a unique URL
- **HTTP Methods**: Use standard verbs (GET, POST, PUT, DELETE)
- **Standard formats**: Usually JSON for data exchange

**HTTP Methods & Actions:**
- **GET**: Retrieve/read data
- **POST**: Create new resource
- **PUT**: Update entire resource
- **PATCH**: Update part of resource
- **DELETE**: Remove resource

**Example REST API:**
```
GET    /users          → Get all users
GET    /users/123      → Get user with ID 123
POST   /users          → Create new user
PUT    /users/123      → Update user 123
DELETE /users/123      → Delete user 123
```

**REST vs Other APIs:**
- **SOAP**: Heavy, XML-based, complex contracts
- **GraphQL**: Single endpoint, client specifies data needed
- **REST**: Simple, standard HTTP, resource-focused

**Key Features:**
- **Predictable URLs**: Clear resource paths
- **Standard status codes**: 200 (OK), 404 (Not Found), 500 (Error)
- **Cacheable**: Responses can be cached for performance
- **Platform independent**: Works with any language/framework

**Real-World Analogy:**
Like a **library system** - you know exactly where to find books (predictable locations), what actions you can perform (borrow, return, search), and the rules are the same everywhere.

**Why Popular:**
- Simple to understand and implement
- Uses existing web standards
- Scalable and flexible
- Wide tool support

### HTTP Headers

| Header       | Description                              |
| ------------ | ---------------------------------------- |
| Accept       | Content types client accepts             |
| Content-Type | Format of data sent/received (e.g. JSON) |
| User-Agent   | Client software                          |
| Server       | Server software                          |

### API Response Attributes

* `.text` — Returns response as Unicode
* `.content` — Returns response as bytes

---

## Lambda Functions

Anonymous functions that can have any number of arguments but can only have one expression.

```bash
add = lambda a, b: a + b
print(add(3, 4)) 
```
---

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
```

**Best Practices:**
- Use `==` for value comparison
- Use `is` for singleton comparison (`None`, `True`, `False`)
- Never use `is` with numbers or strings (except for singletons)

**Q. HOF.**
- Typically stands for Higher-Order Functions in programming.
Higher-Order Functions are functions that:

- Take other functions as arguments, OR
- Return functions as results, OR
- Decorators 

##### Benefits:
- Code reusability: Same function works with different operations
- Abstraction: Hide implementation details
- Functional programming: Compose complex operations from simple ones



##### Built in -> lambda, filter
 - map(): Like a factory assembly line - every item goes through the same process and comes out transformed.
- filter(): Like a security checkpoint - only items that pass the test are allowed through

```bash
# Get squares of even numbers only
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Method 1: Filter first, then map
evens = filter(lambda x: x % 2 == 0, numbers)
squares_of_evens = list(map(lambda x: x**2, evens))
print(squares_of_evens)  # [4, 16, 36, 64, 100]

# Method 2: Map first, then filter
squares = map(lambda x: x**2, numbers)
even_squares = list(filter(lambda x: x % 2 == 0, squares))
print(even_squares)  # [4, 16, 36, 64, 100]
```



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
Must provide in order

**2. Keyword Arguments:**
Can provide in any order

**3. Default Arguments:**
Parameters with default values

**4. Variable-Length Arguments args**
Accept any number of positional arguments

**5. Keyword Variable-Length Arguments kwargs :**
Accept any number of keyword arguments

**Important Notes:**
- Order matters: positional → default → *args → **kwargs
- Avoid mutable default arguments (use `None` instead)

**Q: What are decorators? How do you create and use them?**

**A:** Decorators are functions that modify or extend the behavior of other functions without permanently modifying them.

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

**Method Types:**
- **Instance methods**: Operate on instance data, receive `self` as first parameter
- **Class methods**: Operate on class data, receive `cls` as first parameter, use `@classmethod`
- **Static methods**: Don't receive special first parameter, use `@staticmethod`. They behave like normal functions. When you have utility functions that are logically related to the class but don't need access to instance or class data


**Q: Explain list comprehensions and when to use them.**

**A:** List comprehensions provide a concise way to create lists based on existing iterables.

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

**Hash Requirements:**
- Keys must be hashable (immutable)
- Custom objects need `__hash__()` and `__eq__()` methods

**Q: What's the difference between `dict.get()` and `dict[]` for accessing values?**

**A:** These methods handle missing keys differently:

**`dict[]` (subscript notation):**
- Raises `KeyError` if key doesn't exist
- Direct access, slightly faster for existing keys

**`dict.get()`:**
- Returns `None` or specified default if key doesn't exist
- Safer for uncertain key existence

**When to Use:**
- **`dict[]`**: When you're certain the key exists or want to handle KeyError explicitly
- **`dict.get()`**: When key might not exist and you want to provide a default

**Performance:**
`dict[]` is slightly faster for existing keys, but `dict.get()` is more robust.

## Object-Oriented Programming

### Classes and Objects


**Q: What are Python's magic methods (dunder methods)? Give examples.**

**A:** Magic methods (double underscore methods) define how objects behave with built-in Python operations:

**Common Magic Methods:**

**Object Creation and Representation:**
- `__init__`: Object initialization
- `__str__`: Human-readable string representation
- `__repr__`: Developer-friendly representation
- `__len__`: Called by len()

**Arithmetic Operations:**
- `__add__`: Addition (+)
- `__mul__`: Multiplication (*)
- `__eq__`: Equality (==)

**Container Methods:**
- `__getitem__`: Index access ([])
- `__setitem__`: Index assignment
- `__delitem__`: Index deletion
- `__contains__`: Membership test (in)

**Context Manager:**
- `__enter__`: Entering context
- `__exit__`: Exiting context


**Q: Explain method resolution order (MRO) in Python.**

**A:** Method Resolution Order determines the order in which Python searches for methods in inheritance hierarchies, especially with multiple inheritance.

**MRO Algorithm:**
Python uses the C3 linearization algorithm, which ensures:
- Child classes are checked before parent classes
- Left-to-right order for multiple inheritance
- Each class appears only once in the MRO

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

**Composition ("has-a" relationship):**
- Object contains other objects
- Loose coupling between classes
- More flexible and easier to test

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

**Benefits of Generators:**
- **Memory Efficient**: Don't store all values in memory
- **Lazy Evaluation**: Compute values only when needed
- **Infinite Sequences**: Can represent infinite data streams

**Q: Explain the iterator protocol in Python.**

**A:** The iterator protocol defines how objects can be iterated over using `for` loops and `next()`.

**Iterator Protocol Requirements:**
1. `__iter__()` method: Returns the iterator object
2. `__next__()` method: Returns the next value, raises `StopIteration` when done

**Iterable vs Iterator:**
- **Iterable**: Object that can be iterated over (has `__iter__()`)
- **Iterator**: Object that does the actual iteration (has `__iter__()` and `__next__()`)

### Context Managers

**Q: What are context managers and how do you implement them?**

**A:** Context managers define runtime context for executing code blocks, ensuring proper resource management with automatic cleanup.

**Two Ways to Implement:**

**1. Class-based (using `__enter__` and `__exit__`):**
Define `__enter__` and `__exit__` methods

**2. Function-based (using `@contextmanager` decorator):**
Use contextlib.contextmanager decorator with yield

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
```
def decorator_with_args(arg1, arg2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Use arg1, arg2, func, args, kwargs
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

**Q: What are metaclasses and when would you use them?**

**A:** Metaclasses are "classes that create classes" - they define how classes are constructed.

**Basic Understanding:**
Everything in Python is an object, including classes. Classes are instances of metaclasses.

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
Create a base exception for your application and specific categories for different error types.

**Rich Exception Information:**
Include relevant data like status codes, URLs, field names, and methods to check error types.

**Exception Chaining:**
Use `raise ... from ...` to preserve original error context while adding your own.

## Testing and Debugging

### Unit Testing

**Q: How do you write unit tests in Python? Explain different testing frameworks.**

**A:** Python offers several testing frameworks, with `unittest` being built-in and `pytest` being very popular:

**1. unittest (Built-in):**
Uses classes that inherit from unittest.TestCase with methods like setUp, tearDown, assertEqual, assertRaises.

**2. pytest (Popular third-party):**
Uses simple functions with assert statements, provides fixtures, parametrized tests, and better error reporting.

**3. Advanced Testing with Mocking:**
Use unittest.mock to mock external dependencies like API calls, database connections, or file operations.

**4. Fixtures and Test Data:**
pytest fixtures provide reusable test data and setup/teardown functionality.

**Q: How do you debug Python code effectively?**

**A:** Python provides several debugging tools and techniques:

**1. Print Debugging (Basic):**
Simple print statements to trace execution flow.

**2. Python Debugger (pdb):**
Built-in debugger with breakpoints and interactive debugging.
Commands: n (next), s (step), c (continue), l (list), p (print)

**3. Context Manager Debugging:**
Custom context managers for timing and error tracking.

**4. Logging for Debugging:**
Use logging module with different levels (debug, info, warning, error).

**5. Profiling and Performance Debugging:**
Use cProfile, pstats, and memory_profiler to identify bottlenecks.

## Performance and Optimization

### Performance Tips

**Q: How do you optimize Python code for better performance?**

**A:** Python optimization involves understanding bottlenecks and applying appropriate techniques:

**1. Profiling First:**
Always profile before optimizing to identify real bottlenecks.

**2. Data Structure Optimization:**
Use appropriate data structures (sets for membership testing, deques for queues).

**3. String Optimization:**
Use join() instead of concatenation in loops.

**4. List Comprehensions vs Loops:**
List comprehensions are generally faster than equivalent for loops.

**6. Avoid Global Variables:**
Local variable access is faster than global variable access.

**Q: Explain the GIL (Global Interpreter Lock) and its implications.**

**A:** The Global Interpreter Lock (GIL) is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecode simultaneously.

**What GIL Does:**
- Ensures thread safety for Python objects
- Prevents race conditions in reference counting
- Simplifies memory management

**Alternatives to GIL:**
- Multiprocessing for CPU-bound tasks
- asyncio for I/O-bound tasks
- Concurrent.futures for mixed workloads

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
- Array creation and vectorized operations
- Mathematical functions and linear algebra
- Broadcasting for operations on arrays of different shapes

**2. Pandas (Data Analysis):**
- DataFrame and Series for structured data
- Data manipulation, filtering, and grouping
- File I/O operations (CSV, Excel, JSON)
- Missing data handling

**3. Requests (HTTP Library):**
- GET, POST, PUT, DELETE requests
- Headers, parameters, and authentication
- Error handling and timeouts
- Session management for persistent connections

**Q: How do you handle asynchronous programming in Python?**

**A:** Python provides several approaches for asynchronous programming, with `asyncio` being the most common:

**1. Basic asyncio:**
async/await syntax for defining and running asynchronous functions.

**2. Async HTTP Requests:**
Using aiohttp for concurrent HTTP requests.

**3. Async Context Managers:**
__aenter__ and __aexit__ methods for resource management.

**4. Async Generators:**
async for loops and async comprehensions.

**5. Mixing Sync and Async:**
Using run_in_executor to run blocking code in thread pools.

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

**Descriptor Protocol:**
- `__get__(self, instance, owner)`: Called when attribute is accessed
- `__set__(self, instance, value)`: Called when attribute is assigned
- `__delete__(self, instance)`: Called when attribute is deleted

**Common Use Cases:**
- Data validation
- Computed properties
- Caching
- Type checking

### Memory Management

**Q: How does Python manage memory? Explain reference counting and garbage collection.**

memory cleanup system that finds and removes objects that are no longer being used by your program.

**A:** Python uses a combination of reference counting and cyclic garbage collection for memory management:

**1. Reference Counting:**
Every object has a reference count that tracks how many variables point to it.

**2. Circular References Problem:**
When objects reference each other in a cycle, reference counting alone cannot clean them up.

**4. Memory Profiling:**
Tools and techniques for monitoring memory usage and identifying leaks.

**5. Memory Management Best Practices:**
- Use `__slots__` for classes with fixed attributes
- Use generators for large datasets
- Avoid circular references or use weak references
- Use appropriate data structures
- Profile memory usage to identify bottlenecks

**Memory Management Tips:**
- Use `__slots__` for classes with fixed attributes
- Use generators for large datasets
- Avoid circular references or use weak references
- Use appropriate data structures (deque, array, etc.)
- Profile memory usage to identify bottlenecks
- Use context managers for resource management
- Be aware of reference cycles in complex object graphs

This comprehensive guide covers the essential Python concepts and advanced topics commonly asked in interviews. Each answer includes practical examples and best practices that demonstrate real-world understanding of Python programming.