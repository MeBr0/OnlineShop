from rest_framework import serializers

from product.models import Category, Product


# default serializer for generic view
class CategorySerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', )


# serializer for ProductSerializer and ProductOrderSerializer
class CategoryProductSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField()

    class Meta:
        model = Category
        fields = ('id', 'name', )


# default serializer for generic view
class ProductSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    category = CategoryProductSerializer()

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'image_url', 'cost', 'count', 'category', )

    def create(self, validated_data):

        # get category from DB by id
        category_json = validated_data.pop('category')
        category = Category.objects.get(id=category_json['id'])

        product = Product.objects.create(category=category, **validated_data)

        return product


# serializer for OrderSerializer
class ProductOrderSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField()
    category = CategoryProductSerializer()

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'image_url', 'cost', 'count', 'category', )

    def create(self, validated_data):

        # get category from DB by id
        category_json = validated_data.pop('category')
        category = Category.objects.get(id=category_json['id'])

        product = Product.objects.create(category=category, **validated_data)

        return product
