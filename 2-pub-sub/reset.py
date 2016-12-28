import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(virtual_host='guest'))
channel = connection.channel()

channel.exchange_delete(exchange='pub-sub')

connection.close()
