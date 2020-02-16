from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Item(models.Model):
    name = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity_with_unit = models.CharField(max_length=100, null=True)
    acquisition_date = models.DateField(auto_now=False, null=True)
    expiration_date = models.DateField(auto_now=False, null=True)

    def __str__(self):
        return self.name + ' ' + str(self.acquisition_date)
