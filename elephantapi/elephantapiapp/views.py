import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Sanctuary
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

# Create your views here.
def index_view(request):
    return JsonResponse({ 'Elephant API': "Elephant Sanctuaries, Orphanages and Parks Around the World 🐘" })

def create_sanctuary_view(request):

    if request.method == 'POST':
        pass
    
    return JsonResponse({'msg': "Welcome to the create view!"})

def read_country_view(request):
    return JsonResponse(Sanctuary.countries_list, safe=False)