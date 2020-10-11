# Generated by Django 3.0.6 on 2020-10-11 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200509_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselObjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pictures')),
                ('img_text', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]
