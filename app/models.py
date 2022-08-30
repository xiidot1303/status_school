from django.db import models

class Application(models.Model):
    name = models.CharField(null=True, blank=False, max_length=255)
    degree = models.IntegerField(null=True, blank=False)
    phone = models.CharField(null=True, blank=False, max_length=32)
    office = models.CharField(null=True, blank=False, max_length=255)
    time = models.CharField(null=True, blank=False, max_length=255)
    address = models.CharField(null=True, blank=False, max_length=255)
    payment = models.CharField(null=True, blank=True, max_length=255)
    published = models.DateTimeField(null=True, blank=True, db_index=True, auto_now_add=True)

