from django.db import models

# Create your models here.
class Orders(models.Model):
    firstname = models.CharField(max_length=255, null=False, blank=False)
    secondname = models.CharField(max_length=255, null=False, blank=False)
    patronymic = models.CharField(max_length=255, null=True, blank=False)
    address = models.CharField(max_length=255, null=False, blank=False)
    type = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.secondname



