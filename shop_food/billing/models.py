
from django.db import models
from products.models import Cart
# Create your models here.


class PaymentType(models.TextChoices):
    cash = 'cash', 'cash'
    card = 'card', 'card'


class Billing(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=10, choices=PaymentType.choices, default=PaymentType.cash)
    comments = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comments[:10]
