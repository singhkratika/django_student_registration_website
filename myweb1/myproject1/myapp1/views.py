from django.shortcuts import render, redirect
from . models import Student 

# Create your views here.
def index1(request):
    msg=''
    if request.method=="POST":
        sturollno=request.POST['sturollno']
        stuname=request.POST['stuname']
        branch=request.POST['branch']
        email=request.POST['email']
        stu=Student(sturollno=sturollno,stuname=stuname,branch=branch,email=email)
        stu.save()
        msg='Registration is done.'
    stu=Student.objects.all()
    return render(request,"index1.html",{'msg':msg,'stu':stu})
def deletestu(request,sturollno):
    stu=Student.objects.get(sturollno=sturollno)
    stu.delete()
    return redirect('index1')
def updatestu(request,sturollno):
    stu=Student.objects.get(sturollno=sturollno)
    return render(request,"update.html",{'stu':stu})
def updatecode(request):
    sturollno=request.POST['sturollno']
    stuname=request.POST['stuname']
    branch=request.POST['branch']
    email=request.POST['email']
    Student.objects.filter(sturollno=sturollno).update(stuname=stuname,branch=branch,email=email)
    return redirect('index1')