import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    virtual_host='guest'))
channel = connection.channel()

channel.exchange_declare(exchange='x', exchange_type='direct')
channel.exchange_declare(exchange='dlx', exchange_type='direct')

channel.queue_declare(queue='x.queue',
                      arguments={
                          'x-dead-letter-exchange': 'dlx',
                      })
channel.queue_bind(exchange='x', queue='x.queue', routing_key='key')

channel.queue_declare(queue='dlx.queue',
                      arguments={
                          'x-message-ttl': 3000,
                          'x-dead-letter-exchange': 'x',
                      })
channel.queue_bind(exchange='dlx', queue='dlx.queue', routing_key='key')

message = 'Message: Some Imp. work.'

channel.basic_publish(exchange='x', routing_key='key', body=message)

print('Published... {}'.format(message))

connection.close()
