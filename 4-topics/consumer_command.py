import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(virtual_host='guest'))
channel = connection.channel()

channel.exchange_declare(exchange='topics', exchange_type='topic')

channel.queue_declare(queue='command')
channel.queue_bind(exchange='topics', queue='command', routing_key='command.#')


def callback(ch, method, properties, body):
    print('Consumed... {}'.format(body))


try:
    print('Consuming command...')

    channel.basic_consume(callback, queue='command', no_ack=True)
    channel.start_consuming()

except:
    connection.close()
