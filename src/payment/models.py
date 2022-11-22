from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=300)
    price = models.FloatField()

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'

    def __str__(self):
        return self.name
