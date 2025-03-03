from confluent_kafka import Producer, Consumer

# Producer
conf = {'bootstrap.servers': 'localhost:9092'}
producer = Producer(conf)

def send_kafka_message(topic, message):
    producer.produce(topic, value=message)
    producer.flush() # Ensure message is delivered

# Consumer
conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'django-group',
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(conf)
consumer.subscribe(["analysis"])

def consume_messages():
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue 
        if msg.error():
            continue 
        print(f"Received message: {msg.value().decode('utf-8')}")
