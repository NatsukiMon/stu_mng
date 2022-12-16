from django.urls import path
from . import views 
import student.views

urlpatterns = [
   path('', views.home, name="主页"),
    path('studentinfo/', student.views.studentinfo),
    path('insert/', student.views.insert),
    path('delete/', student.views.delete),
    path('update/', student.views.update),
    path('login/',student.views.login),
    path('register/',student.views.register),
    path('gradeinfo/',student.views.gradeinfo),
    path('changeinfo/',student.views.changeinfo),
    path('scinfo/',student.views.sc),
    path('deletesc/',student.views.deletesc),
    path('updatesc/',student.views.updatesc),
    path('insertsc/',student.views.insertsc)
]