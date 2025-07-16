# Apache Superset Comprehensive Course

## Course Overview
This comprehensive course will transform you from a Superset beginner to an advanced practitioner capable of building enterprise-grade dashboards and managing Superset deployments. You'll work through real-world scenarios, complete hands-on projects, and learn industry best practices.

**Duration:** 12-15 hours  
**Prerequisites:** Basic SQL knowledge, familiarity with data concepts, basic command line usage  
**Learning Outcomes:** Design, build, deploy, and maintain production-ready Superset dashboards and infrastructure


## Module 1: Introduction to Apache Superset (60 minutes)

### What is Apache Superset?
Apache Superset is an enterprise-grade business intelligence web application that democratizes data visualization across organizations. Born at Airbnb in 2015 and donated to the Apache Software Foundation, it's now used by thousands of companies worldwide.

- Superset is a modern data exploration and data visualization platform.

### The Business Case for Superset
**Why Organizations Choose Superset:**
- **A no-code interface** for building charts quickly  
- **A powerful, web-based SQL Editor** for advanced querying  
- **A lightweight semantic layer** for quickly defining custom dimensions and metrics  
- **Out-of-the-box support** for nearly any SQL database(PostgreSQL, MySQL, Maria DB, Oracle) or data engine  
- **A wide array of beautiful visualizations** to showcase your data, ranging from simple bar charts to geospatial visualizations  
- **Lightweight, configurable caching layer** to help ease database load  
- **Highly extensible security roles** and authentication options  
- **An API** for programmatic customization  
- **A cloud-native architecture** designed from the ground up for scale  


### Core Capabilities Deep Dive

#### 1. Rich Visualization Library
**40+ Chart Types Including:**
- **Statistical Charts**: Box plots, violin plots, histograms
- **Time Series**: Advanced time series with annotations
- **Geographic**: Choropleth maps, scatter plots on maps
- **Relationship Charts**: Network graphs, chord diagrams
- **Business Charts**: Funnel charts, gauge charts, KPI cards

#### 2. SQL Lab - The Data Explorer
**Advanced Features:**
- **Query History**: Full audit trail of all queries
- **Query Scheduling**: Cron-like scheduling for data refreshes
- **Result Caching**: Multi-level caching for performance
- **CSV Export**: Query results to CSV for further analysis
- **Query Sharing**: Collaborative query development

#### 3. Dashboard Builder
**Enterprise Features:**
- **Responsive Design**: Mobile-first dashboard layouts
- **Real-time Updates**: Live data streaming capabilities
- **Cross-Filtering**: Interactive dashboard elements
- **Embedded Analytics**: White-label dashboard embedding
- **Version Control**: Dashboard change tracking


Steps taken when building dashbaords and what to consider



### Architecture Deep Dive

#### System Components
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Load Balancer │    │   Web Server    │    │   Cache Layer   │
│   (nginx/HAProxy)│───▶│   (Flask/Gunicorn)│───▶│   (Redis)       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │  Metadata DB    │
                       │ (PostgreSQL)    │
                       └─────────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │   Data Sources  │
                       │ (Your Databases)│
                       └─────────────────┘
```

#### Scalability Patterns
- **Horizontal Scaling**: Multiple web server instances
- **Database Sharding**: Distribute metadata across databases
- **Caching Strategy**: Redis cluster for high availability
- **Async Processing**: Celery for background tasks

### Competitive Analysis

| Feature | Superset | Tableau | Power BI | Looker |
|---------|----------|---------|----------|---------|
| **Cost** | Free | $70/user/month | $10/user/month | $30/user/month |
| **Customization** | High | Medium | Low | Medium |
| **SQL Support** | Native | Limited | Good | Excellent |
| **Embedding** | Free | $$ | $$ | $$$ |
| **Open Source** | Yes | No | No | No |



## Module 2: Installation and Environment Setup (90 minutes)

### Development Environment Setup

#### Option 1: Docker Development Environment (Recommended)
```bash
# Create project directory
mkdir superset-learning
cd superset-learning

# Clone repository
git clone https://github.com/apache/superset.git
cd superset

# Create environment file
cat > .env << EOF
SUPERSET_ENV=development
SUPERSET_LOAD_EXAMPLES=yes
CYPRESS_CONFIG=false
SUPERSET_PORT=8088
SUPERSET_SECRET_KEY=$(python -c "import secrets; print(secrets.token_urlsafe(42))")
EOF

