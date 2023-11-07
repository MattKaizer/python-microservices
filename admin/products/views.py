import random
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .producer import publish

from .serializers import ProductSerializer
from .models import Product, User


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/products
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        # publish('Hello World')
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish("product_created", serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish("product_updated", serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, pk=None):
        product = Product.objects.get(id=pk)
        product.delete()
        publish("product_deleted", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserApiView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({"id": user.id})