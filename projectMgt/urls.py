from django.urls import path
from . import views 

urlpatterns = [
    # path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('login',views.log_in,name='login'),
    path('',views.projects,name='projects'),
    path('add-project',views.add_project,name='add-project'),
    path('<uuid:pk>/',views.project_details,name='project-detail'),
    path('<uuid:pk>/edit/',views.edit_project,name='project-edit'),
     path('<uuid:pk>/delete/',views.delete_project,name='project-delete')
]
