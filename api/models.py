from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import date

class Item(models.Model):
    name = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity_with_unit = models.CharField(max_length=100, null=True, blank=True)
    acquisition_date = models.DateField(null=False, blank=False)
    expiration_date = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.name + ' ' + str(self.acquisition_date)