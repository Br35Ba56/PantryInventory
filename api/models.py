from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Item(models.Model):
    name = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    unit_quantity = models.DecimalField(decimal_places=2, max_digits=20, null=True)
    unit_type = models.CharField(max_length=100, null=True)
    acquisition_date = models.DateField(auto_now=False, null=True)
    expiration_date = models.DateField(auto_now=False, null=True)

    def __str__(self):
        return self.name + ' ' + str(self.acquisition_date)
