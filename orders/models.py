from django.db import models

# Create your models here.

class Order(models.Model):
    STATUS_VOID = 0
    STATUS_PAID = 10
    STATUS_CANCELED = 20
    STATUS_CHOICES = (

        (STATUS_VOID,'Unknown'),
        (STATUS_PAID,'Paid'),
        (STATUS_CANCELED,'Canceled by user.')
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