# Start development environment
docker-compose -f docker-compose-non-dev.yml up -d

# Monitor startup
docker-compose -f docker-compose-non-dev.yml logs -f superset_app
```

#### Option 2: Python Virtual Environment
```bash
# System prerequisites (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install -y python3-pip python3-venv python3-dev \
    gcc g++ libffi-dev libssl-dev libsasl2-dev libldap2-dev

# Create and activate virtual environment
python3 -m venv superset_env
source superset_env/bin/activate

# Upgrade pip and install build tools
pip install --upgrade pip setuptools wheel

# Install Superset
pip install apache-superset[postgres,mysql,redis]

# Environment configuration
export SUPERSET_CONFIG_PATH=/path/to/your/superset_config.py
export SUPERSET_SECRET_KEY='your-secret-key-here'

# Initialize database
superset db upgrade

# Create admin user
superset fab create-admin --username admin --firstname Admin \
    --lastname User --email admin@example.com --password admin

# Load example data
superset load_examples

# Initialize
superset init

# Start development server
superset run -p 8088 --with-threads --reload --debugger
```

### Production Environment Setup

#### Kubernetes Deployment
```yaml
# superset-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: superset
spec:
  replicas: 3
  selector:
    matchLabels:
      app: superset
  template:
    metadata:
      labels:
        app: superset
    spec:
      containers:
      - name: superset
        image: apache/superset:latest
        ports:
        - containerPort: 8088
        env:
        - name: SUPERSET_CONFIG_PATH
          value: "/app/pythonpath/superset_config.py"
        - name: SUPERSET_SECRET_KEY
          valueFrom:
            secretKeyRef:
              name: superset-secret
              key: secret-key
        volumeMounts:
        - name: config
          mountPath: /app/pythonpath
        resources:
          requests:
            memory: "1Gi"
            cpu: "500m"
          limits:
            memory: "2Gi"
            cpu: "1000m"
      volumes:
      - name: config
        configMap:
          name: superset-config
```

#### Production Configuration File
```python
# superset_config.py
import os
from datetime import timedelta

# Database Configuration
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

# Redis Configuration
REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.environ.get('REDIS_PORT', 6379))
REDIS_DB = int(os.environ.get('REDIS_DB', 0))

# Cache Configuration
CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_KEY_PREFIX': 'superset_',
    'CACHE_REDIS_HOST': REDIS_HOST,
    'CACHE_REDIS_PORT': REDIS_PORT,
    'CACHE_REDIS_DB': REDIS_DB,
}

# Security Configuration
WTF_CSRF_ENABLED = True
SECRET_KEY = os.environ.get('SUPERSET_SECRET_KEY')

# Feature Flags
FEATURE_FLAGS = {
    'ENABLE_TEMPLATE_PROCESSING': True,
    'DASHBOARD_NATIVE_FILTERS': True,
    'GLOBAL_ASYNC_QUERIES': True,
    'VERSIONED_EXPORT': True,
}

# Query Configuration
SQL_MAX_ROW = 100000
SUPERSET_CELERY_TIMEOUT = 300
SUPERSET_WEBSERVER_TIMEOUT = 300

# Email Configuration
EMAIL_NOTIFICATIONS = True
SMTP_HOST = os.environ.get('SMTP_HOST')
SMTP_PORT = int(os.environ.get('SMTP_PORT', 587))
SMTP_USER = os.environ.get('SMTP_USER')
SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD')
SMTP_MAIL_FROM = os.environ.get('SMTP_MAIL_FROM')

# Logging Configuration
ENABLE_TIME_ROTATE = True
TIME_ROTATE_LOG_LEVEL = 'INFO'
FILENAME = os.path.join(DATA_DIR, 'superset.log')
ROLLOVER = 'midnight'
INTERVAL = 1
BACKUP_COUNT = 30

# Custom CSS
CUSTOM_CSS = """
.navbar-brand {
    background-image: url('/static/assets/images/your-logo.png');
}
"""
```

### Environment Verification

#### Health Check Script
```python
# health_check.py
import requests
import sys
import time

def check_superset_health():
    """Comprehensive health check for Superset instance"""
    base_url = "http://localhost:8088"
    
    checks = [
        ("Main page", f"{base_url}/health"),
        ("API health", f"{base_url}/api/v1/health"),
        ("Database connectivity", f"{base_url}/api/v1/database/"),
    ]
    
    for name, url in checks:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                print(f"✓ {name}: OK")
            else:
                print(f"✗ {name}: Failed ({response.status_code})")
                return False
        except Exception as e:
            print(f"✗ {name}: Error - {str(e)}")
            return False
    
    return True

