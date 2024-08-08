from kafka import KafkaConsumer
from kafka.errors import KafkaError
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize Kafka consumer
try:
    consumer = KafkaConsumer('ecommerce_data',
                             bootstrap_servers=['localhost:9092'],
                             auto_offset_reset='earliest',
                             value_deserializer=lambda x: json.loads(x.decode('utf-8')),
                             group_id='ecommerce_group',
                             enable_auto_commit=True,
                             auto_commit_interval_ms=5000)
    logger.info("Kafka consumer initialized successfully")
except KafkaError as e:
    logger.error(f"Failed to initialize Kafka consumer: {e}")
    raise

# Consume messages
try:
    for message in consumer:
        try:
            logger.info(f"Received: {message.value} | Topic: {message.topic} | Partition: {message.partition} | Offset: {message.offset}")
        except json.JSONDecodeError:
            logger.error(f"Failed to decode message: {message.value}")
        except Exception as e:
            logger.error(f"Unexpected error processing message: {e}")
except KafkaError as e:
    logger.error(f"Kafka error: {e}")
except KeyboardInterrupt:
    logger.info("Consumer stopped by user")
finally:
    consumer.close()
    logger.info("Consumer closed")
