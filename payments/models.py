from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=250, verbose_name="Наименование товара")
    description = models.TextField(max_length=5000, blank=True, verbose_name="Описание")
    price = models.FloatField(max_length=20, verbose_name="Цена")

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def convert_to_usd(self):
        return f"{self.price:.2f}"

    def __str__(self):
        return self.name
