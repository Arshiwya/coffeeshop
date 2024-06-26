from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models import F
from products.models import Product


class Order(models.Model):
    STATUS_VOID = 0
    STATUS_PAID = 10
    STATUS_CANCELED = 20
    STATUS_CHOICES = (

        (STATUS_VOID, 'Unknown'),
        (STATUS_PAID, 'Paid'),
        (STATUS_CANCELED, 'Canceled by user.')
    )

    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    product = models.ManyToManyField('products.Product')
    total_amount = models.BigIntegerField()
    pay_amount = models.BigIntegerField()
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=STATUS_VOID)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Order'
        verbose_name = 'order'
        verbose_name_plural = 'orders'


class Discount(models.Model):
    user_id = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    product_id = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    discount_rate = models.BigIntegerField()
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Discount'
        verbose_name = 'discount'
        verbose_name_plural = 'discounts'


class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'
        verbose_name = 'cart'
        verbose_name_plural = 'carts'

    def __str__(self):
        return f"Cart for {self.user}"
    def clear(self):
        self.cartitem_set.all().delete()




class CartItem(models.Model):
    cart = models.ForeignKey(Cart,related_name='cartitems', verbose_name='cart',on_delete=models.CASCADE)
    item = models.ForeignKey(Product,related_name='cartitems',verbose_name='item', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'CartItem'
        verbose_name = 'cartitem'
        verbose_name_plural = 'cartitems'

    def increment_quantity(self):
        self.quantity = F('quantity') + 1
        self.save()

    def decrement_quantity(self):
        if self.quantity > 1:
            self.quantity = F('quantity') -1
            self.save()
        else:
            self.delete()

