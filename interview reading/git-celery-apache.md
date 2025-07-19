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
- A thread is a lightweight unit of execution within a program that can run concurrently with other threads. It's like having multiple tasks running simultaneously within the same application.

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


## What you might have meant:
- `git pull` - fetches and merges changes from remote
- `HEAD` - refers to the current commit/branch you're on
- `HEAD@{n}` - refers to previous positions of HEAD (reflog syntax)

## Essential Git Commands for Interviews:

**Basic Operations:**
```bash
git init                    # Initialize a new repository
git clone <url>            # Clone a repository
git add <file>             # Stage changes
git commit -m "message"    # Commit changes
git status                 # Check working directory status
git log                    # View commit history
```

**Branching:**
```bash
git branch                 # List branches
git branch <name>          # Create new branch
git checkout <branch>      # Switch to branch
git checkout -b <branch>   # Create and switch to new branch
git merge <branch>         # Merge branch into current
git branch -d <branch>     # Delete branch
```

**Remote Operations:**
```bash
git remote -v              # List remotes
git fetch                  # Download changes without merging
git pull                   # Fetch and merge from remote
git push                   # Upload changes to remote
git push -u origin <branch> # Push and set upstream
```

**Undoing Changes:**
```bash
git reset --soft HEAD~1    # Undo last commit, keep changes staged
git reset --hard HEAD~1    # Undo last commit, discard changes
git revert <commit>        # Create new commit that undoes changes
git checkout -- <file>     # Discard local changes to file
```

**Advanced:**
```bash
git stash                  # Temporarily save changes
git stash pop              # Apply stashed changes
git rebase <branch>        # Reapply commits on top of another branch
git cherry-pick <commit>   # Apply specific commit to current branch
```

## Renaming Git Branches

**Rename the current branch:**
```bash
git branch -m <new-name>
```

**Rename a different branch (while on another branch):**
```bash
git branch -m <old-name> <new-name>
```

**Complete workflow for renaming a branch that's already pushed:**

1. **Rename the local branch:**
```bash
git branch -m old-branch-name new-branch-name
```

2. **Delete the old branch on remote:**
```bash
git push origin --delete old-branch-name
```

3. **Push the new branch and set upstream:**
```bash
git push -u origin new-branch-name
```

**Alternative one-liner for remote rename:**
```bash
git push origin :old-name new-name
```

**If you're currently on the branch you want to rename:**
```bash
# Step 1: Rename current branch
git branch -m new-branch-name

# Step 2: Push new branch and delete old one
git push origin -u new-branch-name
git push origin --delete old-branch-name
```

**Important notes:**
- `-m` stands for "move" (rename)
- If the new name already exists, use `-M` (force move)
- Always coordinate with your team when renaming shared branches
- Update any pull requests or CI/CD configurations that reference the old branch name


### **What happens to tracking information when you rename a branch?**
Tracking information is lost. You need to re-establish it with `git push -u origin new-branch-name`.

### **How do you rename the default branch (`master` to `main`)?**
```bash
git branch -m master main
git push -u origin main
git push origin --delete master
```
Then update the default branch in your Git hosting service (GitHub/GitLab settings).

### **What if multiple developers are working on the branch you want to rename?**
**Don't do it** unless coordinated. All developers must:
1. Pull latest changes
2. Delete local old branch: `git branch -d old-name`
3. Checkout new branch: `git checkout -b new-name origin/new-name`

Better approach: Create new branch, migrate work, then delete old branch after everyone has switched.

## Git Interview Questions Explained

### 1. **Difference between `git pull` and `git fetch`**

**`git fetch`:**
- Downloads changes from remote repository
- **Does NOT merge** changes into your current branch
- Updates your local references to remote branches
- Safe operation - won't modify your working directory

**`git pull`:**
- Combines `git fetch` + `git merge`
- Downloads changes AND merges them into current branch
- Can cause merge conflicts if there are conflicting changes
- Equivalent to: `git fetch origin` followed by `git merge origin/branch`

```bash
# Fetch only - safe, no changes to working directory
git fetch origin

# Pull - fetches and merges automatically
git pull origin main
```

### 2. **How to undo the last commit**

**Three main approaches:**

**Soft reset (keep changes staged):**
```bash
git reset --soft HEAD~1
# Moves HEAD back one commit, keeps changes in staging area
```

**Mixed reset (keep changes unstaged) - DEFAULT:**
```bash
git reset HEAD~1
# or
git reset --mixed HEAD~1
# Moves HEAD back, unstages changes but keeps them in working directory
```

**Hard reset (discard changes completely):**
```bash
git reset --hard HEAD~1
# WARNING: This permanently deletes changes
```

### 3. **Difference between `git reset` and `git revert`**

**`git reset`:**
- Moves the branch pointer backwards
- Rewrites history (dangerous for shared branches)
- Changes are "undone" by removing commits
- Use for local, unpushed commits

**`git revert`:**
- Creates a NEW commit that undoes changes
- Preserves history (safe for shared branches)
- Changes are "undone" by creating opposite changes
- Use for commits that have been pushed/shared

```bash
# Reset - rewrites history
git reset --hard HEAD~2

# Revert - creates new commit undoing changes
git revert HEAD~2
```

### 4. **How to resolve merge conflicts**

**Step-by-step process:**

1. **Identify conflicts:**
```bash
git status
# Shows files with conflicts
```

2. **Open conflicted files and look for markers:**
```
Incoming changes
```

3. **Resolve conflicts by:**
   - Choosing one version
   - Combining both versions
   - Writing completely new code

4. **Remove conflict markers and save file**

5. **Stage resolved files:**
```bash
git add <resolved-file>
```

