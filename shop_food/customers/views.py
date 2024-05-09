
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from products.models import Category, Comment, Product, Cart

# Create your views here.


class LandingPageView(View):
    def get(self, request):
        search = request.GET.get('search')
        print(search)
        if not search:
            categories = Category.objects.all()
            products = Product.objects.all()
            comments = Comment.objects.all()
            users = User.objects.filter(is_active=True)
            cart = Cart.objects.filter(user=request.user)
            number_product = products.count()
            number_customer = users.count()
            number_order = cart.count
            a = 1
            context = {
                'categories': categories,
                'products': products,
                'comments': comments,
                'number_order': number_order,
                'number_product': number_product,
                'number_customer': number_customer,
                'a': a,
            }
            return render(request, 'vegetable_web/index.html', context)
        else:
            categories = Category.objects.filter(title__icontains=search)
            products = Product.objects.filter(title__icontains=search)
            comments = Comment.objects.all()
            cart = Cart.objects.filter(user=request.user)
            users = User.objects.filter(is_active=True)
            number_product = products.count()
            number_order = cart.count()
            number_customer = users.count()
            a = 1
            context = {
                'categories': categories,
                'products': products,
                'comments': comments,
                'number_order': number_order,
                'number_product': number_product,
                'number_customer': number_customer,
                'a': a,
            }
            return render(request, 'vegetable_web/index.html', context)


class UsersLoginView(View):
    def get(self, request):
        return render(request, 'auth/login_users.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        data = {'username': username,
                'password': password
                }
        login_form = AuthenticationForm(data=data)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('landing')
        else:
            return render(request, 'auth/login_users.html')


class UsersLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('landing')


class UserRegisterView(View):
    def get(self, request):
        return render(request, 'auth/register_user.html')

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password_1']
        password2 = request.POST['password_2']
        if password1 != password2:
            return redirect('register')
        else:
            user = User(first_name=first_name, last_name=last_name, email=email, username=username)
            user.set_password(password1)
            user.save()
            return redirect('login')


class ContactView(View):
    def get(self, request):
        a = 1
        cart = Cart.objects.filter(user=request.user)
        number_order = cart.count()
        return render(request, 'vegetable_web/contact.html', {'a': a, 'number_order': number_order})


class ProfileView(View):
    def get(self, request):
        if request.user.is_authenticated:
            user = User.objects.get(username=request.user.username)
            cart = Cart.objects.filter(user=request.user)
            number_order = cart.count()
            return render(request, 'vegetable_web/profile.html', {'user': user, 'number_order': number_order})
        else:
            return render(request, 'vegetable_web/profile.html')

# 404 page nimagadir xartolik beryapdi


def my_custom_404_view(request, exception):
    return render(request, 'vegetable_web/404.html', status=404)
