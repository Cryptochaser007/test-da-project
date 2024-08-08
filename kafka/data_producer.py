import json
from kafka import KafkaProducer
import pandas as pd
import time
import logging
from kafka.errors import KafkaError

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize Kafka producer
try:
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=lambda x: json.dumps(x).encode('utf-8'),
                             retries=3)  # Add retries for robustness
    logger.info("Kafka producer initialized successfully")
except KafkaError as e:
    logger.error(f"Failed to initialize Kafka producer: {e}")
    raise

# Load the dataset
try:
    orders_df = pd.read_csv('olist_customers_dataset.csv')
    logger.info(f"Dataset loaded successfully. Shape: {orders_df.shape}")
except FileNotFoundError:
    logger.error("Dataset file not found")
    raise
except pd.errors.EmptyDataError:
    logger.error("Dataset file is empty")
    raise
except pd.errors.ParserError:
    logger.error("Error parsing the dataset file")
    raise

# Simulate streaming data
for index, row in orders_df.iterrows():
    data = row.to_dict()
    try:
        future = producer.send('ecommerce_data', value=data)
        record_metadata = future.get(timeout=10)
        logger.info(f"Sent: {data} | Topic: {record_metadata.topic} | Partition: {record_metadata.partition} | Offset: {record_metadata.offset}")
    except KafkaError as e:
        logger.error(f"Failed to send message: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
    
    time.sleep(1)  # Simulate delay between messages

producer.close()
logger.info("Producer closed")
