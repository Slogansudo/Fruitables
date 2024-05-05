from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from billing.models import Billing
from products.models import Comment, Category, Product, Cart
from customers.models import Country, City, Address, Customers
from .serializer import AddressSerializer, ProductSerializer, CustomersSerializer, CategorySerializer, CommentSerializer, CartSerializer, BillingSerializer,CountrySerializer, CitySerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.authentication import TokenAuthentication
# Create your views here.


class CountryAPIViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )


class CityAPIViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class AddressAPIViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class CustomersAPIViewSet(ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, )


class CommentAPIViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class CategoryAPIViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class ProductAPIViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class CartAPIViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class BillingAPIViewSet(ModelViewSet):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)