import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(virtual_host='guest'))
channel = connection.channel()

channel.exchange_declare(exchange='topics', exchange_type='topic')

channel.queue_declare(queue='critical')
channel.queue_bind(exchange='topics',
                   queue='critical',
                   routing_key='#.critical')


def callback(ch, method, properties, body):
    print('Consumed... {}'.format(body))


try:
    print('Consuming critical...')

    channel.basic_consume(callback, queue='critical', no_ack=True)
    channel.start_consuming()

except:
    connection.close()
