

from rest_framework import serializers
from billing.models import Billing
from products.models import Comment, Category, Product, Cart
from django.contrib.auth.models import User


"""class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'created_date']


class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)

    class Meta:
        model = City
        fields = ['id', 'name', 'country', 'created_date']


class AddressSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Address
        fields = ['id', 'name', 'city', 'created_date']


class CustomersSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Customers
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'address', 'created_date']
"""


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'username', 'first_name', 'last_name', 'email'


class CommentSerializer(serializers.ModelSerializer):
    customer = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'text', 'customer', 'last_update']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'national', 'title', 'image', 'created_date']


class ProductSerializer(serializers.ModelSerializer):
   class Meta:
       model = Product
       fields = ['id', 'title', 'description', 'category', 'image', 'price', 'popular_products', 'price_type', 'rating', 'comments']


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'


class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = '__all__'
