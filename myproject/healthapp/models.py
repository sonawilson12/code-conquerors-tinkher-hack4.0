# healthapp/models.py
from django.db import models

class reg(models.Model):
    name    = models.CharField(max_length=100, null=True, blank=True)
    age     = models.IntegerField()
    email   = models.EmailField(unique=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    image   = models.FileField(upload_to='image/')

    def __str__(self):
        return self.name or self.email
    
    
    from django.db import models

class health(models.Model):
    gender = models.CharField(max_length=10, null=True, blank=True)
    age = models.IntegerField()
    weight = models.FloatField()   # in kg
    height = models.FloatField()   # in meters
    goal = models.CharField(max_length=20, null=True, blank=True)
    

    def __str__(self):
        return self.gender or str(self.age)
    
    
