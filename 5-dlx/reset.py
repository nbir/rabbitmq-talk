import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(virtual_host='guest'))
channel = connection.channel()

channel.exchange_delete(exchange='x')
channel.exchange_delete(exchange='dlx')
channel.queue_delete(queue='x.queue')
channel.queue_delete(queue='dlx.queue')

connection.close()
