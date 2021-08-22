from django.db import models

# Create your models here.
#Task = mohima
class Task(models.Model):
    destinace = models.CharField(max_length=200 , blank=True , null=True)
    date = models.DateTimeField()
    namber_percen =  models.IntegerField(null=True ,blank=True ,verbose_name='Enter Your Nober percen')
    content = models.CharField(max_length=200 , blank=True , null=True)
    comlete = models.BooleanField(default=False)
    price =  models.IntegerField(null=True ,blank=True ,verbose_name='Enter Your price')
    def __str__(self):
        return self.content

