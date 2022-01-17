from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    #path('image_upload/', views.image_upload_view, name='image_upload_view'),
    
] 
