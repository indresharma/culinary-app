# Generated by Django 3.0.2 on 2020-05-09 13:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_comments_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='calories',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='recipe',
            name='paid_recipe',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='recipe',
            name='preparation_time',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='qty',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='unit',
            field=models.CharField(choices=[('teaspoon', 'Teaspoon'), ('tablespoon', 'Tablespoon'), ('unit', 'Unit'), ('add_to_taste', 'Add to taste')], default='unit', max_length=20),
        ),
    ]