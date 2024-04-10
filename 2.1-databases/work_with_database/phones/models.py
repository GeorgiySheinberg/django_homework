from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    price = models.CharField(max_length=50)
    image = models.CharField(max_length=100)
    release_date = models.CharField(max_length=50)
    lte_exists = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)


