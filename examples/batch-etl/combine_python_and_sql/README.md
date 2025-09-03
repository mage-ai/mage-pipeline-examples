# Combine Python and SQL Pipeline

This pipeline demonstrates how to effectively combine Python data processing with SQL operations in Mage, showcasing the power of using both languages together for complex data transformations.

## Overview

The pipeline performs the following steps:
1. **Python Data Loading** - Load data using Python libraries (pandas, requests, etc.)
2. **SQL Transformation** - Apply complex transformations using SQL
3. **Python Post-processing** - Use Python for advanced analytics and ML operations
4. **Hybrid Export** - Combine SQL and Python for final data export

## Features

- **Hybrid Processing** - Seamlessly combine Python and SQL operations
- **Data Validation** - Use Python for data quality checks and SQL for data integrity
- **Advanced Analytics** - Leverage Python libraries (pandas, numpy, scipy) with SQL aggregations
- **Flexible Transformations** - Use SQL for complex joins and Python for custom logic
- **Performance Optimization** - Use SQL for large-scale operations and Python for detailed processing

## Use Cases

- **Complex Data Transformations** - When you need both SQL's power and Python's flexibility
- **Data Quality Pipeline** - SQL for data integrity, Python for anomaly detection
- **Analytics Workflows** - SQL for aggregations, Python for statistical analysis
- **ML Feature Engineering** - SQL for data preparation, Python for feature creation
- **Reporting Pipelines** - SQL for data extraction, Python for visualization

## Pipeline Architecture

```
Data Source → Python Loader → SQL Transformer → Python Processor → SQL Exporter
     ↓              ↓              ↓              ↓              ↓
  CSV/API      pandas/requests   JOIN/AGG      analytics      Database
```

## Setup

### Prerequisites
- PostgreSQL database (or compatible SQL database)
- Required Python packages (see requirements.txt)

### Configuration

1. **Database Setup:**
   ```sql
   -- Create sample tables for demonstration
   CREATE TABLE customers (
       customer_id INT PRIMARY KEY,
       name VARCHAR(100),
       email VARCHAR(100),
       registration_date DATE
   );
   
   CREATE TABLE orders (
       order_id INT PRIMARY KEY,
       customer_id INT,
       product_name VARCHAR(100),
       quantity INT,
       price DECIMAL(10,2),
       order_date DATE
   );
   ```

2. **Environment Variables:**
   ```env
   # Database Configuration
   POSTGRES_DBNAME=your_database
   POSTGRES_USER=your_username
   POSTGRES_PASSWORD=your_password
   POSTGRES_HOST=localhost
   POSTGRES_PORT=5432
   
   # API Configuration (if using external data)
   API_BASE_URL=https://api.example.com
   API_KEY=your_api_key
   ```

3. **IO Configuration (`io_config.yaml`):**
   ```yaml
   dev:
     POSTGRES_CONNECT_TIMEOUT: 10
     POSTGRES_DBNAME: "{{ env_var('POSTGRES_DBNAME') }}"
     POSTGRES_USER: "{{ env_var('POSTGRES_USER') }}"
     POSTGRES_PASSWORD: "{{ env_var('POSTGRES_PASSWORD') }}"
     POSTGRES_HOST: "{{ env_var('POSTGRES_HOST') }}"
     POSTGRES_PORT: "{{ env_var('POSTGRES_PORT') }}"
   ```

## Pipeline Components

### 1. Python Data Loader
- Loads customer data from API or CSV files
- Performs data cleaning and type conversion
- Handles missing values and data validation

### 2. SQL Transformer
- Complex joins between customers and orders tables
- Customer segmentation based on spending patterns
- Aggregations and calculations using SQL functions

### 3. Python Post-processor
- Statistical analysis using scipy and numpy
- Customer lifetime value predictions
- Anomaly detection algorithms

### 4. Hybrid Exporter
- Exports results to database using SQL
- Generates summary reports using Python
- Combines both approaches for optimal performance

## Usage

1. **Import the Pipeline:**
   ```bash
   # Create zip file
   cd examples/batch-etl/combine-python-and-sql
   zip -r combine-python-sql-pipeline.zip .
   
   # Upload to Mage UI
   # Go to Pipelines → Import → Upload zip file
   ```

2. **Configure Database:**
   - Set up PostgreSQL database
   - Update `io_config.yaml` with your credentials
   - Run the sample data setup

3. **Run the Pipeline:**
   - Open the pipeline in Mage UI
   - Click "Run" to execute
   - Monitor execution in real-time

4. **View Results:**
   - Check the `customer_analytics` table in your database
   - Review the analytics summary in the logs

## Performance Tips

1. **Use SQL for Large Operations:**
   - Joins, aggregations, and filtering
   - Data type conversions
   - Complex calculations

2. **Use Python for Advanced Analytics:**
   - Statistical analysis
   - Machine learning operations
   - Custom business logic
   - Data visualization

3. **Optimize Data Flow:**
   - Minimize data movement between SQL and Python
   - Use appropriate data types
   - Implement proper indexing

## Troubleshooting

**SQL Connection Issues:**
- Verify database credentials in `io_config.yaml`
- Check network connectivity
- Ensure database is running

**Python Import Errors:**
- Install required packages: `pip install -r requirements.txt`
- Check Python version compatibility
- Verify virtual environment

**Performance Issues:**
- Optimize SQL queries
- Use appropriate data types
- Consider data partitioning for large datasets

## Dependencies

```txt
pandas>=1.5.0
numpy>=1.21.0
scipy>=1.9.0
psycopg2-binary>=2.9.0
requests>=2.28.0
sqlalchemy>=1.4.0
```