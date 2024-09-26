from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth import authenticate,login

# Create your views here.

def home(request):
  return render(request,'projectMgt/project-list.html')

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

def projects(request):
  return render(request,'projectMgt/project-list.html')
