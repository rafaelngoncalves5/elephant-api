import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Sanctuary, Country, Amount
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

# Create your views here.
def index_view(request):
    return JsonResponse({ 'Elephant API': "Elephant Sanctuaries, Orphanages and Parks Around the World 🐘" })

@csrf_exempt
def create_sanctuary(request):

    # Data received in the request
    amount = request.GET.get('amount')
    country = request.GET.get('country')
    name = request.GET.get('name')

    if request.method == 'POST':
        try:
            new_amount = Amount.objects.create(unities = amount)
            new_amount.save()
    
            new_country = Country(name = country)
            new_country.save()

            new_sanctuary = Sanctuary.objects.create(living_elephants = new_amount, location = new_country, name = name)
            new_sanctuary.save()

            return JsonResponse({'msg': 'Congratulations! You registered {0} as a new sanctuary'.format(name), 'status': 'OK'})
        except:
            pass

@csrf_exempt
def read_sanctuary(request):
    list_data = list(Sanctuary.objects.values())
    return JsonResponse(list_data, safe=False)

@csrf_exempt
def delete_sanctuary(request):
    id = request.GET.get('id')

    if request.method == 'POST':
        sanctuary = get_object_or_404(Sanctuary, pk=id)
        try:
            sanctuary.delete()
            sanctuary.save()
            return JsonResponse({'msg': 'Sanctuary {0} deleted with success!'.format(sanctuary.name)})
        except (KeyError, Sanctuary.DoesNotExist):
            pass

@csrf_exempt
def edit_sanctuary(request):
    id = request.GET.get('id')

    # Data received in the request
    amount = request.GET.get('amount')
    country = request.GET.get('country')
    name = request.GET.get('name')

    if request.method == 'POST':
        sanctuary = get_object_or_404(Sanctuary, pk=id)
        try:
            new_amount = Amount.objects.create(unities = amount)
            new_amount.save()
    
            new_country = Country(name = country)
            new_country.save()
            old_country = Country.objects.get(pk=new_country.id_country)
            old_country.delete()
            old_country.save()

            Sanctuary.objects.filter(id_sanctuary=sanctuary.id_sanctuary).update(living_elephants = new_amount, location = new_country, name = name)
        
            return JsonResponse({'msg': 'Sanctuary {0} edited with success!'.format(sanctuary.name)})       
        except (KeyError, Sanctuary.DoesNotExist):
            pass


@csrf_exempt
def read_location(request):
    list_data = list(Country.objects.values())
    return JsonResponse(list_data, safe=False)
