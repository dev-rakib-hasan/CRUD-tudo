from rest_framework import serializers
from . models import Product

# create serializer here
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        
        