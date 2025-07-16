## Interview Preparation: Data Science, Information Systems & Analytics Developer (Intermediate Level)

### Fundamentals

**1. What is Git?**
Git is a distributed version control system that helps developers track changes in code, collaborate with others, and manage different versions of a project.

**2. What is Celery?**
Celery is an asynchronous task queue/job queue system based on distributed message passing. It's used to run time-consuming tasks (like sending emails or processing data) in the background.

**3. What are Queues and Tasks in Celery?**\\

* **Queue**: A list-like structure where tasks wait to be picked up by workers.
* **Task**: A unit of work (Python function) that Celery executes asynchronously.

**4. What does Asynchronous Mean?**
Asynchronous execution allows code to run in the background without waiting for other operations to complete, enabling the system to handle more tasks concurrently.

**5. What is Redis Server?**
Redis is an in-memory key-value data store often used as a message broker in Celery. It supports data structures such as strings, hashes, lists, sets, and more.

**6. What is Threading?**
Threading is a programming technique that allows multiple threads (smaller units of a process) to run concurrently within the same application, sharing memory.

**7. What is Multithreading?**
Multithreading involves running multiple threads in parallel within a single process to improve the efficiency of I/O-bound operations. Python’s `threading` module supports this.

**8. What are Processes?**
Processes are independent execution units with their own memory space. Unlike threads, they do not share memory and are used to achieve true parallelism, especially in CPU-bound tasks.

---

### GIT: Workflows, Pull Requests, Issues, Actions

**1. What is a pull request?**
A pull request (PR) is a request to merge changes from one branch (usually feature or bugfix) into another (usually main or develop). It allows for code review, discussions, and CI checks before merging.

**2. What are GitHub Issues used for?**
GitHub Issues are used for tracking bugs, feature requests, tasks, or questions related to the project. They support tagging, assignment, and linking to commits/PRs.

**3. Describe a typical Git workflow in a team.**

* Main branches: `main` (production), `develop` (next release)
* Feature branches: `feature/feature-name`
* Bugfix branches: `bugfix/bug-description`
* Release branches: `release/x.x`
* Hotfix branches: `hotfix/urgent-fix`
  Steps:

1. Branch off from `develop`
2. Commit work regularly
3. Push to remote
4. Open PR → review → merge

**4. What is GitHub Actions?**
GitHub Actions is a CI/CD tool that lets you automate workflows such as testing, building, and deploying. You define workflows in `.github/workflows/*.yml`.

**Example:**

```yaml
name: Django Test
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: python manage.py test
```

**5. How do you squash commits before merging?**
Use `git rebase -i HEAD~n`, mark commits as `squash`, and force push.

**6. How do you handle a broken deployment caused by a recent commit?**
Identify the commit via `git log`, use `git revert <sha>` or roll back the release via CI/CD.

---

### Celery in Django: Setup and Configuration

**1. How do you set up Celery in a Django project?**

**Steps:**

1. Install:

```bash
pip install celery redis
```

2. Create `celery.py` in project root:

```python
from __future__ import absolute_import
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
app = Celery('myproject')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
```

3. In `__init__.py`:

```python
from .celery import app as celery_app
__all__ = ['celery_app']
```

4. In `settings.py`:

```python
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Africa/Nairobi'
```

5. Create tasks in `app/tasks.py`:

```python
from celery import shared_task

@shared_task
def add(x, y):
    return x + y
```

6. Run workers:

```bash
celery -A myproject worker --loglevel=info
```

**2. How do you schedule periodic tasks?**
Install `django-celery-beat` and define tasks in `PeriodicTask` model via Django admin or code.

**3. What broker and backend did you use with Celery?**
Redis for both (fast, reliable, easy to set up).

**4. Explain how you monitor and retry failed Celery tasks.**
Use Flower for monitoring. Implement retry policies in tasks:

```python
@shared_task(bind=True, max_retries=3)
def task_name(self, ...):
    try:
        ...
    except Exception as e:
        self.retry(exc=e, countdown=60)
```

**5. How do you handle long-running tasks and ensure task results aren’t lost?**
Use durable backend like Redis or database. Set `acks_late=True` and `task_acks_on_failure_or_timeout = False` to avoid loss on crashes.

---

### Redis

**1. Why is Redis used with Celery?**
It acts as a fast, in-memory broker to queue and store tasks before Celery picks them up.

**2. What data structures does Redis support?**
Strings, lists, sets, sorted sets, hashes, bitmaps, streams. E.g., use hashes for caching user sessions, lists for queues.

**3. What are best practices for Redis memory management?**

* Set key expirations
* Use LRU/LFU policies
* Monitor with `redis-cli INFO`
* Avoid unnecessary persistence

**4. Redis max connections reached. What to do?**
Increase `maxclients` in config, use connection pooling, close idle connections.

**5. Redis evicting keys. How to fix?**

* Increase memory or adjust `maxmemory`
* Use `maxmemory-policy` like `allkeys-lru`
* Move persistent data to a database

---

### Apache Deployment

**1. How do you deploy Django using Apache?**

* Install `mod_wsgi`
* Configure Apache:

```apache
WSGIDaemonProcess myproject python-home=/path/to/venv python-path=/path/to/project
WSGIProcessGroup myproject
WSGIScriptAlias / /path/to/project/project/wsgi.py
<Directory /path/to/project/project>
  <Files wsgi.py>
    Require all granted
  </Files>
</Directory>
```

* Collect static files:

```bash
python manage.py collectstatic
```

* Restart Apache:

```bash
sudo systemctl restart apache2
```

**2. What is the role of `mod_wsgi`?**
It's a WSGI-compliant Apache module to serve Python web apps. It bridges Apache and Django.

**3. Have you configured HTTPS on Apache?**
Yes, using Let's Encrypt with Certbot. Install Certbot, run `certbot --apache`, and renew with cron.

**4. Compare Apache with Nginx for serving a model API.**
Nginx is faster and more lightweight. Apache is more configurable. Nginx is often used as reverse proxy with Gunicorn.

---

### Scenario-Based Interview Questions

**1. Celery tasks not completing. Debug steps?**

* Check worker logs
* Ensure Redis is running
* Validate `CELERY_BROKER_URL`
* Run `celery inspect active`/`registered`

**2. Redis evicting keys. Solutions?**

* Increase `maxmemory`
* Set expirations (`EXPIRE`)
* Use `maxmemory-policy`

**3. Broken deployment from recent commit?**

* Use `git log` to find commit
* `git revert <sha>` or roll back CI/CD pipeline

**4. Architect a system using Git, Celery, Redis, Apache**

* Git for version control + Actions for CI
* Celery + Redis for async jobs
* Apache for serving frontend/API
* PostgreSQL for DB, Flower for monitoring

---
