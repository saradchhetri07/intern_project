from django.db import models
from django.utils.timezone import now

class Research(models.Model):
    rid=models.AutoField(primary_key=True)
    rname=models.CharField(max_length=20)
    rfield=models.CharField(max_length=20)
    rnumber_of_people=models.IntegerField()
    duration=models.IntegerField(default=30)
    rescshortdesc=models.CharField(max_length=50,default=None)
    research_start_time=models.DateField()
    dept_restriction=models.BooleanField()  
    research_department=models.CharField(max_length=20,default=None)
    def __str__(self):
        return self.rname
    