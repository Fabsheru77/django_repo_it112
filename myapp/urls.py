
from django.urls import path
from . import views

urlpatterns = [
  path('home/', views.Home_view, name='home_view'),
  path('about/', views.About_Page_view, name='about_view'),
  path('function/', views.function_view, name='function_view'),
  path('class/', views.ClassView.as_view(), name='class_view'),
  path('coding/', views.Coding_view, name='coding_view'),
  
]

