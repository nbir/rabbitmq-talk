import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(virtual_host='guest'))
channel = connection.channel()

channel.exchange_declare(exchange='topics', exchange_type='topic')

channel.queue_declare(queue='error')
channel.queue_bind(exchange='topics', queue='error', routing_key='error.#')


def callback(ch, method, properties, body):
    print('Consumed... {}'.format(body))


try:
    print('Consuming error...')

    channel.basic_consume(callback, queue='error', no_ack=True)
    channel.start_consuming()

except:
    connection.close()
