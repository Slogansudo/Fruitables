from django.shortcuts import render
from django.views.generic import View
from products.models import Cart, Comment


# Create your views here.


class CheckOutView(View):
    def get(self, request):
        cart = Cart.objects.filter(user=request.user)
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


class TestimonialView(View):
    def get(self, request):
        cart = Cart.objects.filter(user=request.user)
        number_order = cart.count()
        comment = Comment.objects.all()
        return render(request, 'vegetable_web/testimonial.html', {'number_order': number_order, "comment": comment})
