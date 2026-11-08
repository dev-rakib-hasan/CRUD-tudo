from django.urls import path
from . import views


urlpatterns = [
    path('add/', views.add, name='add'),
    path('get_all/', views.get_all, name='get_all'),
    path('get/<int:pk>/', views.get, name='get'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
  
]
