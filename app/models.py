from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


CATEGORY_CHOICES = (
    ('M', 'Mobile'),
    ('L', 'Laptop'),
    ('TW', 'Top Wear'),
    ('BW', 'Bottom Wear'),
    ('SRV', 'Service'),
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField(null=True, blank=True)
    discounted_price = models.FloatField(null=True, blank=True)
    description = models.TextField(blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=3)
    product_image = models.ImageField(upload_to='productimg', blank=True, null=True)
    is_service = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ServicePrice(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='prices'
    )
    option = models.CharField(max_length=100)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.title} - {self.option} - ₹{self.price}"


class Cart(models.Model):
    session_key = models.CharField(max_length=100, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    service_price = models.ForeignKey(
        ServicePrice,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    quantity = models.PositiveIntegerField(default=1)

    @property
    def unit_price(self):
        if self.service_price:
            return self.service_price.price
        return self.product.discounted_price or self.product.selling_price or 0

    @property
    def total_price(self):
        return self.unit_price * self.quantity


class OrderPlaced(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('cancelled', 'Cancelled'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.FloatField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"

