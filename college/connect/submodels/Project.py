from django.db import models
from django.utils.timezone import now

class Project(models.Model):
    pid=models.AutoField(primary_key=True)
    pname=models.CharField(max_length=20)
    time=models.IntegerField(default=30)
    starttime=models.DateField(default=now)
    projshortdesc=models.TextField(default=None)
    pfield=models.CharField(max_length=20)
    branch_restriction=models.BooleanField(default=False)
    project_branch=models.CharField(max_length=20,default=None)
    number_of_people=models.IntegerField()

    def __str__(self):
        return self.pname

