1. What is astronomer?
- Astro is a data integration platform that allows you to connect to various data sources and load data into a data warehouse like Snowflake. 
2. What is a data warehouse?
- A data warehouse is a system for storing and managing data from various sources.
3. What is a data lake?
- A data lake is a system for storing and managing data from various sources.
4. What is a data pipeline?
- A data pipeline is a process of extracting data from a source, transforming it, and loading it into a target.
5. What is workflow?
- A workflow is a collection of tasks that are executed in a specific order.(since we need to load data regularly, we need to create a workflow)
6. What is airflow?
- Airflow is a platform to manage workflows by running, scheduling, and monitoring workflows.
7. What is the difference between airflow and astro?
- Airflow is a platform to programmatically author, schedule, and monitor workflows. Astro is a data integration platform that allows you to connect to various data sources and load data into a data warehouse like Snowflake.
- Astro cloud is sued to deploy
8. What is ETL Pipeline?

1. **Extract** *-Pull data from sources: databases, APIs, files (CSV, JSON), etc.
* Tools: Python scripts, Airflow, Talend, etc.

2. **Transform** - Clean, validate, and reshape data:

  * Remove nulls/duplicates
  * Convert data types
  * Aggregate or join datasets
* Tools: Pandas, Spark, dbt

3. **Load** - Store processed data into a destination:

  * Data warehouse (e.g. Snowflake, BigQuery)
  * Relational DB (e.g. PostgreSQL, MySQL)
  * Cloud storage (e.g. S3)


Let me know if you want a diagram, orchestration tools, or how this integrates with NLP or ML workflows.

9. Lifecycle of a data scince project
      1. **Problem Definition**: Define business objectives, success metrics, and scope.
      2. **Data Collection**: Gather data from relevant sources.
      3. **Data Cleaning**: Handle missing values, outliers, and inconsistencies.
      4. **Exploratory Analysis**: Visualize data to understand patterns and relationships.
      5. **Feature Engineering**: Create, transform, and select relevant features.
      6. **Model Development**: Select algorithms, train models, and tune hyperparameters.
      7. **Model Evaluation**: Assess performance against business objectives.
      8. **Deployment**: Implement the model in production environment.
      9. **Monitoring**: Track performance and retrain as needed.
      10. **Communication**: Present findings and impact to stakeholders.

Note: This process is iterative rather than strictly sequential.


                (Writes down all the 
                requirements and divide them 
                into smaller tasks/sprints(PO) 
                the sent to DA/DS team)            (identify data they may need to consider to 
                                                    solve  a problem. Might be in the db,   (provides suggestion to DA/DS Team 
                                                                                            depending on where data is found. Identifies the right kind of data to use)
                                                    cloud or 3rd party apis/IOT)
Data science project -> Requirements Gathering -> Data analyst/scientist <-> _Discussion_ (maybe in the..)-> Domain expertise/product owner -> Model Training -> Model Evaluation -> Model Deployment -> Model Monitoring
                            ^          ^                                       |       |
                            |          |                                       |       |
                            |          |                                       |      |
            Domain expertise/         Business Analyst                         DB      Cloud or 3rd party APIS/IOT
            product owner                                                      |       |
                                                                               |       |
                                                                               |       |
                                                                               |       |
                                                                               |       |
                                                           data pipelines                Big data engineering (creates data pipeline to load data from source to target using ETL Pipeline)


10. What is a DAG?
- A DAG is a Directed Acyclic Graph that represents a workflow.
Node        direction
API->Data    ->         Transformations   ->   Data->Postgres
Task 1               Task 2               Task 3

 - A task is a single unit of work in a workflow.
12. What is a operator?
- An operator is a component that is used to create a task.

How to run airflow and astro + project setup

13. **What are the core components of Airflow architecture?**
   - **Web Server**: Flask-based UI for DAG visualization/management (port 8080)
   - **Scheduler**: Monitors DAGs, schedules tasks based on dependencies
   - **Executor**: Determines task execution method (Local, Celery, Kubernetes)
   - **Metadata Database**: Stores workflow state (PostgreSQL, MySQL, SQLite)
   - **DAG Files**: Python files defining workflow structure
   - **Workers**: Execute tasks on separate machines in distributed setups
   - **Queue**: Enables scheduler-worker communication (Redis, RabbitMQ)
   - **XCom**: Facilitates inter-task data exchange
   - **Providers**: Connects to external services (AWS, GCP, databases)

14. **Explain the concept of Executors in Airflow.**
   - Executors are components that run tasks. Different executor types include:
     - SequentialExecutor: Default executor, runs one task at a time (not for production)
     - LocalExecutor: Runs tasks in parallel on single machine using processes - executing multiple tasks simultaneously rather than one after another
     - CeleryExecutor: Distributes tasks across multiple worker nodes using Celery
     - KubernetesExecutor: Dynamically creates a pod for each task instance

15. **What is XComs in Airflow?**
   - XComs (Cross-Communications) allow tasks to exchange small amounts of data. Tasks can push and pull XComs to share information between them.


16. **How would you handle dependencies between tasks in a DAG?**
   - Using upstream and downstream operators: `task1 >> task2 >> task3`
   - Using set_upstream and set_downstream methods: `task3.set_upstream(task2)`
   - Using lists: `[task1, task2] >> task3` or `task1 >> [task2, task3]`


