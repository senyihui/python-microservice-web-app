import pika, json

# params = pika.URLParameters('your_rabbitmq_url')
params = pika.URLParameters('amqps://bckbphsf:8O87Jj4BMSK1RvMZ0mazx59h9kT21ngh@gerbil.rmq.cloudamqp.com/bckbphsf')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
