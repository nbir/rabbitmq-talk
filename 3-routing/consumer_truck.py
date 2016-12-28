import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(virtual_host='guest'))
channel = connection.channel()

channel.exchange_declare(exchange='routing', exchange_type='direct')

channel.queue_declare(queue='truck')
channel.queue_bind(exchange='routing', queue='truck', routing_key='mexico')


def callback(ch, method, properties, body):
    print('Consumed on [truck]... {}'.format(body))


try:
    print('Consuming on truck...')

    channel.basic_consume(callback, queue='truck', no_ack=True)
    channel.start_consuming()

except:
    connection.close()