17. **What are Sensors in Airflow?**
   - Sensors are a type of operator that wait for a certain condition to be true before succeeding and allowing the workflow to continue.

## Intermediate Airflow Questions

18. **Explain task retries and how to configure them.**
   - Tasks can be configured to retry using `retries` parameter, with `retry_delay` to set time between retries.
   - Example: `task = PythonOperator(task_id='my_task', python_callable=my_function, retries=3, retry_delay=timedelta(minutes=5))`

19. **What are the different types of sensors in Airflow?**
   - FileSensor: Waits for a file to land in a specified location
   - ExternalTaskSensor: Waits for a task in another DAG to complete
   - SqlSensor: Waits for a SQL query to return results
   - S3KeySensor: Waits for a key (file) to appear in an S3 bucket
   - HttpSensor: Waits for an HTTP endpoint to respond with a 200 status code

20. **How do you implement branching in Airflow?**
   - Using the BranchPythonOperator, which returns the task_id of the next task to execute based on certain conditions.

21. **What is a SubDAG and when would you use it?**
   - SubDAGs are DAGs embedded within another DAG. They can be used to group related tasks and reuse common patterns. However, they often lead to deadlocks and aren't recommended in current Airflow versions.

22. **What are Task Groups and how do they differ from SubDAGs?**
   - Task Groups are a way to organize tasks in the UI without affecting the actual task execution. Unlike SubDAGs, they don't have scheduling or execution implications and are the recommended approach for grouping tasks.

## Advanced Airflow Questions

23. **How would you handle a situation where a DAG has hundreds of tasks?**
   - Use Task Groups to organize tasks visually
   - Consider using dynamic task generation
   - Review if the DAG can be split into multiple DAGs
   - Monitor performance and consider using a more powerful executor

24. **Explain Airflow's Pool concept and when you would use it.**
   - Pools are a way to limit parallelism for a group of tasks. They're useful when multiple tasks need to access a limited resource (like a database with connection limits).

25. **What are Smart Sensors in Airflow?**
   - Smart Sensors are a feature that allows multiple sensor instances to be executed in a single process, reducing resource consumption when many sensors are running.

26. **How do you implement dynamic DAG generation in Airflow?**
   - Using Python code within the DAG file to dynamically generate tasks based on configurations, database queries, or file contents.

27. **What is the Airflow Scheduler's mechanism for determining when to run tasks?**
   - The scheduler continuously checks for DAGs to schedule, looks at next execution date, creates DagRuns, examines task dependencies, and queues tasks that are ready to be executed.

## Airflow Deployment and Operations

28. **What are the challenges with scaling Airflow in production?**
   - Database connection limits and performance
   - Worker resource utilization
   - Scheduler performance with many DAGs/tasks
   - Monitoring and alerting setup
   - High availability configuration

29. **How would you monitor Airflow in production?**
   - Using Airflow's built-in metrics with StatsD/Prometheus
   - Setting up alerts for failed tasks and SLA misses
   - Monitoring database health and connection pools
   - Log aggregation and analysis

30. **What is the difference between schedule_interval and execution_date in Airflow?**
   - schedule_interval: Defines how often a DAG runs
   - execution_date: The logical date/time for which a DAG Run is executed (typically represents the start of the period the data belongs to)

31. **How would you approach testing DAGs and operators?**
   - Using Airflow's testing utilities like dag_test_utils
   - Creating unit tests for custom operators and hooks
   - Setting up end-to-end tests with a test database
   - Using dag.test() method in development

32. **Explain strategies for handling large files in Airflow.**
   - Avoid storing large files in XComs
   - Use external storage like S3 or HDFS
   - Consider streaming data instead of loading entirely into memory
   - Use appropriate operators like S3FileTransformOperator or GCSToGCSOperator

## Airflow Integration with Data Ecosystem

33. **How would you integrate Airflow with a data catalog or metadata management system?**
   - Using hooks to connect to metadata APIs
   - Pushing metadata as part of DAG execution
   - Creating a custom operator for metadata integration
   - Implementing lineage tracking through custom callbacks

34. **What approaches exist for implementing data quality checks in Airflow?**
   - Using SQLOperators to run validation queries
   - Integrating with tools like Great Expectations
   - Implementing custom Python functions for validation
   - Using sensors to check for expected outcomes

35. **How would you handle secrets and credentials in Airflow?**
   - Using Airflow's Connections and Variables features
   - Integrating with external secret managers like HashiCorp Vault
   - Using environment variables with appropriate encryption
   - Implementing custom backend for secrets

36. **Explain how you would orchestrate dbt models using Airflow.**
   - Using the DbtOperator from an Airflow provider package
   - Creating a custom operator to execute dbt commands
   - Implementing a BashOperator that runs dbt CLI commands
   - Using a PythonOperator that uses the dbt Python API

37. **How would you handle incremental data processing in Airflow?**
   - Using execution_date to determine processing windows
   - Storing and retrieving watermarks using XComs or Variables
   - Implementing idempotent tasks
   - Using templated queries with time-based parameters
