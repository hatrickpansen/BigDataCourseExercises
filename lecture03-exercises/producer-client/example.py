from kafka import KafkaProducer
import time

kc = KafkaProducer(bootstrap_servers=['kafka:9092'])

messages = ["hej", "med", "dig"]
for message in messages:
    kc.send('foo', f'{message}'.encode()) 

string = str(input())

kc.send('foo', f'{message}'.encode())
