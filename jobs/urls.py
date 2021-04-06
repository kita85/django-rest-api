from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('batch_jobs/', views.batch_jobs, name='batch_jobs'),
]
