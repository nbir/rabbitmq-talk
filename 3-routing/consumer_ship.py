import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(virtual_host='guest'))
channel = connection.channel()

channel.exchange_declare(exchange='routing', exchange_type='direct')

channel.queue_declare(queue='ship')
channel.queue_bind(exchange='routing', queue='ship', routing_key='china')
channel.queue_bind(exchange='routing', queue='ship', routing_key='russia')


def callback(ch, method, properties, body):
    print('Consumed on ship... {}'.format(body))


try:
    print('Consuming on ship...')

    channel.basic_consume(callback, queue='ship', no_ack=True)
    channel.start_consuming()

except:
    connection.close()
