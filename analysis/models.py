from django.db import models


# Create your models here.
class DigitalStatistics(models.Model):
    id = models.AutoField(primary_key=True) 
    number = models.CharField(max_length=2)
    times = models.IntegerField(null=False)

    def __str__(self): # For better representation in the admin and elsewhere
        return f"{self.number}: {self.times}"