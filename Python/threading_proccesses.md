Great! Here’s a detailed breakdown of **Python interview questions and answers** focused on **threading, multiprocessing, and concurrency**, including how Python handles them:

---

### 🔹 **Basics: Concurrency Concepts**

**1. What is the difference between concurrency and parallelism?**

* **Concurrency**: Multiple tasks make progress over time (e.g., multitasking).
* **Parallelism**: Multiple tasks run simultaneously (requires multiple cores).

**2. Does Python support multithreading?**
Yes, Python supports multithreading, but due to the **Global Interpreter Lock (GIL)** in CPython, only one thread executes Python bytecode at a time.

---

### 🔸 **Threading in Python**

**3. What is the `threading` module?**
The `threading` module allows concurrent execution of code using threads.

```python
import threading

def print_numbers():
    for i in range(5):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()
```

**4. What are the limitations of threading in Python?**

* Due to the **GIL**, CPU-bound tasks don't benefit much from threading.
* Threading is better for **I/O-bound** tasks (e.g., network calls, file I/O).

**5. What is the Global Interpreter Lock (GIL)?**
A mutex that allows only one thread to execute Python bytecode at a time, used in **CPython**. It simplifies memory management but restricts true parallelism.

---

### 🔹 **Multiprocessing in Python**

**6. What is the `multiprocessing` module?**
It creates **separate processes** with their own Python interpreter and memory space, allowing true parallelism.

```python
from multiprocessing import Process

def show():
    print("Running in a separate process")

p = Process(target=show)
p.start()
p.join()
```

**7. When should you use multiprocessing over threading?**

* Use **threading** for **I/O-bound** tasks.
* Use **multiprocessing** for **CPU-bound** tasks to bypass the GIL and utilize multiple cores.

---

### 🔺 **Advanced Questions**

**8. How do `Pool` and `Process` differ in `multiprocessing`?**

* `Process`: Manually create and manage individual processes.
* `Pool`: Manages a pool of worker processes automatically and is great for parallel map-like operations.

```python
from multiprocessing import Pool

def square(x):
    return x * x

with Pool(4) as p:
    results = p.map(square, [1, 2, 3, 4])
```

**9. How do you share data between processes?**
Use:

* **Queue** or **Pipe** for messaging.
* **Manager** for shared state (like shared lists/dicts).

```python
from multiprocessing import Manager

with Manager() as manager:
    shared_list = manager.list()
```

**10. What are deadlocks and how do you avoid them?**
A deadlock occurs when two or more threads/processes wait indefinitely for each other’s resources.
**Avoid it by**:

* Acquiring locks in a consistent order.
* Using timeout values when acquiring locks.

---

### 🧪 Code Challenge Idea

**Problem:** Write a script that downloads 5 web pages concurrently using both threading and multiprocessing.
**Goal:** Measure the time taken in both scenarios.

---

Would you like practical exercises for these topics or want me to generate a **cheat sheet** or **PDF summary**?
