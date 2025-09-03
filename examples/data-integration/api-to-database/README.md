# API to Database Pipeline

This pipeline demonstrates how to extract data from a REST API and load it into a PostgreSQL database using Mage.

## Overview

The pipeline performs the following steps:
1. **Extract**: Fetch data from a REST API (using JSONPlaceholder as example)
2. **Transform**: Clean and structure the data
3. **Load**: Insert the data into PostgreSQL database

## Features

- REST API data extraction
- Data validation and cleaning
- PostgreSQL integration
- Error handling and logging
- Configurable API endpoints

## Setup

### Prerequisites
- PostgreSQL database running
- Python 3.8+
- Required Python packages (see requirements.txt)

### Configuration

1. Update `io_config.yaml` with your database credentials:
```yaml
dev:
  POSTGRES_CONNECT_TIMEOUT: 10
  POSTGRES_DBNAME: "your_database"
  POSTGRES_USER: "your_username"
  POSTGRES_PASSWORD: "your_password"
  POSTGRES_HOST: "localhost"
  POSTGRES_PORT: 5432
```

2. Set environment variables in `.env`:
```env
API_BASE_URL=https://jsonplaceholder.typicode.com
API_ENDPOINT=/posts
```

## Usage

1. Import the pipeline into your Mage project
2. Configure your database connection
3. Run the pipeline manually or set up a schedule
4. Monitor execution in the Mage UI

## Pipeline Components

- **Data Loader**: Fetches data from REST API
- **Transformer**: Cleans and validates data
- **Data Exporter**: Loads data into PostgreSQL

## Sample Data

This example uses JSONPlaceholder API which provides fake JSON data for testing.
