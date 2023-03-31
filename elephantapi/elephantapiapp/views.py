import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Sanctuary
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

# Create your views here.
def index_view(request):
    return JsonResponse({ 'Elephant API': "Elephant Sanctuaries, Orphanages and Parks Around the World 🐘" })

@csrf_exempt
def create_sanctuary_view(request):

    if request.method == 'POST':
        name = request.GET.get('name')
        elephants_living = request.GET.get('elephants_living')
        country = request.GET.get('country')

        new_sanctuary = Sanctuary.objects.create(name = name, elephants_living = elephants_living, country = country)
        new_sanctuary.save()

        return JsonResponse({'msg': 'Sanctuary {0} registered with success!'.format(name)})
    
    return JsonResponse({'msg': "Welcome to the create view!"})

def read_sanctuary_view(request):
    data = Sanctuary.objects.values()
    return JsonResponse(list(data), safe=False)

@csrf_exempt
def update_sanctuary_view(request):
    if request.method == 'PUT' or request.method == 'POST':
        # Get the id
        id = request.GET.get('id')
        # Get the other fields
        name = request.GET.get('name')
        elephants_living = request.GET.get('elephants_living')
        country = request.GET.get('country')

        sanctuary = get_object_or_404(Sanctuary, pk=id)

        if name is None or name == '' or name == 0 or name == ' ':
            name = sanctuary.name

        if elephants_living is None or elephants_living == '' or elephants_living == 0 or elephants_living == ' ':
            elephants_living = sanctuary.elephants_living

        if country is None or country == '' or country == 0 or country == ' ':
            country = sanctuary.country

        try:
            selected_sanctuary = Sanctuary.objects.get(pk = sanctuary.id)
            Sanctuary.objects.filter(id = selected_sanctuary.id).update(name = name, elephants_living = elephants_living, country = country)
            # Saving the DB
            for s in Sanctuary.objects.all():
                s.save()
            return JsonResponse({'msg': 'Sanctuary {0} updated with success!'.format(sanctuary), 'status': 200})

        except(KeyError, Sanctuary.DoesNotExist):
            return JsonResponse({'msg': 'Sanctuary with id {0} not found!'.format(id), 'status': 404})

    return JsonResponse({'msg': 'Welcome to the update page!'})

@csrf_exempt
def delete_sanctuary_view(request):

    if request.method == 'DELETE' or request.method == 'POST':
        # Get the id
        id = request.GET.get('id')
        sanctuary = get_object_or_404(Sanctuary, pk=id)

        try:
            selected_sanctuary = Sanctuary.objects.get(pk = sanctuary.id)
            selected_sanctuary.delete()
            return JsonResponse({'msg': 'Sanctuary {0} deleted with success!'.format(selected_sanctuary), 'status': 200})

        except(KeyError, Sanctuary.DoesNotExist):
            return JsonResponse({'msg': 'Sanctuary with id {0} not found!'.format(id), 'status': 404})
      
def read_country_view(request):
    return JsonResponse(Sanctuary.countries_list, safe=False)