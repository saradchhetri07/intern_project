from django.shortcuts import render,redirect
from .models import Project,Research
from math import ceil
from .forms import *
# Create your views here.

def home(request,num):
    projects=Project.objects.all()
    researchs=Research.objects.all()
    catp=Project.objects.values('pfield','pid')
    catp={item['pfield'] for item in catp}
    catr=Research.objects.values('rfield','rid')
    catr={item['rfield'] for item in catr}
    cats=catp.union(catr)
   
    try:
        usr_id=request.session['id']

    except:
        return redirect('/connect/login')
      
    if num==0:
        params={'projects':projects,'researchs':researchs,'topics':cats,'num':num,'id':usr_id}
        return render(request,'connect/home.html',params)
    if num==1:
        params={'projects':projects,'researchs':[],'topics':catp,'num':num,'id':usr_id}
        return render(request,'connect/home.html',params)
    if num==2:
        params={'projects':[],'researchs':researchs,'topics':catr,'num':num,'id':usr_id}
        return render(request,'connect/home.html',params)

def topics(request,num,topic):
    catp=Project.objects.values('pfield','pid')
    catp={item['pfield'] for item in catp}
    catr=Research.objects.values('rfield','rid')
    catr={item['rfield'] for item in catr}
    cats=catp.union(catr)
    projects=Project.objects.filter(pfield=topic)
    researchs=Research.objects.filter(rfield=topic)
    usr_id=request.session['id']
    if num==0:
        params={'projects':projects,'researchs':researchs,'topics':cats,'num':num,'id':usr_id}
        return render(request,'connect/home.html',params)
    if num==1:
        params={'projects':projects,'researchs':[],'topics':catp,'num':num,'id':usr_id}
        return render(request,'connect/home.html',params)
    if num==2:
        params={'projects':[],'researchs':researchs,'topics':catr,'num':num,'id':usr_id}
        return render(request,'connect/home.html',params)

def myprofile(request):
    if request.session['id']:
        if request.session['role']=="Student":
            s=Student.objects.get(pk=request.session['id'])
            ps=Project_Student.objects.filter(usn=s)
            projects=[]
            for i in range(len(ps)):
                p=ps[i]
                projects.append(p)
            if s.rid:
                research=s.rid
            else:
                research=''
            return render(request,'connect/myprofile.html',{'projects':projects,'research':research,'researchs':[]})
        if request.session['role']=="Teacher":
            t=Teacher.objects.get(pk=request.session['id'])
            pt=Project_Teacher.objects.filter(tid=t)
            projects=[]
            researchs=[]
            for i in range(len(pt)):
                p=pt[i]
                projects.append(p)
            rt=Research_Teacher.objects.filter(tid=t)
            for i in range(len(rt)):
                r=rt[i]
                researchs.append(r)
            return render(request,'connect/myprofile.html',{'projects':projects,'researchs':researchs,'research':''})
    else:
        return redirect('/connect/login')

def signup(request):
    return render(request,'connect/sign_up.html')

def signup_student(request):
    if request.method=='POST':
        form=StudSignup(request.POST)
        if form.is_valid():
            print('sss')
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/connect/signup')
        else:
            print(form.errors)
            return redirect('/connect/signup_student')

    else:
        form=StudSignup()
        return render(request,'connect/stud_signup.html',{'forms':form})


def signup_teacher(request):
    if request.method=='POST':
        form=TeacherSignup(request.POST)

        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/connect/signup')
        else:
            print(form.errors)
            return redirect('/connect/signup_teacher')

    else:
        form=TeacherSignup()
        return render(request,'connect/teacher_signup.html',{'forms':form})

