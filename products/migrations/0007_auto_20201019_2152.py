# Generated by Django 3.0.6 on 2020-10-19 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20201018_1656'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rmstock',
            options={'verbose_name': 'Raw Material Stock', 'verbose_name_plural': 'Raw Material Stock'},
        ),
        migrations.AddField(
            model_name='rmstock',
            name='payment_status',
            field=models.CharField(blank=True, choices=[('Done', 'Done'), ('Pending', 'Pending')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='rmstock',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='rmstock',
            name='supplier',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
