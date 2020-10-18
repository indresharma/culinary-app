from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class BaseTracker(models.Model):
    created_by = models.ForeignKey(
        User, related_name='created_%(class)s', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tags(BaseTracker):
    tag = models.CharField(max_length=20)


class Product(BaseTracker):
    """Finished Products available for selling"""
    product = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    quantity_available = models.PositiveIntegerField(
        default=0, blank=True, null=True)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    tags = models.ManyToManyField('Tags')
    status = models.BooleanField(default=True, blank=True, null=True)
    product_discount = models.PositiveSmallIntegerField(default=0,
        validators=[MaxValueValidator(10)], blank=True, null=True)
    image = models.ImageField(upload_to='pictures',
                              default='pictures/mypic.jpg')
    weight = models.PositiveSmallIntegerField(blank=True, null=True)
    best_before = models.PositiveSmallIntegerField(blank=True, null=True)
    base_ingredient = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        if self.product:
            return self.product
        return f'Product No. {self.pk}'

    class Meta:
        permissions = (
            ('access_dashboard', 'Access Dashboard'),
        )

    def get_status(self):
        if self.status:
            return 'Active'
        return 'Disabled'


##### Raw Materials ########

UNITS = (
    (1, 'Grams.'),
    (2, 'Pcs.'),
    (3, 'Milli-Litres.'),
    (4, 'KiloGrams.'),
    (5, 'Litres.'),
)


class RawMaterial(BaseTracker):
    item = models.CharField(max_length=25, blank=True, null=True)
    quantity_available = models.PositiveSmallIntegerField(
        blank=True, null=True)
    unit = models.PositiveSmallIntegerField(
        choices=UNITS, blank=True, null=True)

    def __str__(self):
        return self.item


class RMStock(BaseTracker):
    item = models.ForeignKey(
        'RawMaterial', on_delete=models.CASCADE, related_name='rm_stock')
    quantity = models.PositiveSmallIntegerField(blank=True, null=True)
    validity = models.DateField(blank=True, null=True)
