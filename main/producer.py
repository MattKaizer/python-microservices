import pika, json

params = pika.URLParameters(
    'amqps://vgstixrq:BipRo5apKKEo4c-tENoihuroiIjfPzu6@puffin.rmq2.cloudamqp.com/vgstixrq'
)


connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)