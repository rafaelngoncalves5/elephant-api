from django.urls import path

from elephantapiapp import views

app_name='elephantapiapp'
urlpatterns = [
    path('', views.index, name='index'),
]