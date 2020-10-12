from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Tags(models.Model):
    tag = models.CharField(max_length=20)


class Product(models.Model):
    """Finished Products available for selling"""
    product = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    quantity_available = models.PositiveIntegerField(
        default=0, blank=True, null=True)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    tags = models.ManyToManyField('Tags')
    status = models.BooleanField(default=True, blank=True, null=True)
    product_discount = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(10)], blank=True, null=True)
    image = models.ImageField(upload_to='pictures', default='pictures/mypic.jpg')
    weight = models.PositiveSmallIntegerField(blank=True, null=True)
    height = models.PositiveSmallIntegerField(blank=True, null=True)
    color = models.CharField(max_length=15, blank=True, null=True)
    best_before = models.PositiveSmallIntegerField(blank=True, null=True)
    base_ingredient = models.CharField(max_length=25, blank=True, null=True)
    

    def __str__(self):
        if self.product:
            return self.product
        return f'Product No. {self.pk}'

    class Meta:
        permissions = (
            
        )

    
