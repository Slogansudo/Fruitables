from django.shortcuts import render
from django.views.generic import View


# Create your views here.


class CheckOutView(View):
    def get(self, request):
        return render(request, 'vegetable_web/chackout.html')


class TestimonialView(View):
    def get(self, request):
        return render(request, 'vegetable_web/testimonial.html')
