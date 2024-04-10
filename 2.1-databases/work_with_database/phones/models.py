from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    price = models.CharField(max_length=50)
    image = models.CharField(max_length=100)
    release_date = models.CharField(max_length=50)
    lte_exists = models.CharField(max_length=50)
    # slug = models.SlugField(max_length=50)


