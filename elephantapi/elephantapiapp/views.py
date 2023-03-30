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

    # Data received in the request
    amount = request.GET.get('amount')
    country = request.GET.get('country')
    name = request.GET.get('name')

    if request.method == 'POST':

        new_amount = Amount.objects.create(unities = amount)
        new_amount.save()
    
        new_country = Country(name = country)
        new_country.save()

        new_sanctuary = Sanctuary.objects.create(fk_amount = new_amount, fk_country = new_country, name = name)
        new_sanctuary.save()

        return JsonResponse({'msg': 'Congratulations! You registered {0} as a new sanctuary'.format(name), 'status': 'OK'})