# E-commerce Data Pipeline and Analytics Dashboard

This project demonstrates the development of a data pipeline and analytics dashboard for an e-commerce use case.

## Project Overview
The project involves the following key steps:
1. Data Collection: Ingesting e-commerce data from a public dataset using Apache Kafka.
2. Data Storage: Designing a data warehouse schema and implementing data storage.
3. Data Processing: Performing ETL (Extract, Transform, Load) jobs using Apache Spark or Python scripts.
4. Data Analysis: Conducting exploratory data analysis and calculating key metrics.
5. Data Visualization: Creating an interactive dashboard using Tableau, Power BI, or a web framework.
6. Automation and Scheduling: Setting up automated data refresh and pipeline execution using Apache Airflow.
7. Documentation and Testing: Writing clear documentation and implementing unit tests.
8. Version Control and CI/CD: Using Git for version control and setting up a basic CI/CD pipeline.

## Getting Started

1. Clone the repository: git clone https://github.com/your-username/e-commerce-data-pipeline.git
cd e-commerce-data-pipeline

2. Set up the environment: `make setup`
3. Start the Kafka server: `make start-kafka`
4. Run the data producer: `make run-producer`
5. Run the data consumer: `make run-consumer`
6. Run the tests: `make test`
7. Proceed with the remaining steps of the project, such as data storage, processing, analysis, and visualization.
-------------------------------------------------------------------------------------------------------------------------------------------

1. Install the required dependencies by running `pip install -r requirements.txt`.
2. Download the "Brazilian E-Commerce Public Dataset by Olist" from Kaggle and place the `olist_orders_dataset.csv` file in the `data/` directory.
3. Follow the instructions in the `data_producer.py` and `data_consumer.py` files to set up and run the Kafka-based data ingestion process.
4. Proceed with the remaining steps of the project, such as data storage, processing, analysis, and visualization.

## Project Structure
- `data_producer.py`: Python script that simulates streaming data ingestion into Kafka.
- `data_consumer.py`: Python script that consumes data from the Kafka topic and processes the messages.
- `requirements.txt`: Lists the Python dependencies required for the project.
- `data/`: Directory containing the e-commerce dataset file.

## Contributing
Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please feel free to open a new issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
