from django.db import models
from django.utils.timezone import now
from .Project import Project
from .Research import Research
from .Student import Student
from .Teacher import Teacher

class Project_Teacher(models.Model):
    class Meta:
        unique_together = ('tid','pid')
    tid=models.ForeignKey(to=Teacher,on_delete=models.RESTRICT)
    pid=models.ForeignKey(to=Project,on_delete=models.CASCADE)
 
    def __str__(self):
        return "tid:{} pid:{}".format(self.tid.tid,self,pid.pid)


class Project_Student(models.Model):
    class Meta:
        unique_together = ('pid','usn')
    pid=models.ForeignKey(to=Project,on_delete=models.CASCADE)
    usn=models.ForeignKey(to=Student,on_delete=models.RESTRICT)

    def __str__(self):
        return "project id:{} usn:{}".format(self.pid.pid,self.usn.usn)

class Research_Teacher(models.Model):
    class Meta:
        unique_together = ('rid','tid')
    rid=models.ForeignKey(to=Research,on_delete=models.CASCADE)
    tid=models.ForeignKey(to=Teacher,on_delete=models.RESTRICT)
    
    def __str__(self):
        return "research id:{} tid:{}".format(self.rid.rid,self.tid.tid)
    