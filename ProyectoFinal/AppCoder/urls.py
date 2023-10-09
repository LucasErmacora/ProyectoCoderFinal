from django.contrib import admin
from django.urls import path



from.views import cursos_view,inicio_view

urlpatterns = [
    path('cursos/', cursos_view, name='cursos_view'), 
    path('inicio/', inicio_view, name='inicio_view'),   
]