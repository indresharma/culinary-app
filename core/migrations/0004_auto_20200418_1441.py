# Generated by Django 3.0.5 on 2020-04-18 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200418_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='pictures/mypic.jpg', upload_to='pictures'),
        ),
    ]
