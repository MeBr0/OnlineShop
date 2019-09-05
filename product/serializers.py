from django.shortcuts import get_object_or_404

from rest_framework import serializers

from product.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', )


class ProductSerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'image_url', 'cost', 'count', 'category', 'category_id')

    def create(self, validated_data):
        # pop and search category by id
        category_id = validated_data.pop('category_id')
        category = get_object_or_404(Category, id=category_id)

        # create product with given category
        product = Product.objects.create(category=category, **validated_data)

        return product
