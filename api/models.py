from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Item(models.Model):
    name = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    acquisition_date = models.DateField(auto_now=False)
    expiration_date = models.DateField()

    def __str__(self):
        return self.name + ' ' + str(self.acquisition_date)
