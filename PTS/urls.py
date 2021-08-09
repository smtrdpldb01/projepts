from django.contrib import admin
from django.urls import path,include
from Pr0001 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('index/',views.index,name="index"),

    path('projects/',views.projects,name="projects"),
    
    path('project/<int:id>', views.project,name="project"),

    path('user/', include("user.urls")),
    path('Pr0001/', include("Pr0001.urls")),

]
