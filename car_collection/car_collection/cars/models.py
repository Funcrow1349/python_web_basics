from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from car_collection.cars.validators import year_is_valid


class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        validators=[MinLengthValidator(2, "The username must be a minimum of 2 chars")],
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        validators=[MinValueValidator(18)],
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name='First Name'
    )

    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name='Last Name'
    )

    profile_picture = models.URLField(
        verbose_name='Profile Picture',
        null=True,
        blank=True,
    )

    def get_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else:
            return ""


class Car(models.Model):
    SPORTS_CAR = "Sports Car"
    PICKUP = "Pickup"
    CROSSOVER = "Crossover"
    MINIBUS = "Minibus"
    OTHER = "Other"

    CAR_TYPES = {
        (SPORTS_CAR, SPORTS_CAR),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER, OTHER)
    }

    car_type = models.CharField(
        choices=CAR_TYPES,
        verbose_name="Type",
        null=False,
        blank=False,
    )

    car_model = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(2)],
        null=False,
        blank=False,
        verbose_name='Model'
    )

    year = models.IntegerField(
        validators=[year_is_valid],
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL'
    )

    price = models.FloatField(
        validators=[MinValueValidator(1)],
        null=False,
        blank=False,
    )
