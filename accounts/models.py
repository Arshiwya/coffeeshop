from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    phone = models.CharField(max_length=20, null=True, blank=True)
    is_admin = models.BooleanField(default=False, verbose_name='Admin status')

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
