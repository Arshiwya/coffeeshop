from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from orders.models import Cart, CartItem


class User(AbstractUser):
    phone = models.CharField(max_length=20, null=True, blank=True)
    is_admin = models.BooleanField(default=False, verbose_name='Admin status')
    email = models.EmailField(unique=True, verbose_name='email', null=False, blank=False)

    class Meta:
        db_table = 'User'
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        if self.first_name:
            if self.last_name:
                return self.first_name + ' ' + self.last_name
            else:
                return self.first_name

        else:
            return self.username

    def __str__(self):
        return self.get_full_name()

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        if not Cart.objects.filter(user=self).exists():
            Cart.objects.create(user=self)


class Contact(models.Model):
    GOOD = 1
    EXCELLENT = 2
    BAD = 3

    STATUS_CHOICES = (
        (GOOD, 'Good'),
        (EXCELLENT, 'Excellent'),
        (BAD, 'Bad')
    )
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=GOOD)

    class Meta:
        db_table = 'Contact'
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'

    def __str__(self):
        return self.user.get_full_name()
