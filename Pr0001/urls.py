from django.contrib import admin
from django.urls import path
from . import views

app_name="Pr0001"

urlpatterns = [
    path('dashboard/',views.dashboard,name="dashboard"),
    path('addproject/',views.addproject,name="addproject"),

    path('project/<int:id>',views.project,name="project"),
    path('update/<int:id>',views.updateProject,name="update"),
    path('delete/<int:id>',views.deleteProject,name="delete"),
]