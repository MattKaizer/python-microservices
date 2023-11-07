import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product

params = pika.URLParameters(
    'amqps://vgstixrq:BipRo5apKKEo4c-tENoihuroiIjfPzu6@puffin.rmq2.cloudamqp.com/vgstixrq'
)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="admin")


def callback(ch, method, properties, body):
    print("Recieved in admin")
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print("Product liked incremented!")

channel.basic_consume(queue="admin", on_message_callback=callback, auto_ack=True)

print("Start consuming")

channel.start_consuming()

channel.close()
