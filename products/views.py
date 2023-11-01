from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from products.serialier import ProductSerializer
from products.models import Product

'''
mixins.CreateModelMixin - POST - ADD/INSERT     --1
mixins.RetrieveModelMixin- GET - SINGLE         --2
mixins.UpdateModelMixin - PUT/PATCH - update
mixins.DestroyModelMixin - DELETE -> delete/remove
mixins.ListModelMixin  - GET - list

'''
from rest_framework.permissions import AllowAny,IsAuthenticated

class ProductOperations(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)



