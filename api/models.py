from django.db import models

# Create your models here.
#class User(models.Model):
#    username=mdoels.CharField(max_length=10)

#class Pantry(models.Model):
#    pass

class Item(models.Model):
    name=models.CharField(max_length=100)
    quantity=models.IntegerField()
    acquisition_date=models.DateField(auto_now=False)

    def __str__(self):
        return self.name + ' ' + str(self.quantity) + ' ' + str(self.acquisition_date)
