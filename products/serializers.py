# serializers.py
from rest_framework import serializers
from products.models import ItemMaster

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemMaster
        fields = ['CATEGORY']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemMaster
        fields = ['BRAND']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemMaster
        fields = '__all__'
