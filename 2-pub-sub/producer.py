import pika
import sys
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(virtual_host='guest'))
channel = connection.channel()

channel.exchange_declare(exchange='pub-sub', exchange_type='fanout')

try:
    counter = 0

    while True:
        message = 'Message {}'.format(counter)

        channel.basic_publish(exchange='pub-sub', routing_key='', body=message)

        print('Published... {}'.format(message))

        time.sleep(1)
        counter += 1

except:
    connection.close()
