from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

# Create your views here.

# def home(request):
#   return render(request,'projectMgt/project-list.html')

def signup(request):
  if request.method == 'POST':
    username = request.POST.get('username','')
    email = request.POST.get('email')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    
    if username and email and  password1 and password2:
      user = User.objects.create_user(username,email,password1)
      return redirect('login')
    else:
      print('wrong')
  else:
    print("show form")
      
  
  return render(request,'projectMgt/signup.html')

def log_in(request):
  if request.method == 'POST':
    email = request.POST.get('email','')
    password = request.POST.get('password','')
    
    if email and password:
      user = authenticate(request, email=email,password=password)
      if user is not None:
        login(request,user)
        return redirect('home')
      print(user)
  return render(request,'projectMgt/login.html')

@login_required
def projects(request):
  projects = Project.objects.filter(created_by=request.user).order_by('-id')
  return render(request,'projectMgt/project-list.html',{'projects':projects})

@login_required
def add_project(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    description = request.POST.get('description')
    if name:
      projects = Project.objects.create(name=name,description=description,created_by=request.user)
      return redirect('projects')
    
  return render(request,'projectMgt/add_project.html')

@login_required
def project_details(request,pk):
  project = Project.objects.filter(created_by=request.user).get(pk=pk)
  return render(request,'projectMgt/project-detail.html',{'project':project})


@login_required
def edit_project(request,pk):
  project = Project.objects.filter(created_by=request.user).get(pk=pk)
  if request.method == 'POST':
    name = request.POST.get('name')
    description = request.POST.get('description')
    if name:
      project.name = name
      project.description = description
      project.save()
      return redirect('projects')
  return render(request,'projectMgt/project-edit.html',{'project':project})


@login_required
def delete_project(request,pk):
  project = Project.objects.filter(created_by=request.user).get(pk=pk)
  if request.method == 'POST':
    project.delete()
    return redirect('projects')
 
  return render(request,'projectMgt/delete.html',{'obj':project})