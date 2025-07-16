
**1. What is Object-Oriented Programming (OOP)?**
OOP is a programming paradigm based on **objects**, which bundle data (attributes) and behavior (methods). Python supports key OOP features such as **encapsulation**, **inheritance**, **abstraction**, and **polymorphism**.

---

**2. What is an object?**
An object is an **instance of a class** that combines data and methods.

```python
class Dog:
    def __init__(self, name):
        self.name = name

my_dog = Dog("Buddy")  # 'my_dog' is an object
```

---

**3. What is an attribute?**
An attribute is a **variable stored in an object**, representing its state.

```python
print(my_dog.name)  # Output: Buddy
```

---

**4. What is a method?**
A method is a **function defined in a class** that operates on the object’s attributes.

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof!")

my_dog = Dog("Buddy")
my_dog.bark()  # Output: Buddy says woof!
```

---

**5. What is a class and an object in Python?**
A **class** is a blueprint for creating objects. An **object** is an instance of a class.

```python
class Dog:
    def bark(self):
        print("Woof!")

my_dog = Dog()
my_dog.bark()
```

---

Here’s your updated version of the four OOP principles, with **examples** and **types of inheritance** included:

---

### **6. What are the four main principles of OOP?**

---

#### **Encapsulation**

Encapsulation hides the internal state of an object and only allows access through well-defined methods.

✅ **Example:**

```python
class Account:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

acct = Account(1000)
acct.deposit(500)
print(acct.get_balance())  # Output: 1500
print(acct.__balance)      # Error: attribute is private
```

> `__balance` is private and cannot be accessed directly. Access is only allowed via `get_balance()` and `deposit()`.

---

#### **Abstraction**

Abstraction hides complex implementation details and exposes only essential features.

✅ **Example:**

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

car = Car()
car.start_engine()  # Output: Car engine started
```

> The abstract class `Vehicle` defines an interface, and `Car` provides the specific implementation.

---

#### **Inheritance**

Inheritance allows a class (child) to inherit attributes and methods from another class (parent).

✅ **Example:**

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

dog = Dog()
dog.speak()  # Output: Dog barks
```

> `Dog` inherits the `speak` method from `Animal` and overrides it.

##### **Types of Inheritance in Python:**

| Type             | Description                               | Example Classes          |
| ---------------- | ----------------------------------------- | ------------------------ |
| **Single**       | One child, one parent                     | `class B(A):`            |
| **Multiple**     | One child, multiple parents               | `class C(A, B):`         |
| **Multilevel**   | Derived from a derived class              | `class C(B), class B(A)` |
| **Hierarchical** | Multiple children from one parent         | `class B(A), class C(A)` |
| **Hybrid**       | Combination of multiple inheritance types | Mix of above forms       |

✅ **Example (Multiple Inheritance):**

```python
class A:
    def method(self):
        print("A")

class B:
    def method(self):
        print("B")

class C(A, B): pass

c = C()
c.method()  # Output: A (based on MRO)
```

---

#### **Polymorphism**

Polymorphism allows different classes to implement the same method in their own way.

✅ **Example:**

```python
class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Bark")

def make_animal_speak(animal):
    animal.speak()

make_animal_speak(Cat())  # Output: Meow
make_animal_speak(Dog())  # Output: Bark
```

> The `speak()` method is implemented differently in `Cat` and `Dog`, but used polymorphically.


---

**7. What is inheritance and how is it implemented in Python?**

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Bark")

dog = Dog()
dog.speak()  # Output: Bark
```

---

Sure! Here's an improved version of:

---

### **8. What is method overriding?**

**Method overriding** occurs when a **subclass provides a specific implementation** of a method that is already defined in its **parent class**. This allows the subclass to **customize or completely replace** the behavior of the inherited method.

✅ **Example:**

```python
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):  # Overriding the 'speak' method from Animal
        print("Dog barks")

class Cat(Animal):
    def speak(self):  # Overriding the 'speak' method from Animal
        print("Cat meows")

# Usage
dog = Dog()
cat = Cat()

dog.speak()  # Output: Dog barks
cat.speak()  # Output: Cat meows
```

> Both `Dog` and `Cat` override the `speak()` method of the `Animal` class to provide class-specific behavior.
---



**9. What is the difference between instance methods, class methods, and static methods?**

* **Instance method**: Takes `self` as the first argument.
* **Class method**: Takes `cls` and uses `@classmethod`.
* **Static method**: Takes neither; uses `@staticmethod`.

```python
class Example:
    def instance_method(self):
        return "instance"

    @classmethod
    def class_method(cls):
        return "class"

    @staticmethod
    def static_method():
        return "static"
```

---

**10. What is multiple inheritance?**

```python
class A:
    def method(self): print("A")

class B:
    def method(self): print("B")

class C(A, B): pass

c = C()
c.method()  # Output: A (based on MRO)
```

---

**11. What is Method Resolution Order (MRO) in Python?**
MRO is the sequence Python follows to look up methods in inheritance hierarchies. Use `Class.mro()` or `Class.__mro__`.

---

**12. What are `__init__` and `__new__` methods?**

* `__init__`: Initializes a newly created object.
* `__new__`: Creates the object; used mainly with immutable types.

---

**13. What is the difference between composition and inheritance?**

* **Inheritance**: "is-a" relationship (reuse via parent class).
* **Composition**: "has-a" relationship (reuse via containing objects).

---

**14. What are dunder (magic) methods?**
Special methods that begin and end with double underscores to customize behavior.

```python
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book: {self.title}"
```

---

**15. What is encapsulation and how is it implemented in Python?**
Encapsulation restricts direct access to object data. Python enforces this via naming conventions:

* `_var`: Protected (convention only)
* `__var`: Private (name-mangled)

---

Let me know if you'd like this as a downloadable **PDF**, **flashcards**, or **quiz format**!
