import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Sanctuary
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

# Create your views here.
def index_view(request):
    return JsonResponse({ 'msg': "Welcome to Elephant API! Elephant Sanctuaries, Orphanages and Parks Around the World 🐘. See below for our available endpoints: ",                   
    'sanctuary/create': ''' - Creates a new sanctuary, receives: name, country and elephants_living. Visit it with a GET HTTP method to get more information about how it works''',

    'sanctuary/read': """- Displays all available sanctuaries in the Database. Visit it with a GET HTTP method to get more information about how it works""",
    
    'sanctuary/update': '''- Updates a created sanctuary, receives: id, name, country and elephants_living. Visit it with a GET HTTP method to get more information about how it works''',

    'sanctuary/delete': '''- Deletes a sanctuary with id equals the received query name id. Visit it with a GET HTTP method to get more information about how it works''',

    'sanctuary/country/read': '''- Displays all available countries in the Database. Visit it with a GET HTTP method to get more information about how it works''', 'status': 200})

@csrf_exempt
def create_sanctuary_view(request):

    if request.method == 'POST':
        name = request.GET.get('name')
        elephants_living = request.GET.get('elephants_living')
        country = request.GET.get('country')

        new_sanctuary = Sanctuary.objects.create(name = name, elephants_living = elephants_living, country = country)
        new_sanctuary.save()

        return JsonResponse({'msg': 'Sanctuary {0} registered with success!'.format(name)})
    
    return JsonResponse({'msg': '''Welcome to the create page 🐘, this page receives a POST method with name, elephants_living and country to register a sanctuary! Url example: http://localhost:8000/sanctuary/create?name=David%20Sheldrick%20Orphanage&elephants_living=500&country=Kenya''', 'status': 200})

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

    return JsonResponse({'msg': '''Welcome to the update page 🐘, this page receives a PUT or POST method with id, elephants_living, name and country. If you omit elephants_living, name and/or country, the values remain the same! Url example: http://localhost:8000/sanctuary/update?elephants_living=498&id=1&name=David%20Sheldrick%20Orphanage''', 'status': 200})

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
        
    return JsonResponse({'msg': '''Welcome to the update page 🐘, this page receives a DELETE or POST method with the id of the sanctuary you want to delete! Url example: http://localhost:8000/sanctuary/delete?id=1''', 'status': 200})

def read_country_view(request):
    return JsonResponse(Sanctuary.countries_list, safe=False)