if __name__ == "__main__":
    if check_superset_health():
        print("\n🎉 Superset is healthy and ready!")
        sys.exit(0)
    else:
        print("\n❌ Superset health check failed!")
        sys.exit(1)
```

### Hands-On Exercise: Environment Setup

**Task**: Set up a complete development environment and verify functionality.

1. **Choose Installation Method**: Docker or Python virtual environment
2. **Configure Environment**: Set up configuration files
3. **Verify Installation**: Run health checks
4. **Load Sample Data**: Import example datasets
5. **Basic Navigation**: Explore the interface

**Expected Outcomes**:
- Superset running on localhost:8088
- Admin access working
- Sample dashboards visible
- Database connections established

---

## Module 3: Data Source Management (120 minutes)

### Understanding Data Source Architecture

#### Database Support Matrix
```
┌─────────────────┬─────────────┬─────────────┬─────────────┐
│ Database Type   │ Read Support│ Write Support│ Performance │
├─────────────────┼─────────────┼─────────────┼─────────────┤
│ PostgreSQL      │ Excellent   │ No          │ Excellent   │
│ MySQL/MariaDB   │ Excellent   │ No          │ Good        │
│ SQLite          │ Good        │ No          │ Limited     │
│ Oracle          │ Good        │ No          │ Good        │
│ SQL Server      │ Good        │ No          │ Good        │
│ Snowflake       │ Excellent   │ No          │ Excellent   │
│ BigQuery        │ Excellent   │ No          │ Excellent   │
│ Redshift        │ Good        │ No          │ Good        │
│ Spark SQL       │ Good        │ No          │ Variable    │
│ Presto/Trino    │ Excellent   │ No          │ Excellent   │
└─────────────────┴─────────────┴─────────────┴─────────────┘
```

### Database Connection Deep Dive

#### PostgreSQL Configuration
```python
# Connection string format
postgresql://username:password@host:port/database

# Advanced connection with SSL
postgresql://user:pass@host:port/db?sslmode=require&sslcert=client-cert.pem&sslkey=client-key.pem

# Connection pooling configuration
SQLALCHEMY_ENGINE_OPTIONS = {
    'pool_pre_ping': True,
    'pool_recycle': 3600,
    'pool_size': 10,
    'max_overflow': 20,
}
```

#### Connection String Examples
```bash
# MySQL
mysql://username:password@localhost:3306/database_name

# SQL Server
mssql+pyodbc://username:password@host:port/database?driver=ODBC+Driver+17+for+SQL+Server

# Snowflake
snowflake://username:password@account.region.snowflakecomputing.com/database/schema?warehouse=warehouse_name&role=role_name

# BigQuery
bigquery://project_id/dataset_id

# Redshift
redshift+psycopg2://username:password@host:port/database

# Spark SQL
spark://username:password@host:port/database
```

### Advanced Database Setup

#### Setting Up Sample E-commerce Database
```sql
-- Create sample e-commerce database
CREATE DATABASE ecommerce_analytics;
USE ecommerce_analytics;

-- Customers table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    registration_date DATE,
    country VARCHAR(50),
    city VARCHAR(50),
    age_group VARCHAR(20),
    customer_segment VARCHAR(20)
);

-- Products table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(200),
    category VARCHAR(50),
    subcategory VARCHAR(50),
    brand VARCHAR(50),
    price DECIMAL(10,2),
    cost DECIMAL(10,2),
    launch_date DATE,
    discontinued BOOLEAN DEFAULT FALSE
);

-- Orders table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    shipping_date DATE,
    total_amount DECIMAL(10,2),
    shipping_cost DECIMAL(10,2),
    discount_amount DECIMAL(10,2),
    payment_method VARCHAR(50),
    order_status VARCHAR(20),
    sales_channel VARCHAR(50),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Order items table
CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    unit_price DECIMAL(10,2),
    total_price DECIMAL(10,2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Website analytics table
CREATE TABLE website_analytics (
    session_id VARCHAR(50) PRIMARY KEY,
    customer_id INT,
    session_date DATE,
    page_views INT,
    session_duration_minutes INT,
    bounce_rate DECIMAL(5,2),
    conversion_rate DECIMAL(5,2),
    traffic_source VARCHAR(50),
    device_type VARCHAR(20),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Inventory table
CREATE TABLE inventory (
    product_id INT,
    warehouse_location VARCHAR(50),
    stock_quantity INT,
    reorder_point INT,
    last_updated TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
```

#### Data Population Script
```python
# populate_sample_data.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_sample_data():
    """Generate realistic e-commerce sample data"""
    
    # Generate customers
    customers = []
    for i in range(1, 10001):
        customers.append({
            'customer_id': i,
            'first_name': f'Customer_{i}',
            'last_name': f'LastName_{i}',
            'email': f'customer{i}@example.com',
            'registration_date': datetime.now() - timedelta(days=random.randint(1, 1095)),
            'country': random.choice(['USA', 'Canada', 'UK', 'Germany', 'France', 'Australia']),
            'city': random.choice(['New York', 'Toronto', 'London', 'Berlin', 'Paris', 'Sydney']),
            'age_group': random.choice(['18-25', '26-35', '36-45', '46-55', '56+']),
            'customer_segment': random.choice(['Premium', 'Standard', 'Basic'])
        })
    
    # Generate products
    categories = ['Electronics', 'Clothing', 'Home', 'Books', 'Sports', 'Beauty']
    products = []
    for i in range(1, 1001):
        category = random.choice(categories)
        products.append({
            'product_id': i,
            'product_name': f'Product_{category}_{i}',
            'category': category,
            'subcategory': f'Sub_{category}_{i%10}',
            'brand': f'Brand_{i%50}',
            'price': round(random.uniform(10, 1000), 2),
            'cost': round(random.uniform(5, 500), 2),
            'launch_date': datetime.now() - timedelta(days=random.randint(1, 365)),
            'discontinued': random.choice([True, False])
        })
    
    # Generate orders and order items
    orders = []
    order_items = []
    order_id = 1
    
    for customer_id in range(1, 10001):
        num_orders = random.randint(0, 10)
        for _ in range(num_orders):
            order_date = datetime.now() - timedelta(days=random.randint(1, 365))
            shipping_date = order_date + timedelta(days=random.randint(1, 7))
            
            order = {
                'order_id': order_id,
                'customer_id': customer_id,
                'order_date': order_date,
                'shipping_date': shipping_date,
                'total_amount': 0,  # Will calculate later
                'shipping_cost': round(random.uniform(0, 25), 2),
                'discount_amount': round(random.uniform(0, 50), 2),
                'payment_method': random.choice(['Credit Card', 'PayPal', 'Bank Transfer']),
                'order_status': random.choice(['Completed', 'Processing', 'Shipped', 'Cancelled']),
                'sales_channel': random.choice(['Online', 'Mobile App', 'Phone', 'In-Store'])
            }
            
            # Generate order items
            num_items = random.randint(1, 5)
            total_amount = 0
            for item_id in range(1, num_items + 1):
                product_id = random.randint(1, 1000)
                quantity = random.randint(1, 3)
                unit_price = round(random.uniform(10, 1000), 2)
                total_price = quantity * unit_price
                total_amount += total_price
                
                order_items.append({
                    'order_item_id': (order_id * 100) + item_id,
                    'order_id': order_id,
                    'product_id': product_id,
                    'quantity': quantity,
                    'unit_price': unit_price,
                    'total_price': total_price
                })
            
            order['total_amount'] = total_amount
            orders.append(order)
            order_id += 1
    
    return customers, products, orders, order_items

# Convert to DataFrames and save
customers, products, orders, order_items = generate_sample_data()

pd.DataFrame(customers).to_csv('customers.csv', index=False)
pd.DataFrame(products).to_csv('products.csv', index=False)
pd.DataFrame(orders).to_csv('orders.csv', index=False)
pd.DataFrame(order_items).to_csv('order_items.csv', index=False)

print("Sample data generated successfully!")
```

### Data Source Security and Optimization

#### Security Best Practices
```python
# Database user with minimal permissions
CREATE USER 'superset_readonly'@'%' IDENTIFIED BY 'secure_password';
GRANT SELECT ON ecommerce_analytics.* TO 'superset_readonly'@'%';
FLUSH PRIVILEGES;

# Connection with SSL
SQLALCHEMY_DATABASE_URI = 'mysql://superset_readonly:secure_password@host:3306/ecommerce_analytics?ssl_ca=/path/to/ca.pem&ssl_cert=/path/to/client-cert.pem&ssl_key=/path/to/client-key.pem'
```

#### Query Optimization
```sql
-- Create indexes for common query patterns
CREATE INDEX idx_orders_date ON orders(order_date);
CREATE INDEX idx_orders_customer ON orders(customer_id);
CREATE INDEX idx_order_items_order ON order_items(order_id);
CREATE INDEX idx_order_items_product ON order_items(product_id);
CREATE INDEX idx_customers_segment ON customers(customer_segment);
CREATE INDEX idx_products_category ON products(category);

-- Create materialized views for common aggregations
CREATE MATERIALIZED VIEW daily_sales AS
SELECT 
    DATE(order_date) as sale_date,
    COUNT(*) as order_count,
    SUM(total_amount) as total_sales,
    AVG(total_amount) as avg_order_value
FROM orders 
WHERE order_status = 'Completed'
GROUP BY DATE(order_date);

-- Refresh materialized view procedure
DELIMITER //
CREATE PROCEDURE refresh_daily_sales()
BEGIN
    DROP MATERIALIZED VIEW IF EXISTS daily_sales;
    CREATE MATERIALIZED VIEW daily_sales AS
    SELECT 
        DATE(order_date) as sale_date,
        COUNT(*) as order_count,
        SUM(total_amount) as total_sales,
        AVG(total_amount) as avg_order_value
    FROM orders 
    WHERE order_status = 'Completed'
    GROUP BY DATE(order_date);
END //
DELIMITER ;
```

### Hands-On Exercise: Multi-Database Setup

**Task**: Configure multiple data sources and create a unified analytics environment.

#### Step 1: Primary Database Setup
1. Create PostgreSQL database with sales data
2. Configure connection in Superset
3. Test connectivity and basic queries

#### Step 2: Secondary Database Setup
1. Create MySQL database with customer data
2. Configure connection in Superset
3. Set up cross-database queries

#### Step 3: Data Validation
```sql
-- Validate data quality
SELECT 
    'customers' as table_name,
    COUNT(*) as record_count,
    COUNT(DISTINCT customer_id) as unique_customers,
    MIN(registration_date) as earliest_date,
    MAX(registration_date) as latest_date
FROM customers
UNION ALL
SELECT 
    'orders' as table_name,
    COUNT(*) as record_count,
    COUNT(DISTINCT order_id) as unique_orders,
    MIN(order_date) as earliest_date,
    MAX(order_date) as latest_date
FROM orders;
```

**Expected Outcomes**:
- Multiple databases connected
- Data quality validated
- Cross-database queries working
- Indexes created for performance

---

## Module 4: SQL Lab Mastery (150 minutes)

### Advanced SQL Lab Features

#### Interface Deep Dive
```
┌─────────────────────────────────────────────────────────────────┐
│ SQL Lab Interface Components                                    │
├─────────────────────────────────────────────────────────────────┤
│ 1. Database/Schema Browser (Left Panel)                        │
│    - Hierarchical table structure                              │
│    - Column metadata and types                                 │
│    - Quick table preview                                       │
│                                                                 │
│ 2. Query Editor (Center Panel)                                 │
│    - Syntax highlighting                                       │
│    - Auto-completion                                           │
│    - Multiple tabs                                             │
│    - Query templates                                           │
│                                                                 │
│ 3. Results Panel (Bottom)                                      │
│    - Tabular results                                           │
│    - Query statistics                                          │
│    - Export options                                            │
│    - Visualization preview                                     │
│                                                                 │
│ 4. Query History (Right Panel)                                 │
│    - All previous queries                                      │
│    - Query performance metrics                                 │
│    - Share/clone functionality                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Advanced Query Techniques

#### 1. Window Functions for Analytics
```sql
-- Customer lifetime value analysis
WITH customer_metrics AS (
    SELECT 
        c.customer_id,
        c.customer_segment,
        c.registration_date,
        COUNT(o.order_id) as total_orders,
        SUM(o.total_amount) as lifetime_value,
        AVG(o.total_amount) as avg_order_value,
        MAX(o.order_date) as last_order_date,
        MIN(o.order_date) as first_order_date
    FROM customers c
    LEFT JOIN orders o ON c.customer_id = o.customer_id
    WHERE o.order_status = 'Completed'
    GROUP BY c.customer_id, c.customer_segment, c.registration_date
),
customer_rankings AS (
    SELECT 
        *,
        ROW_NUMBER() OVER (PARTITION BY customer_segment ORDER BY lifetime_value DESC) as segment_rank,
        PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY lifetime_value) OVER (PARTITION BY customer_segment) as segment_median_ltv,
        lifetime_value - LAG(lifetime_value) OVER (PARTITION BY customer_segment ORDER BY lifetime_value) as ltv_diff_from_previous
    FROM customer_metrics
)
SELECT 
    customer_segment,
    segment_rank,
    customer_id,
    lifetime_value,
    segment_median_ltv,
    CASE 
        WHEN lifetime_value > segment_median_ltv * 1.5 THEN 'High Value'
        WHEN lifetime_value > segment_median_ltv * 0.8 THEN 'Medium Value'
        ELSE 'Low Value'
    END as value_tier,
    total_orders,
    avg_order_value,
    EXTRACT(DAYS FROM (last_order_date - first_order_date)) as customer_lifespan_days
FROM customer_rankings
WHERE segment_rank <= 100
ORDER BY customer_segment, segment_rank;
```

#### 2. Cohort Analysis
```sql
-- Monthly cohort analysis
WITH monthly_cohorts AS (
    SELECT 
        customer_id,
        DATE_TRUNC('month', MIN(order_date)) as cohort_month,
        DATE_TRUNC('month', order_date) as order_month
    FROM orders
    WHERE order_status = 'Completed'
    GROUP BY customer_id, DATE_TRUNC('month', order_date)
),
cohort_sizes AS (
    SELECT 
        cohort_month,
        COUNT(DISTINCT customer_id) as cohort_size
    FROM monthly_cohorts
    GROUP BY cohort_month
),
cohort_retention AS (
    SELECT 
        mc.cohort_month,
        mc.order_month,
        COUNT(DISTINCT mc.customer_id) as active_customers,
        EXTRACT(MONTH FROM AGE(mc.order_month, mc.cohort_month)) as month_number
    FROM monthly_cohorts mc
    GROUP BY mc.cohort_month, mc.order_month
)
SELECT 
    cr.cohort_month,
    cr.month_number,
    cr.active_customers,
    cs.cohort_size,
    ROUND(100.0 * cr.active_customers / cs.cohort_size, 2) as retention_rate
FROM cohort_retention cr
JOIN cohort_sizes cs ON cr.cohort_month = cs.cohort_month
WHERE cr.cohort_month >= '2023-01-01'
ORDER BY cr.cohort_month, cr.month_number;
```

#### 3. Advanced Time Series Analysis
```sql
-- Sales trend analysis with seasonality
WITH daily_sales AS (
    SELECT 
        DATE(order_date) as sale_date,
        SUM(total_amount) as daily_sales,
        COUNT(*) as order_count,
        AVG(total_amount) as avg_order_value
    FROM orders
    WHERE order_status = 'Completed'
        AND order_date >= CURRENT_DATE - INTERVAL '2 years'
    GROUP BY DATE(order_date)
),
sales_with_moving_avg AS (
    SELECT 
        sale_date,
        daily_sales,
        order_count,
        avg_order_value,
        AVG(daily_sales) OVER (
            ORDER BY sale_date 
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) as moving_avg_7day,
        AVG(daily_sales) OVER (
            ORDER BY sale_date 
            ROWS BETWEEN 29 PRECEDING AND CURRENT ROW
        ) as moving_avg_30day,
        LAG(daily_sales, 7) OVER (ORDER BY sale_date) as sales_7_days_ago,
        LAG(daily_sales, 365) OVER (ORDER BY sale_date) as sales_1_year_ago
    FROM daily_sales
)
SELECT 
    sale_date,
    daily_sales,
    moving_avg_7day,
    moving_avg_30day,
    ROUND(100.0 * (daily_sales - sales_7_days_ago) / NULLIF(sales_7_days_ago, 0), 2) as wow_growth_rate,
    ROUND(100.0 * (daily_sales - sales_1_year_ago) / NULLIF(sales_1_year_ago, 0), 2) as yoy_growth_rate,
    EXTRACT(DOW FROM sale_date) as day_of_week,
    EXTRACT(MONTH FROM sale_date) as month,
    CASE 
        WHEN daily_sales > moving_avg_30day * 1.2 THEN 'Above Average'
        WHEN daily_sales < moving_avg_30day * 0.8 THEN 'Below Average'
        ELSE 'Normal'
    END as performance_category
FROM sales_with_moving_avg
WHERE sale_date >= CURRENT_DATE - INTERVAL '6 months'
ORDER BY sale_date;
```

### Query Templates and Reusability

#### Template Library
```