from django.urls import path, re_path

from elephantapiapp import views

app_name='elephantapiapp'
urlpatterns = [
    path('', views.index_view, name='index'),
    # Receives amount, country and name: http://localhost:8000/create?amount=5&country=India&name=Nagarhole%20National%20Park
    path('sanctuary/create', views.create_sanctuary, name='sanctuarry_create'),
    path('sanctuary/read', views.read_sanctuary, name='sanctuarry_read'),
    # Receives the id: http://localhost:8000/sanctuary/delete?id=1
    path('sanctuary/delete', views.delete_sanctuary, name='delete_sanctuary'),
    # Receives id, amount and name: http://localhost:8000/create?amount=5&country=India&name=Nagarhole%20National%20Park
    path('sanctuary/edit', views.edit_sanctuary, name='edit_sanctuary')
]