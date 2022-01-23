from django.db import models

from .Research import Research
from .Student import Student
from .Teacher import Teacher
from .Project import Project
from .Others import Research_Teacher,Project_Student,Project_Teacher

#Research.people_requested=models.ManyToManyField(to=Student,default=None)
#Research.add_to_class(name='people_requested',value=models.ManyToManyField(to=Student,default=None))
#Project.add_to_class(name='people_requested',value=models.ManyToManyField(to=Student,default=None))