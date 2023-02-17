# Generated by Django 4.1.7 on 2023-02-17 06:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payments", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="item",
            options={"verbose_name": "Товар", "verbose_name_plural": "Товары"},
        ),
        migrations.AlterField(
            model_name="item",
            name="price",
            field=models.IntegerField(
                max_length=20,
                validators=[
                    django.core.validators.MinValueValidator(50),
                    django.core.validators.MaxValueValidator(10000000),
                ],
                verbose_name="Цена",
            ),
        ),
    ]
