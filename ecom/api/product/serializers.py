from rest_framework import serializers

 #TODO: Define a serializer

from .models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(max_length=None, allow_null=True, required=False)
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'stock', 'is_active', 'image','category','created_at', 'updated_at')