def login(request):
    if request.method=='POST':
        data=request.POST
        if data['role']=='Teacher':
            teach=Teacher.objects.filter(tid=data['id'])
            if len(teach)==0:
                return redirect('/connect/login')
            if teach[0].password==data['password']:
                request.session['id']=data['id']
                request.session['role']=data['role']
                request.session.set_expiry(3000)
                return redirect('/connect/home/0')
            else:
                return redirect('/connect/login')
        elif data['role']=='Student':
            stud=Student.objects.filter(usn=data['id'])
            if len(stud)==0:
                return redirect('/connect/login')
            if stud[0].password==data['password']:
                request.session['id']=data['id']
                request.session['role']=data['role']
                request.session.set_expiry(3000)
                return redirect('/connect/home/0')
            else:
                return redirect('/connect/login')
        else:
            return redirect('/connect/login')
    else:
        return render(request,'connect/login.html',{'forms':Login})
    

def createproject(request): 
    if request.method=='POST':
        try:
            pname=request.POST['pname']
            pfield=request.POST['pfield']
            number_of_people=int(request.POST['number_of_people'])
            projshortdesc=request.POST['projshortdesc']
            if request.POST['branch_restriction']=='True':
                branch_restriction=True
            else:
                branch_restriction=False
            date=request.POST['starttime_year']+'-'+request.POST['starttime_month']+'-'+request.POST['starttime_day']
            starttime=date
            time=request.POST['time']
            if request.session['role']=='Student':
                s=Student.objects.get(pk=request.session['id'])
                branch=s.sdept
            else:
                t=Teacher.objects.get(pk=request.session['id'])
                branch=t.tdept
            
            p=Project.objects.create(pname=pname,pfield=pfield,number_of_people=number_of_people,projshortdesc=projshortdesc,branch_restriction=branch_restriction,starttime=starttime,time=time,project_branch=branch)
            p.save()
            if request.session['role']=='Student':
                ps=Project_Student.objects.create(pid=p,usn=s)
                ps.save()
            else:
                pt=Project_Teacher.objects.create(tid=t,pid=p)
                pt.save()
            msg='success'
        except:
            msg='failure'
        return render(request,'connect/createproject.html',{'forms':CreateProject,'msg':msg})

    return render(request,'connect/createproject.html',{'forms':CreateProject,'msg':'none'})

def createresearch(request):
    if request.method=='POST':
        try:
            rname=request.POST['rname']
            rfield=request.POST['rfield']
            rnumber_of_people=int(request.POST['rnumber_of_people'])
            rescshortdesc=request.POST['rescshortdesc']
            if request.POST['dept_restriction']=='True':
                dept_restriction=True
            else:
                dept_restriction=False
            date=request.POST['starttime_year']+'-'+request.POST['starttime_month']+'-'+request.POST['starttime_day']
            starttime=date
            time=request.POST['duration']
            if request.session['role']=='Student':
                s=Student.objects.get(pk=request.session['id'])
                branch=s.sdept
            else:
                t=Teacher.objects.get(pk=request.session['id'])
                branch=t.tdept
            
            #p=Project.objects.create(pname=pname,pfield=pfield,number_of_people=number_of_people,projshortdesc=projshortdesc,branch_restriction=branch_restriction,starttime=starttime,time=time,project_branch=branch)
            r=Research.objects.create(rname=rname,rfield=rfield,rnumber_of_people=rnumber_of_people,duration=time,rescshortdesc=rescshortdesc,research_start_time=starttime,dept_restriction=dept_restriction,research_department=branch)
            r.save()
            if request.session['role']=='Student':
                s.rid=r
                s.save()
            else:
                rt=Research_Teacher.objects.create(tid=t,rid=r)
                rt.save()
            msg='success'
        except:
            msg='failure'
        return render(request,'connect/createresearch.html',{'forms':CreateResearch,'msg':msg})

    return render(request,'connect/createresearch.html',{'forms':CreateResearch,'msg':'none'})  

def delete(request):
    if "pid" in request.GET:
        Project.objects.filter(pid=request.GET['pid']).delete()
        return redirect('/connect/myprofile')
    elif "rid" in request.GET:
        Research.objects.filter(rid=request.GET['rid']).delete()
        return redirect('/connect/myprofile')
    else:
        return redirect('/connect/myprofile')

def logout(request):
    try:
        del request.session['id']
        del request.session['role']
        return redirect('/connect/login')
    except:
        return redirect('/connect/login')
