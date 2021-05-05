from django.db import models
from uuid import uuid4

class Books(models.Model):
    id_book = models.UUIDField(primary_key = True, default = uuid4, editable = False)
    title = models.CharField(max_length = 255)
    isbn = models.IntegerField()
    authors = models.CharField(max_length = 255)
    publishing_company = models.CharField(max_length = 255)
    edition = models.IntegerField()
    number_pages = models.IntegerField()
    description = models.CharField(max_length = 255)
