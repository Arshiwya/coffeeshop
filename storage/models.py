from django.db import models


class Material(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name="name")
    image = models.ImageField(blank=True)
    amount = models.BigIntegerField(default=0)

    class Meta:
        db_table = "Material"
        verbose_name = "Material"
        verbose_name_plural = "Materials"

    def __str__(self):
        return self.name
