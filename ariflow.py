# DAG File Example (etl_pipeline.py)
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.transfers.s3_to_redshift import S3ToRedshiftOperator
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor
from airflow.models.connection import Connection
from airflow.models import Variable



# DAG File: Python script defining workflow structure
# Scheduler: Would pick up this DAG and schedule it to run daily at 1 AM
# Executor: Would execute these tasks based on the configured executor
# Web Server: Would display this DAG's structure and execution status
# Sensors: S3KeySensor waits for file availability
# XCom: Used to pass data between tasks (validation result)
# Providers: AWS provider for S3 and Redshift operations
# Connections: Referenced via aws_conn_id and redshift_conn_id
# Variables: Could be used within tasks (though not explicitly shown)

# Default arguments used by the DAG
default_args = {
    'owner': 'data_team',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email': ['alerts@example.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

# DAG definition
dag = DAG(
    'etl_s3_to_redshift',
    default_args=default_args,
    description='ETL pipeline from S3 to Redshift',
    schedule_interval='0 1 * * *',  # Run at 1:00 AM daily
    catchup=False
)

# Task 1: Sensor to check if data file exists in S3
check_s3_file = S3KeySensor(
    task_id='check_s3_file',
    bucket_key='data/{{ds}}/sales_data.csv',  # Dynamic path with execution date
    bucket_name='my-company-data',
    aws_conn_id='aws_default',
    timeout=60*60,  # 1 hour timeout
    poke_interval=300,  # Check every 5 minutes
    dag=dag
)

# Task 2: Python function to validate data quality
def validate_data(**context):
    # Get the XCom value - file path that was checked by the sensor
    file_path = context['task_instance'].xcom_pull(task_ids='check_s3_file')
    print(f"Validating data from {file_path}")
    
    # Perform validation logic
    # ...
    
    # Push validation result to XCom
    context['task_instance'].xcom_push(key='validation_passed', value=True)
    return "Data validation complete"

validate_data_task = PythonOperator(
    task_id='validate_data',
    python_callable=validate_data,
    provide_context=True,
    dag=dag
)

# Task 3: Load data from S3 to Redshift (Redshift is Amazon's fully managed, petabyte-scale data warehouse service in the cloud. )
load_to_redshift = S3ToRedshiftOperator(
    task_id='load_to_redshift',
    schema='public',
    table='sales',
    s3_bucket='my-company-data',
    s3_key='data/{{ds}}/sales_data.csv',
    copy_options=['CSV', 'IGNOREHEADER 1'],
    redshift_conn_id='redshift_default',
    aws_conn_id='aws_default',
    dag=dag
)

# Set task dependencies
check_s3_file >> validate_data_task >> load_to_redshift


# The DAG creates a simple ETL pipeline that checks for data in S3, validates it, and loads it into Redshift.