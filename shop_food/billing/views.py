from django.shortcuts import render, redirect
from django.views.generic import View
from products.models import Cart, Comment
from .models import Billing
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class CheckOutView(LoginRequiredMixin, View):
    def get(self, request):
        cart = Cart.objects.filter(user=request.user, payment_status=False)
        user = request.user
        total_price = 0
        quantity = 0
        number_order = 0
        for car in cart:
            total_price += car.product.price
            number_order += 1
        for car in cart:
            dat = car.product
            if dat.title == car.product.title:
                quantity = 1
        return render(request, 'vegetable_web/chackout.html', {"cart": cart, "user": user, "total_price": total_price, "quantity": quantity, "number_order": number_order})

    def post(self, request):
        shipping = request.POST.get("Shipping-1")
        transfer = request.POST.get("Transfer")
        payments = request.POST.get("Payments")
        delivery = request.POST.get("Delivery")
        paypal = request.POST.get("Paypal")
        print(shipping, transfer, payments, delivery, paypal)
        cart = Cart.objects.get(user=request.user)
        cart.payment_status = True
        cart.save()
        billing = Billing.objects.create(cart=cart, payment_type=cart.product.price_type)
        billing.save()
        return redirect('landing')


class TestimonialView(LoginRequiredMixin, View):
    def get(self, request):
        cart = Cart.objects.filter(user=request.user)
        number_order = cart.count()
        comment = Comment.objects.all()
        return render(request, 'vegetable_web/testimonial.html', {'number_order': number_order, "comment": comment})
