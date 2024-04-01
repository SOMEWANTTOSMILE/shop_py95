from rest_framework import serializers
from catalog.models import Category, Product, Product_img, Seller, Discount


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')


class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Product_img
        fields = ('image', )


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, source='product_img_set')

    class Meta:
        model = Product
        fields = ('id', 'article', 'name', 'price', 'images')


class SellerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seller
        fields = ('id', 'name', 'description')


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ('id', 'name' )


