from utils.faker import generate_sales_transactions
from kafka import KafkaProducer
import json
from datetime import datetime
import time

transaction_topic = "transaction"

producer = KafkaProducer(
    bootstrap_servers=['localhost:9093'],  
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

curr_time = datetime.now()

try:
    while (datetime.now() - curr_time).seconds < 120:
        try:
            transaction = generate_sales_transactions()
            transaction['totalAmount'] = transaction['productPrice'] * transaction['productQuantity']
            
            print(transaction)
            
            # Send the transaction to Kafka
            producer.send(transaction_topic, value=transaction, key=transaction["transactionId"].encode('utf-8'))
            # Wait one second before sending the next transaction
            time.sleep(1)
            
        except BufferError:
            print("Buffer full, waiting...")
            time.sleep(1)
        except Exception as e:
            print(e)
finally:
    # Ensure all messages are sent before exiting
    producer.flush()
    producer.close()