6. **Complete the merge:**
```bash
git commit -m "Resolve merge conflict"
```

**Tools to help:**
```bash
git mergetool          # Opens merge tool
git diff               # Shows differences
git log --oneline --graph  # Visualize branches
```

### 5. **Difference between `git merge` and `git rebase`**

**`git merge`:**
- Creates a new "merge commit" 
- Preserves the complete history of both branches
- Results in a branching history graph
- Non-destructive operation

**`git rebase`:**
- Moves commits from one branch to another
- Creates a linear history (no merge commits)
- Rewrites commit history
- Results in cleaner, linear project history

**Visual example:**
```bash
# Before merge/rebase:
A---B---C main
     \
      D---E feature

# After merge:
A---B---C---F main
     \     /
      D---E feature
# F is the merge commit

# After rebase:
A---B---C---D'---E' main
# D' and E' are new commits with same changes but different hashes
```

**Commands:**
```bash
# Merge feature into main
git checkout main
git merge feature

# Rebase feature onto main
git checkout feature
git rebase main
```

**When to use each:**
- **Merge:** When you want to preserve context and history
- **Rebase:** When you want clean, linear history (but never rebase shared/pushed commits)

**Golden rule:** Never rebase commits that have been pushed to shared repositories!

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

## Django Periodic Tasks

### **Scheduling Periodic Tasks in Django**

**Using Celery (most common):**
```python
# settings.py
CELERY_BEAT_SCHEDULE = {
    'send-daily-report': {
        'task': 'myapp.tasks.send_daily_report',
        'schedule': crontab(hour=9, minute=0),  # Daily at 9 AM
    },
    'cleanup-old-files': {
        'task': 'myapp.tasks.cleanup_files',
        'schedule': 30.0,  # Every 30 seconds
    },
}
```

**Alternative options:**
- **Django-cron:** Simple cron-like functionality
- **APScheduler:** Advanced Python scheduler
- **System cron:** Call Django management commands

### **What is a Broker?**

A **message broker** is a middleware that handles communication between your Django app and background workers.

**Purpose:**
- Receives tasks from Django
- Queues tasks for processing
- Delivers tasks to available workers

**Common brokers:**
- **Redis** (most popular)
- **RabbitMQ** (enterprise)
- **Amazon SQS** (cloud)

### **What is a Worker?**

A **worker** is a separate process that executes background tasks.

**Function:**
- Listens to the broker for new tasks
- Executes tasks asynchronously
- Reports results back

**Starting workers:**
```bash
# Celery worker
celery -A myproject worker --loglevel=info

# Celery beat scheduler (for periodic tasks)
celery -A myproject beat --loglevel=info
```

### **Simple Flow:**
1. Django app → sends task → **Broker** (Redis)
2. **Broker** → queues task → **Worker** picks it up
3. **Worker** → executes task → reports back

**Example setup:**
```python
# tasks.py
from celery import shared_task

@shared_task
def send_email_task(email, subject):
    # Background email sending
    send_mail(subject, 'message', 'from@example.com', [email])
```
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

## RabbitMQ Overview

### **What is RabbitMQ?**
RabbitMQ is a **message broker** that implements the Advanced Message Queuing Protocol (AMQP). It acts as an intermediary for messaging between applications.

**Core Features:**
- Message queuing and routing
- High availability and clustering
- Message persistence
- Complex routing patterns
- Management UI

### **RabbitMQ vs Redis**

| Feature | RabbitMQ | Redis |
|---------|----------|--------|
| **Primary Purpose** | Message broker | In-memory data store |
| **Protocol** | AMQP | Redis protocol |
| **Message Persistence** | Built-in, reliable | Optional, less reliable |
| **Routing** | Complex routing (exchanges, bindings) | Simple pub/sub |
| **Performance** | Good for complex workflows | Faster for simple tasks |
| **Memory Usage** | Higher | Lower |
| **Setup Complexity** | More complex | Simpler |
| **Guaranteed Delivery** | Yes | No |
| **Clustering** | Built-in | Redis Cluster |

### **When to Use Each**

**Use RabbitMQ when:**
- Need guaranteed message delivery
- Complex routing requirements
- Message persistence is critical
- Enterprise-grade reliability needed
- Multiple consumers with different routing needs

**Use Redis when:**
- Simple task queuing
- High performance requirements
- Already using Redis for caching
- Simpler setup preferred
- Cost-effective solution

### **Configuration Examples**

**RabbitMQ Setup:**
```python
# settings.py
CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672//'
CELERY_RESULT_BACKEND = 'rpc://'

# More robust config
CELERY_BROKER_URL = 'amqp://user:pass@localhost:5672/vhost'
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_TASK_REJECT_ON_WORKER_LOST = True
```

**Redis Setup:**
```python
# settings.py
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
```

### **Starting Services**

**RabbitMQ:**
```bash
# Install and start
sudo apt-get install rabbitmq-server
sudo systemctl start rabbitmq-server

# Enable management plugin
sudo rabbitmq-plugins enable rabbitmq_management
# Access UI at http://localhost:15672
```

**Redis:**
```bash
# Install and start
sudo apt-get install redis-server
redis-server

# Or with Docker
docker run -d -p 6379:6379 redis:alpine
```

### **Performance Comparison**

**RabbitMQ:**
- ~20K-50K messages/second
- Better for complex workflows
- Higher memory footprint

**Redis:**
- ~100K+ messages/second
- Better for simple queuing
- Lower memory usage

### **Bottom Line**
- **Redis**: Fast, simple, good for most Django projects
- **RabbitMQ**: Robust, enterprise-grade, better for complex messaging needs

For most Django applications, **Redis is sufficient** and easier to set up. Use RabbitMQ only when you need its advanced features.