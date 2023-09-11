from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Special(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.CharField(max_length=500)

class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    rating = models.PositiveIntegerField(default=5, validators=[MinValueValidator(0), MaxValueValidator(5)])
    description = models.CharField(max_length=500)