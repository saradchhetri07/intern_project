from django.db import models
from django.utils.timezone import now
from .Research import Research
class Student(models.Model):
    usn=models.CharField(primary_key=True,max_length=10)
    sname=models.CharField(max_length=15)
    contact=models.CharField(max_length=10,default=None)
    email=models.EmailField(default=None)
    sem=models.IntegerField()
    sdept=models.CharField(max_length=20)
    password=models.CharField(max_length=20,default="connect123")
    rid=models.ForeignKey(to=Research,default=None, blank=True, null=True,on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.sname