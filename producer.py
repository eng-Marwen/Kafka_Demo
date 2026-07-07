from kafka import KafkaProducer
import uuid

producer_config = {
    'bootstrap_servers': 'localhost:9092'
}
producer = KafkaProducer(producer_config)

orders={
    "order_id": str(uuid.uuid4()),
    "customer_id": 123,
    "order_date": "2023-06-01",
}
