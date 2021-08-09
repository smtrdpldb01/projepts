from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render;HttpResponse,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Pr0001.models import Pr0001
from .models import Pr0001
from .forms import ProjectForm

def index(request):
    context={
        "number1":10,
        "number2":20,
        "number3":[1,2,3,4,5,6]
    }
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")

def projects(request):
    keyword=request.GET.get("keyword")
    if keyword:
        projects=Pr0001.objects.filter(title1__contains=keyword)
        return render(request,"projects.html",{"projects":projects})  
    projects=Pr0001.objects.filter()
    context={
        "projects":projects
    }
    projects=Pr0001.objects.all()
    return render(request,"projects.html",{"projects":projects})

def project(request,id):
    project=get_object_or_404(Pr0001,id=id)
    print(project)
    return render(request,"project.html",{"project":project})

@login_required(login_url="user:login")
def dashboard(request):
    projects=Pr0001.objects.filter(author=request.user)
    context={
        "projects":projects
    }
    return render(request,"dashboard.html",context)

@login_required(login_url="user:login")
def addproject(request):
    form=ProjectForm(request.POST or None)

    if form.is_valid():
        project=form.save(commit=False)
        project.author=request.user
        project.save()
        messages.success(request,"Proje başarıyla oluşturuldu.")
        return redirect("index")
    return render(request,"addproject.html",{"form":form})

@login_required(login_url="user:login")
def updateProject(request,id):
    project=get_object_or_404(Pr0001,id=id)
    form=ProjectForm(request.POST or None,request.FILES or None,instance=project)
    if form.is_valid():
        project=form.save(commit=False)
        project.author=request.user
        project.save()
        messages.success(request,"Proje başarıyla güncellendi.")
        return redirect("Pr0001:dashboard")
    return render(request,"update.html",{"form":form})

@login_required(login_url="user:login")
def deleteProject(request,id):
    project=get_object_or_404(Pr0001,id=id)
    project.delete()
    messages.success(request,"Proje başarıyla silindi.")
    return redirect("Pr0001:dashboard")