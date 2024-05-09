
from django.shortcuts import render
from django.views import View
from .models import Product, Category, Comment, Cart
from customers.models import Customers
from django.contrib.auth.models import User
# Create your views here.


class ProductListView(View):
    def get(self, request):
        search = request.GET.get('search')
        print(search)
        if not search:
            products = Product.objects.all()
            categories = Category.objects.all()
            featured_products = Product.objects.all()
            cart = Cart.objects.filter(user=request.user)
            number_order = cart.count()
            context = {'products': products,
                       "categories": categories,
                       "featured_products": featured_products,
                       "number_order": number_order,
                       }
            return render(request, 'vegetable_web/shop.html', context)
        else:
            products = Product.objects.filter(title__icontains=search)
            featured_products = Product.objects.all()
            categories = Category.objects.all()
            cart = Cart.objects.filter(user=request.user)
            number_order = cart.count()
            context = {'products': products,
                       "categories": categories,
                       "featured_products": featured_products,
                       "number_order": number_order,
                       }
            return render(request, 'vegetable_web/shop.html', context)


class ProductDetailView(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            product = Product.objects.get(id=id)
            featured_products = Product.objects.all()
            categories = Category.objects.all()
            customers = Customers.objects.all()
            comments = Comment.objects.all()
            cart = Cart.objects.filter(user=request.user)
            number_order = cart.count()
            user_id = request.user.id
            " userning malumotlari faqat comment yozish uchun test qilishga olingan "
            user = User.objects.get(id=user_id)
            context = {
                'product': product,
                "categories": categories,
                'featured_products': featured_products,
                'customers': customers,
                'comments': comments,
                'user': user,
                'number_order': number_order,
            }
            return render(request, 'vegetable_web/shop-detail.html', context)
        else:
            return render(request, 'vegetable_web/shop-detail.html')

    def post(self, request, id):
        user = request.user
        text = request.POST.get('comment')

        # Izohni yaratish
        comment = Comment.objects.create(text=text, customer=user)
        comment.save()
        # Izohni mahsulotga qo'shish
        product = Product.objects.get(id=id)
        product.comments.add(comment)
        product.save()
        # Ma'lumotlarni shablonni render qilish uchun olish
        featured_products = Product.objects.all()
        categories = Category.objects.all()
        comments = Comment.objects.all()
        cart = Cart.objects.filter(user=request.user)
        number_order = cart.count()
        context = {
            'product': product,
            'categories': categories,
            'featured_products': featured_products,
            'comments': comments,
            'user': user,
            'number_order': number_order,
        }
        return render(request, 'vegetable_web/shop-detail.html', context)


class CartView(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        user = request.user
        Cart.objects.create(product=product, user=user)
        # Mahsulotlar uchun umumiy narxni va yetkazib berish narxini hisoblash
        total_price = 0
        shipping_price = 0
        for cart_product in Cart.objects.filter(user=request.user):
            total_price += cart_product.product.price
            shipping_price = cart_product.shipping_price
        cart = Cart.objects.filter(user=request.user)
        number_order = cart.count()
        context = {
            'product': product,
            'cart': cart,
            'number_order': number_order,
            'total_price_ship': total_price + shipping_price,
            'total_price': total_price,
            'shipping_price': shipping_price,
        }
        return render(request, 'vegetable_web/cart.html', context)

    def post(self, request, id):
        product = Product.objects.get(id=id)
        user = request.user
        cart_item = Cart.objects.filter(product=product, user=user).first()
        if cart_item:
            cart_item.delete()
        total_price = 0
        shipping_price = 0
        for cart_product in Cart.objects.filter(user=request.user):
            total_price += cart_product.product.price
            shipping_price = cart_product.shipping_price
        cart = Cart.objects.filter(user=request.user)
        number_order = cart.count()
        context = {
            'product': product,
            'cart': cart,
            'total_price_ship': total_price + shipping_price,
            'total_price': total_price,
            'number_order': number_order,
            'shipping_price': shipping_price,
        }
        return render(request, 'vegetable_web/cart.html', context)

