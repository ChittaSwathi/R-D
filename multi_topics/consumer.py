from confluent_kafka import Consumer, KafkaError
import csv
import os
from datetime import datetime
import json

conf = {
 'bootstrap.servers': 'localhost:9092', 
 'group.id': 'my-group',
 'auto.offset.reset': 'earliest'
}

consumer = Consumer(conf)

topic = 'nasdaq' 
consumer.subscribe([topic]) #todo: multiple topics
while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print('Reached end of partition')
        else:
            print(f'Error: {msg.error()}')
    else:
        decoded_msg = json.loads(msg.value().decode("utf-8"))
        print(f'received {decoded_msg}')
        csv_file = decoded_msg["stock"]+'.csv'
        
        data_price = [(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), decoded_msg['price'])]
    
        if not os.path.exists(csv_file):
            with open(csv_file, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["time", "price"]) # Header
                writer.writerows(data_price)
        else:
            with open(csv_file, mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(data_price)