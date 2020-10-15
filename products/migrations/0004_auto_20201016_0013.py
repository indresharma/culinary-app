# Generated by Django 3.0.6 on 2020-10-15 18:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20201015_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_discount',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(10)]),
        ),
    ]