from django.db import models
from django.core.validators import MinValueValidator, MaxLengthValidator
from datetime import date
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    #year = models.IntegerField(
    #    validators=[MinValueValidator(1611), MaxLengthValidator(date.today().year)])
    symbol = models.CharField(null=True, max_length=6)
    is_nasdaq = models.BooleanField(default=False)
    # set blank=True so that it automatically generate slug from save()
    # removed editable=False for readonly_fields in admin.py
    slug = models.SlugField(default="", blank=True, null=False, db_index=True) #opendoor technology => opendoor-technology
    
    def get_absolute_url(self):
        return reverse("company-detail", args=[self.slug])
    
    
    # slug will be auto generated using slugify
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    
    def __str__(self):
        return f"{self.name} ({self.year})"
    
