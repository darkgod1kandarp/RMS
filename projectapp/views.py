from django.shortcuts import render,redirect
from .forms import form,teacherForm
from .models import check,teach
# Create your views here.

def next(request):
    if request.method =='POST':
        profflog = teacherForm(request.POST,request.FILES)
        if profflog.is_valid():
            profflog.save()
            profflog = teacherForm()
            return render(request ,'teacher.html',{'prof':profflog})
      
    else:
        profflog = teacherForm()

        
    return render(request ,'teacher.html',{'prof':profflog})
def click(request):
    if request.method=="POST":
        if request.POST.get('see'):
            return render(request,'afterteacher.html')
            
        else:
            return redirect('LP')
    else:
        return render(request,'inbetween.html')



def login(request): 
    if request.method =="POST":
        log  = form(request.POST)
        if log.is_valid():
            data = request.POST.copy()
            email = data.get('email')
            passwword = data.get('password')
            section = data.get('section')
            checking_email = check.objects.values('email')
            checking_password = check.objects.values('password')
            checking_section = check.objects.values('section')
            em = []
            ps = []
            sec = []
            for i in checking_email:
                em.append(i['email'])
            for i in checking_password:
                ps.append(i['password'])
            for i in checking_section:
                sec.append(i['section'])
            for i in range(len(em)):
                if email==em[i] and passwword ==ps[i] and section==sec[i]:
                    if section=="teacher"or section=="Teacher":
                        return redirect('IN')
                        break
                    else:
                        return redirect('INBS')
            else:
                er = 'Either password is wrong or email id is wrong'
                
                return render(request,'form.html',{'error':er ,'form':log})

    else:
        log = form()
    return render(request ,'form.html',{'form':log})
        

def inbetweenstudent(request):
    dict1 = {}
    all= teach.objects.all()
    filename = []
    check_name = teach.objects.values('name')
    for i in check_name:
        if dict1.get(i['name'])==None:
            filename.append(i['name'])
            dict1[i['name']] = 1

    if request.method == "POST":
        
        for i in check_name:
            for j in request.POST.keys():
                if j==i['name']:
                    naming_convention = j
                    print(naming_convention)
                    return render(request ,'student.html',{'forms':all ,'name':naming_convention})
    
    return render(request,'inbetweenstudent.html',{'forms':filename})
    