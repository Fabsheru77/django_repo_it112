
from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home_view, name='home_view'),
  path('about/', views.About_Page_view, name='about_view'),
  path('function/', views.function_view, name='function_view'),
  path('class/', views.ClassView.as_view(), name='class_view'),
  path('coding/', views.Coding_view, name='coding_view'),
  path('theme/', views.ThemeView.as_view(), name='theme'),
  path('load/', views.load_default_data_view, name='load_default_data'),
  path('inventions/', views.InventionListView.as_view(), name='invention-list'),
  path('invention/<int:pk>/', 
  views.InventionDetailView.as_view(), name='invention-view'),
  
   path('invention/create/', views.InventionCreateView.as_view(), name='create_invention'),
    path('invention/<int:pk>/update/', views.InventionUpdateView.as_view(), name='update_invention'),
    path('invention/<int:pk>/delete/', views.InventionDeleteView.as_view(), name='delete_invention'),


  
]

