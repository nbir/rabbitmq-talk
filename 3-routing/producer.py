import pika
import random
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
    virtual_host='guest'))
channel = connection.channel()

channel.exchange_declare(exchange='routing', exchange_type='direct')

routing_keys = ['china', 'mexico', 'russia']

try:
    while True:
        routing_key = random.choice(routing_keys)
        message = 'Message for {}'.format(routing_key.title())

        channel.basic_publish(exchange='routing',
                              routing_key=routing_key,
                              body=message)

        print('Published... {}'.format(message))

        time.sleep(1)

except:
    connection.close()
