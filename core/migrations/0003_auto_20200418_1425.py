# Generated by Django 3.0.5 on 2020-04-18 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200417_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='mypic.jpg', upload_to='pictures'),
        ),
    ]
