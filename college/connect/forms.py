from django import forms
from .models import *

class StudSignup(forms.ModelForm):
    class Meta:
        model=Student
        fields=('usn','sname','contact','email','sem','sdept','password')

        widgets={
            'sname':forms.TextInput(attrs={'class':'form-control','placeholder':'your name'}),
            'usn':forms.TextInput(attrs={'class':'form-control','placeholder':'your usn'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'your usn'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}),
            'contact':forms.NumberInput(attrs={'class':'form-control','placeholder':'mobile number'}),
            'sdept':forms.TextInput(attrs={'class':'form-control','placeholder':'department (e.g ise)'}),
            'sem':forms.NumberInput(attrs={'class':'form-conrol','placeholder':5})
        } 

class TeacherSignup(forms.ModelForm):
    class Meta:
        model=Teacher
        fields=('tid','tname','contact','email','tdept','password')

        widgets={
            'tid':forms.TextInput(attrs={'class':'form-control','placeholder':'teacher id'}),
            'tname':forms.TextInput(attrs={'class':'form-control','placeholder':'teacher name'}),
            'contact':forms.TextInput(attrs={'class':'form-control','placeholder':'mobile number'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'tdept':forms.TextInput(attrs={'class':'form-control','placeholder':'department(e.g. ise)'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'})
        }

class Login(forms.Form):
    Choices=(('Teacher','teacher'),('Student','student'))
    role=forms.ChoiceField(choices=Choices,label='role')
    id=forms.CharField(max_length=10,label='id')
    password=forms.CharField(max_length=20,label='password',widget=forms.PasswordInput)
    role.widget.attrs['class']='form-control'
    id.widget.attrs['class']='form-control'
    password.widget.attrs['class']='form-control'
    

class CreateProject(forms.Form):
    Choices=((True,'Yes'),(False,'No'))
    pname=forms.CharField(max_length=20,label='pname')
    time=forms.DurationField(label='time')
    starttime=forms.DateField(label='start',widget=forms.SelectDateWidget)
    projshortdesc=forms.CharField(label='desc')
    pfield=forms.CharField(label='pfield')
    branch_restriction=forms.ChoiceField(choices=Choices,label='branch')
    number_of_people=forms.IntegerField(label='people')

    pname.widget.attrs['class']='form-control'
    time.widget.attrs['class']='form-control' 
    starttime.widget.attrs['class']='form-control'
    pfield.widget.attrs['class']='form-control'
    branch_restriction.widget.attrs['class']='form-control'
    number_of_people.widget.attrs['class']='form-control'
    projshortdesc.widget.attrs['class']='form-control'
    time.widget.attrs['placeholder']='Ex. 30 '
    
class CreateResearch(forms.Form):
    Choices=((True,'Yes'),(False,'No'))
    rname=forms.CharField(max_length=20,label='rname')
    rfield=forms.CharField(max_length=20,label='rfield')
    rnumber_of_people=forms.IntegerField(label='people')
    duration=forms.DurationField(label='duration')
    rescshortdesc=forms.CharField(label='desc')
    starttime=forms.DateField(label='start',widget=forms.SelectDateWidget)
    dept_restriction=forms.ChoiceField(choices=Choices,label='dept')

    rname.widget.attrs['class']='form-control'
    duration.widget.attrs['class']='form-control' 
    starttime.widget.attrs['class']='form-control'
    rfield.widget.attrs['class']='form-control'
    dept_restriction.widget.attrs['class']='form-control'
    rnumber_of_people.widget.attrs['class']='form-control'
    rescshortdesc.widget.attrs['class']='form-control'
    duration.widget.attrs['placeholder']='Ex. 30 '
    



    