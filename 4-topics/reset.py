import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(virtual_host='guest'))
channel = connection.channel()

channel.exchange_delete(exchange='topics')
channel.queue_delete(queue='command')
channel.queue_delete(queue='error')
channel.queue_delete(queue='turbine')
channel.queue_delete(queue='critical')

connection.close()
