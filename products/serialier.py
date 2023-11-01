from rest_framework.serializers import ModelSerializer
from products.models import Product


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'              # all fields
        #fields = ('id','name','qty')    # only these fields will be json
        #exclude = ('id','name','qty')   #excluding id,name,qty -- all remaining fields will be in json