

# Python 3.7.10

## Definition

Python is a high-level, general-purpose programming language.

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

### Class

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

### Instance

* Realization of an object
* `__init__`: Initializes state
* `__str__`: Converts object to string

```python
class Dog:
    def __str__(self):
        return f"{self.name} is {self.age} years old"
```

### Inheritance Example

```python
class Parent:
    def __init__(self, txt):
        self.message = txt

class Child(Parent):
    def __init__(self, txt):
        super().__init__(txt)

x = Child("Hello, and welcome!")
```

* `super()`: Access parent class
* `self`: Refers to the instance of a class

### Attributes

* **Class Attribute**: Shared across all instances
* **Instance Attribute**: Unique to each instance

### Behaviors

* **Instance Methods**: Defined within a class and called by an instance

---

## Inheritance Types

* **Single**: One child from one parent
* **Multiple**: One child from multiple parents
* **Multilevel**: Chain of inheritance
* **Hierarchical**: Multiple children from one parent
* **Hybrid**: Combination of above types

---

## Encapsulation

### Example

```python
class Base:
    def __init__(self):
        self.a = "Public"
        self.__c = "Private"

class Derived(Base):
    def __init__(self):
        super().__init__()
        # Accessing private will cause an error
```

* **Protected Members**: Use `_`
* **Private Members**: Use `__`
  Not accessible outside or in derived classes.

---

## Abstraction

Hides complex implementation; only essential features are shown.

---

## Polymorphism

### Overriding

```python
class Vehicle:
    def run(self):
        print("Saves Energy")

class EV(Vehicle):
    def run(self):
        print("Runs on Electricity")
```

### Overloading

```python
class A:
    def show(self, a=None, b=None):
        print(a, b)

obj = A()
obj.show()
obj.show(4)
```

---

## Data Structures

### Built-in

* **Lists**: Ordered, mutable, any data type
* **Sets**: Unordered, unique, mutable
* **Tuples**: Ordered, immutable
* **Dictionaries**: Key-value pairs

### User-defined

* **Arrays**: Homogeneous data
* **Stacks**: LIFO
* **Queues**: FIFO
* **Trees**: Hierarchical structure
* **Linked Lists**: Nodes linked by pointers
* **HashMaps**: Like dictionaries
* **Graphs**: Vertices and edges

---

## Scaling

### Types

* **Horizontal**: Add more nodes
* **Vertical**: Increase CPU/RAM

### CPU Scaling

* Use concurrency and parallelism
* **Threads**: Run functions concurrently
* **Processes**: Independent execution units

### Thread Example

```python
import threading

def print_something(something):
    print(something)

t = threading.Thread(target=print_something, args=("hello",))
t.start()
t.join()
```

---

## Microservices

* Loosely coupled services
* Enables rapid, reliable delivery

---

## Caching

### DB Caching

* Create table:
  `python manage.py createcachetable cache_table`

* Settings:

```python
'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
'LOCATION': 'cache_table',
```

* Use Memcache/Redis for horizontal scaling

* Set `CONN_MAX_AGE` to maintain persistent connections

---

## Performance Tips

* Use PostgreSQL
* Add indexes for SELECT speed
* Tune CPU and RAM

---

## Library & API Installation Checklist

* Understand the solution it solves
* Check for bugs/stability
* Version compatibility
* Future maintenance and support

---

## JSON Handling in Python

| Method       | Description                                 |
| ------------ | ------------------------------------------- |
| `json.loads` | Converts JSON string to Python dictionary   |
| `json.dumps` | Converts Python object to JSON string       |
| `json.load`  | Parses JSON from a file object              |
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

### What is an API?

Interface for systems to communicate.

### Types

* **SOAP**: Contract-based, enterprise use
* **REST**: Web APIs, data fetch
* **GraphQL**: Flexible querying by client

### API Requests

| HTTP Method | Description            | Requests Method     |
| ----------- | ---------------------- | ------------------- |
| GET         | Read existing resource | `requests.get()`    |
| POST        | Create new resource    | `requests.post()`   |
| PUT         | Update resource        | `requests.put()`    |
| DELETE      | Delete resource        | `requests.delete()` |

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

```python
x = lambda a: a + 10
print(x(5))  # Output: 15
```

---

Let me know if you'd like a downloadable `.md` file version or formatting adjusted for a blog, slides, or documentation site.
