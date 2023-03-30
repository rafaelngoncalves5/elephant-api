from django.urls import path, re_path

from elephantapiapp import views

app_name='elephantapiapp'
urlpatterns = [
    path('', views.index, name='index'),
    # Receives amount and country: http://localhost:8000/create?amount=5&country=India&name=Nagarhole%20National%20Park
    path('create', views.create, name='create'),

]