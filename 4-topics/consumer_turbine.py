import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(virtual_host='guest'))
channel = connection.channel()

channel.exchange_declare(exchange='topics', exchange_type='topic')

channel.queue_declare(queue='turbine')
channel.queue_bind(exchange='topics',
                   queue='turbine',
                   routing_key='*.turbine.*')


def callback(ch, method, properties, body):
    print('Consumed... {}'.format(body))


try:
    print('Consuming turbine...')

    channel.basic_consume(callback, queue='turbine', no_ack=True)
    channel.start_consuming()

except:
    connection.close()
