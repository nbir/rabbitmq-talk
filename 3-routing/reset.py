import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(virtual_host='guest'))
channel = connection.channel()

channel.exchange_delete(exchange='routing')
channel.queue_delete(queue='ship')
channel.queue_delete(queue='truck')

connection.close()
