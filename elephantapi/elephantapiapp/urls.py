from django.urls import path, re_path

from elephantapiapp import views

app_name='elephantapiapp'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('sanctuary/create', views.create_sanctuary_view),
    path('sanctuary/read', views.read_sanctuary_view),
    path('sanctuary/update', views.update_sanctuary_view),
    path('sanctuary/delete', views.delete_sanctuary_view),
    path('sanctuary/country/read', views.read_country_view),
]