
from rest_framework.views import APIView
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from billing.models import Billing
from products.models import Comment, Category, Product, Cart
from customers.models import Country, City, Address, Customers
from .serializer import ProductSerializer, CategorySerializer, CommentSerializer, CartSerializer, BillingSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import LimitOffsetPagination
from django.db.transaction import atomic
from rest_framework.decorators import action
from datetime import datetime
# Create your views here.


"""class CountryAPIViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    #authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.SearchFilter, )
    search_fields = ['name', 'id']
    pagination_class = LimitOffsetPagination

    # http://api.example.org/accounts/?limit=100
    # /?offset=400&limit=100

    
class CityAPIViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter, )
    search_fields = ['name', 'country__name',]
    pagination_class = LimitOffsetPagination


class AddressAPIViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter, )
    search_fields = ['name', 'city__name', 'city__country__name',]
    pagination_class = LimitOffsetPagination


class CustomersAPIViewSet(ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
    #authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ['first_name', 'last_name', 'username', 'email', 'address__name', 'address__city__name', 'address__city__country__name', 'phone_number']
    pagination_class = LimitOffsetPagination"""


class CommentAPIViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['text', 'id', 'customer__first_name', 'customer__last_name', 'customer__username']
    pagination_classes = LimitOffsetPagination

    @action(detail=True, methods=['get'])
    def users(self, request, *args, **kwargs):
        comment = self.get_object()
        users = comment.customer
        serializer = UserSerializer(users)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def comments_count(self, request, *args, **kwargs):
        comments = self.get_queryset()
        data = comments.count()
        return Response(data=data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def today_comment(self, request, *args, **kwargs):
        comments = self.get_queryset()
        comments = comments.filter(created_date__icontains=datetime.now().date())
        serializer = CommentSerializer(comments, many=True)
        return Response(data=serializer.data)


class CategoryAPIViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title', 'created_date']
    pagination_class = LimitOffsetPagination

    @action(detail=False, methods=['get'])
    def re_order(self, request, *args, **kwargs):
        categories = self.get_queryset()
        categories = categories.order_by('-id')
        serializer = CategorySerializer(categories, many=True)
        return Response(data=serializer.data)

    @action(detail=False, methods=['get'])
    def national_category(self, request, *args, **kwargs):
        categories = self.get_queryset()
        categories = categories.filter(national=True)
        serializer = CategorySerializer(categories, many=True)
        return Response(data=serializer.data)

    @action(detail=True, methods=['get'])
    def products_count(self, request, *args, **kwargs):
        categories = self.get_object()
        products = Product.objects.filter(category=categories)
        products = products.count()
        categories.product_count = products
        categories.save()
        return Response(data=products)


class ProductAPIViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title', 'description', 'manufacturer_name', 'category__title', 'category__national', 'price', 'price_type', 'rating', 'max_weight', 'comments__text', 'comments__customer__username']
    pagination_class = LimitOffsetPagination

    @action(detail=False, methods=['get'])
    def re_order(self, request, *args, **kwargs):
        products = self.get_queryset()
        products = products.order_by('-id')
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data)

    @action(detail=True, methods=['POST'])
    def listen(self, request, *args, **kwargs):
        product = self.get_object()
        with atomic():
            product.popular_products += 1
            product.save()
            return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def top_popular_products(self, request, *args, **kwargs):
        products = self.get_queryset()
        products = products.order_by('-popular_products')[:1]
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data)

    @action(detail=True, methods=['get'])
    def category(self, request, *args, **kwargs):
        products = self.get_object()
        category = products.category
        serializer = CategorySerializer(category)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def unsold_products(self, request, *args, **kwargs):
        products = self.get_queryset()
        products = products.order_by('popular_products')[:2]
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CartAPIViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['product__title', 'product__category__title', 'product__price', 'product__rating', 'product_number', 'product__comments__customer__username']
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=['get'])
    def product(self, request, *args, **kwargs):
        cart = self.get_object()
        product = cart.product
        serializer = ProductSerializer(product)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def user(self, request, *args, **kwargs):
        cart = self.get_object()
        users = cart.user
        serializer = UserSerializer(users)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def today_orders(self, request, *args, **kwargs):
        cart = self.get_queryset()
        orders = cart.filter(created_date__icontains=datetime.now().date())
        serializer = CartSerializer(orders, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class BillingAPIViewSet(ModelViewSet):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['cart__id', 'user__last_name', 'user__username', 'cart__total_price', 'cart__product__title', 'price_type']
    pagination_class = LimitOffsetPagination

    @action(detail=False, methods=['get'])
    def most_payment_types(self, request, *args, **kwargs):
        billings = self.get_queryset()
        billings1 = billings.filter(payment_type__icontains='cash')
        billings2 = billings.filter(payment_type__icontains='card')
        if billings1.count() > billings2.count():
            serializer = BillingSerializer(billings1, many=True)
        else:
            serializer = BillingSerializer(billings2, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def cart(self, request, *args, **kwargs):
        billing = self.get_object()
        cart = billing.cart
        serializer = CartSerializer(cart)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def re_orders(self, request, *args, **kwargs):
        billing = self.get_queryset()
        orders = billing.order_by('-id')
        serializer = BillingSerializer(orders, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def payments_count(self, request, *args, **kwargs):
        billings = self.get_queryset()
        data = billings.count()
        return Response(data=data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def user(self, request, *args, **kwargs):
        billing = self.get_object()
        user = billing.cart.user
        serializer = UserSerializer(user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

