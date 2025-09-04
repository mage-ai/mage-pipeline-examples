# Mage Pipeline Examples 🚀

A comprehensive collection of example pipelines built with [Mage](https://www.mage.ai/), the modern data orchestration platform. Use these pipelines to learn, explore, and jumpstart your own data workflows with Mage.

[![Mage](https://img.shields.io/badge/Mage-Data%20Orchestration-blue)](https://www.mage.ai/)
[![Python](https://img.shields.io/badge/Python-3.8+-green.svg)](https://www.python.org/)

## 🌟 What is Mage?

Mage is a modern data orchestration platform that simplifies building, running, and monitoring data pipelines. Unlike traditional orchestration tools, Mage offers:

- **🎯 Python-first approach** - Build pipelines using familiar Python syntax
- **📊 Interactive development** - Develop and test pipelines in a notebook-style interface
- **🔄 Real-time monitoring** - Built-in observability and monitoring capabilities
- **🧩 Modular architecture** - Reusable blocks for data loading, transformation, and exporting
- **☁️ Cloud-native** - Easy deployment to AWS, GCP, and Azure
- **🤖 ML-focused** - Specialized features for machine learning workflows

### 🚀 Mage Pro Features

For enterprise teams and production environments, **Mage Pro** provides:

- **💻 Enterprise Support** - Dedicated support and SLA guarantees
- **📊 Advanced Analytics** - Enhanced monitoring, alerting, and performance insights
- **🔒 Security & Compliance** - Enterprise-grade security features and compliance tools
- **⚡ High Performance** - Optimized for large-scale data processing
- **🌐 Multi-tenant Architecture** - Support for multiple teams and projects
- **🔄 Advanced Scheduling** - Complex scheduling and dependency management
- **📊 Custom Dashboards** - Tailored monitoring and reporting capabilities

## 📚 Pipeline Examples

This repository contains a comprehensive collection of pipeline examples organized by category:

### 📊 Data Integration
- **API to Database** - Extract data from REST APIs and load into databases
- **Multi-source Sync** - Combine data from multiple APIs, databases, and files
- **Database Replication** - Real-time database synchronization and replication

### 📦 Batch ETL
- **CSV Processing** - Process and transform CSV files with data validation
- **JSON ETL** - Extract, transform, and load JSON data from various sources
- **Combine Python and SQL** - Hybrid processing using both Python and SQL operations

### 🌊 Streaming Pipelines
- **Kafka Consumer** - Real-time data processing from Kafka streams
- **Real-time Analytics** - Live analytics and metrics calculation
- **Event Processing** - Process and route events in real-time

### 🤖 ML Models
- **Model Training** - End-to-end ML model training pipeline
- **Model Inference** - Deploy and serve ML models in production
- **Guide to Accuracy, Precision, and Recall** - Learn ML evaluation metrics

### 🔍 Data Quality
- **Validation Pipeline** - Automated data validation and quality checks
- **Monitoring Dashboard** - Real-time data quality monitoring and alerting
- **Anomaly Detection** - Detect and handle data anomalies automatically

### ☁️ Cloud Operations
- **S3 to RDS** - Transfer data from AWS S3 to RDS PostgreSQL
- **Multi-cloud Sync** - Cross-cloud data movement and synchronization
- **Infrastructure Monitoring** - Monitor cloud resources and costs

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Docker (recommended)
- Git
- **Mage Pro** - For enterprise features, advanced monitoring, and production-ready deployments

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/mage-pipeline-examples.git
   cd mage-pipeline-examples
   ```

2. **Set up Mage using Docker (Recommended):**
   ```bash
   # Clone Mage's quickstart template
   git clone https://github.com/mage-ai/compose-quickstart.git mage-setup
   cd mage-setup

   # Copy environment file
   cp dev.env .env

   # Start Mage
   docker compose up
   ```

3. **Access Mage UI:**
   Open your browser and navigate to `http://localhost:6789`

4. **Import a Pipeline:**

   **Method 1: Zip Upload (Recommended)**

   a. **Prepare the pipeline:**
      ```bash
      # Navigate to the pipeline directory you want to import
      cd examples/data-integration/api-to-database

      # Create a zip file of the pipeline
      zip -r api-to-database-pipeline.zip .
      ```

   b. **Upload to Mage:**
      - Open Mage UI at `http://localhost:6789`
      - Click on **"Pipelines"** in the left sidebar
      - Click **"Import"** button
      - Select **"Upload zip file"**
      - Choose your `api-to-database-pipeline.zip` file
      - Click **"Import"**

   c. **Verify import:**
      - The pipeline should appear in your pipelines list
      - Click on the pipeline to view and edit it
      - Follow the setup instructions in the pipeline's README

   **Method 2: Manual Copy**

   a. **Copy pipeline files:**
      ```bash
      # Copy the entire pipeline directory to your Mage project
      cp -r examples/data-integration/api-to-database/* /path/to/your/mage/project/pipelines/
      ```

   b. **Refresh Mage UI:**
      - The pipeline should appear automatically
      - If not, restart your Mage server

   **Method 3: Git Clone (For Development)**

   a. **Clone into Mage project:**
      ```bash
      # Navigate to your Mage project directory
      cd /path/to/your/mage/project

      # Clone specific pipeline
      git clone https://github.com/your-username/mage-pipeline-examples.git temp
      cp -r temp/examples/data-integration/api-to-database/* pipelines/
      rm -rf temp
      ```

### Post-Import Configuration

After importing a pipeline, you'll need to configure it for your environment:

1. **Install Dependencies:**
   ```bash
   # Install required Python packages
   pip install -r requirements.txt
   ```

2. **Configure Environment Variables:**
   ```bash
   # Create or update .env file in your Mage project root
   echo "API_KEY=your_api_key_here" >> .env
   echo "DATABASE_URL=your_database_url_here" >> .env
   ```

3. **Update IO Configuration:**
   ```bash
   # Edit io_config.yaml with your database and API credentials
   nano io_config.yaml
   ```

4. **Test the Pipeline:**
   - Open the pipeline in Mage UI
   - Click **"Run"** to test the pipeline
   - Check logs for any errors
   - Verify data output

### Alternative: Local Installation

```bash
# Install Mage
pip install mage-ai

# Start Mage server
mage start your_project_name
```

## 📖 How to Use This Repository

### 1. Browse Examples
Each pipeline example is organized in its own directory with:
- `README.md` - Detailed explanation and setup instructions
- Pipeline files - The actual Mage pipeline code
- `requirements.txt` - Python dependencies
- Sample data (if applicable)

### 2. Choose Your Pipeline Category
- **Data Integration** (`examples/data-integration/`) - Connect and sync data from various sources
- **Batch ETL** (`examples/batch-etl/`) - Process large datasets in batches
- **Streaming Pipelines** (`examples/streaming-pipelines/`) - Real-time data processing
- **ML Models** (`examples/ml-models/`) - Machine learning workflows and MLOps
- **Data Quality** (`examples/data-quality/`) - Data validation and monitoring
- **Cloud Operations** (`examples/cloud-ops/`) - Cloud infrastructure and data movement

### 3. Import the Pipeline
Choose your preferred import method:
- **Zip Upload** (Recommended) - Upload pipeline as zip file through Mage UI
- **Manual Copy** - Copy files directly to your Mage project
- **Git Clone** - Clone specific pipeline for development

### 4. Configure and Run
Each pipeline includes:
- Prerequisites and dependencies
- Configuration steps
- Sample data setup
- Running instructions

### 5. Customize for Your Use Case
- Modify data sources and destinations
- Adjust transformation logic
- Add your own business logic
- Scale for your data volume

## 🏗️ Pipeline Structure

Mage pipelines typically consist of three main components:

### Data Loaders
Extract data from various sources:
```python
@data_loader
def load_data_from_api(*args, **kwargs):
    # Your data loading logic here
    return data
```

### Transformers
Process and transform your data:
```python
@transformer
def transform_data(data, *args, **kwargs):
    # Your transformation logic here
    return transformed_data
```

### Data Exporters
Load data to destinations:
```python
@data_exporter
def export_data_to_database(data, *args, **kwargs):
    # Your data export logic here
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file in your Mage project root:
```env
# Database Configuration
POSTGRES_DBNAME=your_database
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

# API Keys
API_KEY=your_api_key
WEATHER_API_KEY=your_weather_api_key

# Cloud Configuration
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
```

### IO Configuration
Configure data connections in `io_config.yaml`:
```yaml
dev:
  POSTGRES_CONNECT_TIMEOUT: 10
  POSTGRES_DBNAME: "{{ env_var('POSTGRES_DBNAME') }}"
  POSTGRES_USER: "{{ env_var('POSTGRES_USER') }}"
  POSTGRES_PASSWORD: "{{ env_var('POSTGRES_PASSWORD') }}"
  POSTGRES_HOST: "{{ env_var('POSTGRES_HOST') }}"
  POSTGRES_PORT: "{{ env_var('POSTGRES_PORT') }}"
```

## 📊 Monitoring and Observability

Mage provides built-in monitoring capabilities:

- **Pipeline Execution History** - Track all pipeline runs
- **Real-time Logs** - Monitor pipeline execution in real-time
- **Data Quality Metrics** - Built-in data validation and quality checks
- **Performance Metrics** - Track execution time and resource usage
- **Error Handling** - Automatic retry and failure notifications

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Adding New Examples
1. Fork the repository
2. Create a new directory for your pipeline example
3. Include:
   - `README.md` with detailed instructions
   - Pipeline code files
   - `requirements.txt`
   - Sample data (if applicable)
4. Submit a pull request

### Guidelines
- Follow Python best practices (PEP 8)
- Include comprehensive documentation
- Test your pipelines before submitting
- Use descriptive commit messages
- Update this README if adding new categories

### Pipeline Requirements
- Clear, well-commented code
- Comprehensive setup instructions
- Error handling and validation
- Sample data or data generation scripts
- Documentation of data sources and destinations

## 📚 Learning Resources

### Official Documentation
- [Mage Documentation](https://docs.mage.ai/)
- [Mage GitHub Repository](https://github.com/mage-ai/mage-ai)
- [Mage Community](https://www.mage.ai/community)

### Tutorials and Guides
- [Getting Started with Mage](https://docs.mage.ai/getting-started)
- [Building Your First Pipeline](https://docs.mage.ai/tutorials/building-your-first-pipeline)
- [Deploying to Production](https://docs.mage.ai/production)

### Community
- [Mage Discord](https://discord.gg/mage-ai)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/mage-ai)
- [GitHub Discussions](https://github.com/mage-ai/mage-ai/discussions)

## 🐛 Troubleshooting

### Common Issues

**Pipeline fails to start:**
- Check your Python dependencies in `requirements.txt`
- Verify environment variables are set correctly
- Ensure data sources are accessible

**Database connection errors:**
- Verify database credentials in `io_config.yaml`
- Check network connectivity
- Ensure database is running and accessible

**Import errors:**
- Install missing dependencies: `pip install -r requirements.txt`
- Check Python version compatibility
- Verify import paths

### Getting Help
- Check the [Mage Documentation](https://docs.mage.ai/)
- Search [GitHub Issues](https://github.com/mage-ai/mage-ai/issues)
- Join the [Mage Discord](https://discord.gg/mage-ai)
- Create an issue in this repository

## 📞 Support

If you find this repository helpful, please:
- ⭐ Star the repository
- 🍴 Fork it for your own use
- 🐛 Report issues
- 💡 Suggest new examples
- 📢 Share with your network

---

**Happy Data Orchestrating! 🎉**

*Built with ❤️ using [Mage](https://www.mage.ai/)*
