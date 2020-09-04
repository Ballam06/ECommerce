from django.db import models


class search(models.Model):

    keyword = models.CharField(max_length=400)
    date = models.CharField(max_length=400)
    page = models.CharField(max_length=400)
    position = models.CharField(max_length=400)
    title = models.CharField(max_length=400)
    author = models.CharField(max_length=400)
    publisher = models.CharField(max_length=400)
    pages = models.CharField(max_length=400)
    publication_date = models.CharField(max_length=400)
    sales_rank = models.CharField(max_length=400)
    page = models.IntegerField()
    image = models.CharField(max_length=400)
    asin = models.CharField(max_length=400)

class keys(models.Model):
    keyword = models.CharField(max_length=400)