from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('login',views.log_in,name='login'),
    path('projects',views.projects,name='projects')
]
