from faker import Faker
import random
from datetime import datetime
import pytz

fake = Faker()

def generate_sales_transactions():
    user = fake.simple_profile()
    now = datetime.now(pytz.utc)  # Get the current UTC time with timezone info
    
    # Manually format milliseconds
    transaction_date = now.strftime('%Y-%m-%dT%H:%M:%S.') + f"{now.microsecond // 1000:03d}" + now.strftime('%z')
    
    return {
        "transactionId": fake.uuid4(),
        "productId": random.choice(['product1', 'product2', 'product3', 'product4', 'product5', 'product6']),
        "productName": random.choice(['laptop', 'mobile', 'tablet', 'watch', 'headphone', 'speaker']),
        'productCategory': random.choice(['electronic', 'fashion', 'grocery', 'home', 'beauty', 'sports']),
        'productPrice': round(random.uniform(10, 1000), 2),
        'productQuantity': random.randint(1, 10),
        'productBrand': random.choice(['apple', 'samsung', 'oneplus', 'mi', 'boat', 'sony']),
        'currency': random.choice(['USD', 'GBP']),
        'customerId': user['username'],
        'transactionDate': transaction_date,
        "paymentMethod": random.choice(['credit_card', 'debit_card', 'online_transfer'])
    }
