from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


def validate_only_letters(value):
    if not value.isalpha():
        raise ValidationError


# Create your models here.
class PetstagramUser(AbstractUser):
    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'

    GENDERS = {
        (MALE, MALE),
        (FEMALE, FEMALE),
        (DO_NOT_SHOW, DO_NOT_SHOW)
    }

    email = models.EmailField(unique=True)
    first_name = models.CharField(
        max_length=30,
        validators=[MinLengthValidator(2), validate_only_letters]
    )
    last_name = models.CharField(
        max_length=30,
        validators=[MinLengthValidator(2), validate_only_letters]
    )

    profile_picture = models.URLField(null=True, blank=True)

    gender = models.CharField(
        choices=GENDERS
    )
