from django.db import models
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Profile(models.Model, Importable):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()
    password = models.CharField(max_length=64)
    # phone_regex = RegexValidator(
    #     regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # phone_number = models.CharField(
    #     validators=[phone_regex], max_length=17, blank=True)  # Validators should be a list
    phone = PhoneNumberField()
    birthday = models.DateField(_(""), auto_now=False, auto_now_add=False)
    country = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    street_address = models.CharField(max_length=128)
    zip_postal_code = models.CharField(max_length=128)

    linkedin_Url = models.URLField()
    twitter_Url = models.URLField()
    facebook_Url = models.URLField()
