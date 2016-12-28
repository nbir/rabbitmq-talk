import pika
import random
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
    virtual_host='guest'))
channel = connection.channel()

channel.exchange_declare(exchange='topics', exchange_type='topic')

routing_keys_types = ['command', 'error']
routing_keys_names = ['fuel', 'control-rod', 'turbine', 'water-supply']
routing_keys_levels = ['normal', 'critical']

try:
    while True:
        routing_keys_type = random.choice(routing_keys_types)
        routing_keys_name = random.choice(routing_keys_names)
        routing_keys_level = random.choice(routing_keys_levels)
        routing_key = '{}.{}.{}'.format(
            routing_keys_type, routing_keys_name, routing_keys_level)

        message = 'Message {}'.format(routing_key)

        channel.basic_publish(exchange='topics',
                              routing_key=routing_key,
                              body=message)

        print('Published... {}'.format(message))

        time.sleep(1)

except:
    connection.close()
