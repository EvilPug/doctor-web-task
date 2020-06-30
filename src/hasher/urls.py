from django.urls import path

from . import views

app_name = 'hasher'

urlpatterns = [
    path('', views.index, name='index'),
    path('upload_file/', views.upload_file, name='favorite'),
    path('download_file/', views.download_file, name='download_file'),
    path('delete_file/', views.delete_file, name='delete_file'),
]
