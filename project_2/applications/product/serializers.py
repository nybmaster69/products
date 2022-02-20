from rest_framework import serializers

from applications.product.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'slug')


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

        def to_representation(self, instance):
            representation = super().to_representation(instance)
            representation.pop('id')
            representation['category'] = CategorySerializer(Category.objects.get(product=instance.id)).data
            return representation
