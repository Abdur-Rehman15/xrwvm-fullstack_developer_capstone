from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    founded_year = models.IntegerField(
        validators=[MinValueValidator(1800), MaxValueValidator(now().year)],
        null=True,
        blank=True
    )
    headquarters = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name

class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField()  # Refers to a dealer created in Cloudant database
    
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    COUPE = 'Coupe'
    TRUCK = 'Truck'
    VAN = 'Van'
    TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (COUPE, 'Coupe'),
        (TRUCK, 'Truck'),
        (VAN, 'Van'),
    ]
    
    name = models.CharField(max_length=100)
    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        default=SUV
    )
    year = models.IntegerField(
        default=2023,
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023)
        ]
    )
    engine = models.CharField(max_length=50, null=True, blank=True)
    horsepower = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"