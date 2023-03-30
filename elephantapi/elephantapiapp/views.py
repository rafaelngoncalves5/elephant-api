from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Sanctuary, Country, Amount
from django.views.generic import CreateView
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return JsonResponse({ 'Elephant API': "Elephant Sanctuaries, Orphanages and Parks Around the World 🐘" })

@csrf_exempt
def create(request):
    amount = request.GET.get('amount')
    country = request.GET.get('country')
    if request.method == 'POST':
        # Sanctuary = 
        return JsonResponse({'msg': 'Welcome to the create view!', 'data': f'We received as data: {request}'})