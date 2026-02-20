from django.db import models

# Create your models here.
class reg(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    age=models.IntegerField()
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    image=models.FileField(upload_to='image/')