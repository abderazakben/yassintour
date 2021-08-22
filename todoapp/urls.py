from django.urls import path

from . import views

app_name = 'todoapp'

urlpatterns = [
    path('Hotel/', views.indux, name="homePageHotel" ),
    path('update/<int:pk>/', views.update, name="update" ),
    path('delete/<int:pk>/', views.delete, name="delete" ),

] 