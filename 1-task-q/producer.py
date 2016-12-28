import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(virtual_host='guest'))
channel = connection.channel()

channel.queue_declare(queue='task-queue', durable=True)

try:
    counter = 0

    while True:
        message = 'Long running job #{}'.format(counter)

        channel.basic_publish(exchange='',
                              routing_key='task-queue',
                              body=message)

        print('Published... {}'.format(message))

        time.sleep(1)
        counter += 1

except:
    connection.close()
